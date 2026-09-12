"""Hipótesis computacional MOC_R, aislada y no canónica.

La implementación no afirma que MOC cause reorganización en experiencias.  Es
un policy de laboratorio que aplica ediciones tipadas y auditables sobre el
mismo estado y con el mismo presupuesto que B6.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum

try:
    from .generic_controllers import ControllerResult
    from .possibility_field import compare_fields, generate_field, select_best
    from .state_model import (
        Relation, RelationalState, SourceType, assert_well_formed, record_edit,
    )
except ImportError:  # pragma: no cover - ejecución desde la carpeta
    from generic_controllers import ControllerResult
    from possibility_field import compare_fields, generate_field, select_best
    from state_model import (
        Relation, RelationalState, SourceType, assert_well_formed, record_edit,
    )


class MOCComponent(str, Enum):
    P = "P"
    EAF = "EAF"
    ACT = "ACT"
    V = "V"
    S = "S"


class EditTarget(str, Enum):
    DISTINCTION = "D"
    RELATION = "R"
    CONSTRAINT = "K"
    GENERATOR = "generator"


@dataclass(frozen=True)
class StructuralEdit:
    target: str
    operation: str
    payload: object
    rationale: str


def structural_diff(before: RelationalState,
                    target: RelationalState) -> tuple[StructuralEdit, ...]:
    """Compila un objetivo exógeno en ediciones atómicas, sin usar case_id.

    La misma función se entrega a B6 y MOC_R en el benchmark. Por ello el
    experimento prueba capacidad de transformación/traza, no comprensión de una
    instrucción en lenguaje natural.
    """
    edits: list[StructuralEdit] = []
    for node in sorted(set(before.D) - set(target.D)):
        edits.append(StructuralEdit("D", "REMOVE", node, "remove distinction"))
    for node in sorted(target.D):
        if node not in before.D or before.D[node] != target.D[node]:
            edits.append(StructuralEdit("D", "UPSERT", (node, target.D[node]),
                                        "upsert distinction"))
    before_relations = set(before.R)
    target_relations = set(target.R)
    for relation in sorted(before_relations - target_relations,
                           key=lambda r: (r.source, r.target, r.kind, r.weight)):
        edits.append(StructuralEdit("R", "REMOVE", relation, "remove relation"))
    for relation in sorted(target_relations - before_relations,
                           key=lambda r: (r.source, r.target, r.kind, r.weight)):
        edits.append(StructuralEdit("R", "ADD", relation, "add relation"))
    for constraint in sorted(before.K - target.K):
        edits.append(StructuralEdit("K", "REMOVE", constraint, "remove constraint"))
    for constraint in sorted(target.K - before.K):
        edits.append(StructuralEdit("K", "ADD", constraint, "add constraint"))
    return tuple(edits)


def _provisional(state: RelationalState, edit: StructuralEdit) -> RelationalState:
    if edit.target == "D" and edit.operation == "UPSERT":
        node, value = edit.payload
        data = dict(state.D)
        data[str(node)] = float(value)
        return replace(state, D=data)
    if edit.target == "D" and edit.operation == "REMOVE":
        node = str(edit.payload)
        data = dict(state.D)
        data.pop(node, None)
        return replace(state, D=data,
                       R=tuple(r for r in state.R
                               if r.source != node and r.target != node))
    if edit.target == "R" and edit.operation == "ADD":
        if not isinstance(edit.payload, Relation):
            raise TypeError("R ADD requires Relation")
        return replace(state, R=state.R + (edit.payload,))
    if edit.target == "R" and edit.operation == "REMOVE":
        return replace(state, R=tuple(r for r in state.R if r != edit.payload))
    if edit.target == "K" and edit.operation == "ADD":
        return replace(state, K=state.K | {str(edit.payload)})
    if edit.target == "K" and edit.operation == "REMOVE":
        return replace(state, K=state.K - {str(edit.payload)})
    raise ValueError(f"unsupported MOC_R edit: {edit.target}/{edit.operation}")


class MOCReorganization:
    """Aplica un script estructural con validación del tipado pentacórico."""

    allowed_components = frozenset(component.value for component in MOCComponent)

    def run(self, state: RelationalState, *, edits: tuple[StructuralEdit, ...],
            event_prefix: str, timestamp: int) -> ControllerResult:
        assert_well_formed(state)
        if set(state.D) != self.allowed_components:
            raise ValueError("MOC_R requires exactly P,EAF,ACT,V,S typed nodes")
        field_before = generate_field(state)
        current = state
        for index, edit in enumerate(edits):
            if isinstance(edit.payload, Relation):
                endpoints = {edit.payload.source, edit.payload.target}
                if not endpoints <= self.allowed_components:
                    raise ValueError("relation endpoints must be MOC typed components")
            provisional = _provisional(current, edit)
            assert_well_formed(provisional)
            current = record_edit(
                current, provisional,
                event_id=f"{event_prefix}:{index}", timestamp=timestamp + index,
                actor="MOC_R_HYPOTHESIS", operation=edit.operation,
                target=edit.target, source_ids=(str(edit.payload),),
                source_type=SourceType.CONTROLLER_INTERVENTION,
                rationale=f"{edit.rationale}; typed MOC_R laboratory hypothesis",
            )
        field_after = generate_field(current)
        chosen_before = select_best(field_before)
        chosen_after = select_best(field_after)
        current = replace(current,
                          selected_action=chosen_after.action_id if chosen_after else None)
        return ControllerResult(
            controller="MOC_R_HYPOTHESIS", before=state, after=current,
            field_before=field_before, field_after=field_after,
            delta=compare_fields(field_before, field_after),
            action_before=chosen_before.action_id if chosen_before else None,
            action_after=chosen_after.action_id if chosen_after else None,
            structure_changed=state.structure_digest() != current.structure_digest(),
        )


__all__ = [
    "MOCComponent", "EditTarget", "StructuralEdit", "structural_diff",
    "MOCReorganization",
]
