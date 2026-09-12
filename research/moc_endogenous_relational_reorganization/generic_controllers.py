"""Controles genéricos: B4 relacional, B5 generativo y B6 estructural."""

from __future__ import annotations

from dataclasses import dataclass, replace

from possibility_field import FieldDelta, PossibilityField, compare_fields, generate_field, select_best
from state_model import (
    GeneratorSpec, Relation, RelationalState, SourceType, assert_well_formed,
    record_edit,
)


@dataclass(frozen=True)
class ControllerResult:
    controller: str
    before: RelationalState
    after: RelationalState
    field_before: PossibilityField
    field_after: PossibilityField
    delta: FieldDelta
    action_before: str | None
    action_after: str | None
    structure_changed: bool


def _result(name: str, before: RelationalState, after: RelationalState,
            old_field: PossibilityField, new_field: PossibilityField) -> ControllerResult:
    old_action = select_best(old_field)
    new_action = select_best(new_field)
    return ControllerResult(
        name, before, after, old_field, new_field, compare_fields(old_field, new_field),
        old_action.action_id if old_action else None,
        new_action.action_id if new_action else None,
        before.structure_digest() != after.structure_digest(),
    )


class B4RelationalSelector:
    """Selecciona dentro de D/R/K/G fijos; control sin reorganización."""

    def run(self, state: RelationalState) -> ControllerResult:
        assert_well_formed(state)
        field = generate_field(state)
        selected = select_best(field)
        after = replace(state, selected_action=selected.action_id if selected else None)
        return _result("B4_RELATIONAL", state, after, field, field)


class B0Automatic:
    """Respuesta automática: toma el primer candidato del campo fijo."""

    def run(self, state: RelationalState) -> ControllerResult:
        assert_well_formed(state)
        field = generate_field(state)
        chosen = field.candidates[0] if field.candidates else None
        after = replace(state, selected_action=chosen.action_id if chosen else None)
        return _result("B0_AUTOMATIC", state, after, field, field)


class B1GenericReflection:
    """Segunda evaluación sobre exactamente las mismas alternativas."""

    def run(self, state: RelationalState) -> ControllerResult:
        assert_well_formed(state)
        field = generate_field(state)
        chosen = select_best(field)
        after = replace(state, selected_action=chosen.action_id if chosen else None)
        return _result("B1_GENERIC_REFLECTION", state, after, field, field)


class B2RewardOptimizer:
    """argmax del score disponible; el score no se interpreta como V."""

    def run(self, state: RelationalState) -> ControllerResult:
        assert_well_formed(state)
        field = generate_field(state)
        chosen = select_best(field)
        after = replace(state, selected_action=chosen.action_id if chosen else None)
        return _result("B2_REWARD", state, after, field, field)


class B3ConstrainedOptimizer:
    """argmax tras filtro exógeno `deny:<action_id>`; no edita K."""

    def run(self, state: RelationalState) -> ControllerResult:
        assert_well_formed(state)
        field = generate_field(state)
        denied = {item.removeprefix("deny:") for item in state.K
                  if item.startswith("deny:")}
        feasible = PossibilityField(
            tuple(candidate for candidate in field.candidates
                  if candidate.action_id not in denied),
            field.state_digest, field.generator_revision,
        )
        chosen = select_best(feasible)
        after = replace(state, selected_action=chosen.action_id if chosen else None)
        return _result("B3_CONSTRAINED", state, after, field, feasible)


class B5GenerativeReplanner:
    """Edita sólo el generador y vuelve a generar el campo."""

    def run(self, state: RelationalState, *, add_operation: str,
            event_id: str, timestamp: int, rationale: str) -> ControllerResult:
        assert_well_formed(state)
        old_field = generate_field(state)
        operations = state.generator.operations
        if add_operation not in operations:
            operations = operations + (add_operation,)
        generator = replace(state.generator, operations=operations,
                            revision=state.generator.revision + 1)
        provisional = replace(state, generator=generator)
        after = record_edit(
            state, provisional, event_id=event_id, timestamp=timestamp,
            actor="B5_GENERATIVE", operation="EDIT_GENERATOR", target="generator",
            source_ids=(state.generator.name,), source_type=SourceType.CONTROLLER_INTERVENTION,
            rationale=rationale,
        )
        new_field = generate_field(after)
        selected = select_best(new_field)
        after = replace(after, selected_action=selected.action_id if selected else None)
        return _result("B5_GENERATIVE", state, after, old_field, new_field)


class B6StructureEditor:
    """Edita D, R o K mediante una operación explícita y auditable."""

    def run(self, state: RelationalState, *, target: str, operation: str,
            payload: object, event_id: str, timestamp: int,
            rationale: str) -> ControllerResult:
        assert_well_formed(state)
        old_field = generate_field(state)
        provisional = state
        if target == "D" and operation == "UPSERT":
            node, value = payload
            data = dict(state.D)
            data[str(node)] = float(value)
            provisional = replace(state, D=data)
        elif target == "D" and operation == "REMOVE":
            data = dict(state.D)
            data.pop(str(payload), None)
            relations = tuple(r for r in state.R
                              if r.source != str(payload) and r.target != str(payload))
            provisional = replace(state, D=data, R=relations)
        elif target == "R" and operation == "ADD":
            if not isinstance(payload, Relation):
                raise TypeError("R ADD requires Relation")
            provisional = replace(state, R=state.R + (payload,))
        elif target == "R" and operation == "REMOVE":
            provisional = replace(state, R=tuple(r for r in state.R if r != payload))
        elif target == "K" and operation == "ADD":
            provisional = replace(state, K=state.K | {str(payload)})
        elif target == "K" and operation == "REMOVE":
            provisional = replace(state, K=state.K - {str(payload)})
        else:
            raise ValueError("unsupported structural edit")
        assert_well_formed(provisional)
        after = record_edit(
            state, provisional, event_id=event_id, timestamp=timestamp,
            actor="B6_STRUCTURE", operation=operation, target=target,
            source_ids=(str(payload),), source_type=SourceType.CONTROLLER_INTERVENTION,
            rationale=rationale,
        )
        new_field = generate_field(after)
        selected = select_best(new_field)
        after = replace(after, selected_action=selected.action_id if selected else None)
        return _result("B6_STRUCTURE", state, after, old_field, new_field)
