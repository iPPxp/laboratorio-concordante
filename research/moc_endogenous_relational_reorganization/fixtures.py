"""Fixtures congelados para reorganizacion relacional endogena.

Este modulo contiene datos y expectativas; no implementa politicas, oraculos ni
controladores. Los casos son sinteticos, no clinicos y no constituyen semantica
MOC canonica. La particion transformation-holdout no debe usarse durante el
desarrollo o ajuste de transformaciones.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from types import MappingProxyType
from typing import Final, Mapping

try:  # Admite ejecucion como paquete o desde esta carpeta.
    from .state_model import (
        GeneratorSpec,
        ProvenanceEvent,
        Relation,
        RelationalState,
        SourceType,
        assert_well_formed,
    )
    from .possibility_field import compare_fields, generate_field
except ImportError:  # pragma: no cover - ruta de ejecucion local
    from state_model import (  # type: ignore
        GeneratorSpec,
        ProvenanceEvent,
        Relation,
        RelationalState,
        SourceType,
        assert_well_formed,
    )
    from possibility_field import compare_fields, generate_field  # type: ignore


FIXTURE_SCHEMA: Final[str] = "MOC-ERR-FIXTURES-001/v1"
FIXTURE_AUTHOR: Final[str] = "FASE2_INDEPENDENT_FIXTURE_AGENT"
FIXTURE_SOURCE: Final[str] = "USER_AUTHORIZED_SYNTHETIC_RESEARCH_FIXTURES"
DEVELOPMENT: Final[str] = "development"
TRANSFORMATION_HOLDOUT: Final[str] = "transformation-holdout"

P_REFRAME: Final[str] = "P_REFRAME"
S_CONSTRAINT_DISCOVERY: Final[str] = "S_CONSTRAINT_DISCOVERY"
V_CLARIFICATION: Final[str] = "V_CLARIFICATION"
ACT_MODE_REORGANIZATION: Final[str] = "ACT_MODE_REORGANIZATION"
RELATION_REORGANIZATION: Final[str] = "RELATION_REORGANIZATION"
DISTINCTION_REFINEMENT: Final[str] = "DISTINCTION_REFINEMENT"
CONSTRAINT_RELABELING: Final[str] = "CONSTRAINT_RELABELING"


@dataclass(frozen=True)
class ExpectedDelta:
    relation_changed: bool
    action_changed: bool
    distinction_change: str  # NONE | NEW | MERGED | REFINED
    constraint_change: str  # NONE | DISCOVERED | FALSE_REMOVED | REAL_LIMIT | RELABELED
    field_expansion: int
    field_contraction: int
    transitability_relation: str  # SAME | INCREASED | DECREASED
    reorganization_expected: bool


@dataclass(frozen=True)
class FixtureCase:
    case_id: str
    partition: str
    transform: str
    title: str
    coverage: frozenset[str]
    before: RelationalState
    after: RelationalState
    expected: ExpectedDelta
    author: str = FIXTURE_AUTHOR
    source: str = FIXTURE_SOURCE
    source_type: str = "SYNTHETIC_TEST_CONTROL"
    epistemic_status: str = "HYPOTHESIZED_TEST_FIXTURE"


_GENERATOR = GeneratorSpec(
    name="fixture_generic_field",
    operations=("select_node", "traverse_relation", "hold"),
    max_candidates=64,
    revision=1,
)


def _state(
    case_id: str,
    phase: str,
    values: tuple[tuple[str, float], ...],
    relations: tuple[tuple[str, str, str, float], ...],
    constraints: tuple[str, ...],
    action: str | None,
) -> RelationalState:
    state = RelationalState(
        D=MappingProxyType(dict(values)),
        R=tuple(Relation(*relation) for relation in relations),
        K=frozenset(constraints),
        generator=_GENERATOR,
        selected_action=action,
    )
    assert_well_formed(state)
    event = ProvenanceEvent(
        event_id=f"{case_id}:{phase}",
        timestamp=0 if phase == "before" else 1,
        actor=FIXTURE_AUTHOR,
        operation="FIXTURE_DECLARATION" if phase == "before" else "SYNTHETIC_TRANSFORM",
        target=case_id,
        before_digest="GENESIS" if phase == "before" else "DECLARED_IN_CASE",
        after_digest=state.structure_digest(),
        source_ids=(FIXTURE_SOURCE, case_id),
        source_type=SourceType.TEST_CONTROL,
        rationale="Caso sintetico congelado; no observacion de persona ni claim canonico.",
        reversible=True,
    )
    return RelationalState(
        D=state.D, R=state.R, K=state.K, generator=state.generator,
        provenance=(event,), selected_action=state.selected_action,
    )


def _case(
    case_id: str,
    partition: str,
    transform: str,
    title: str,
    coverage: tuple[str, ...],
    before_values: tuple[tuple[str, float], ...],
    after_values: tuple[tuple[str, float], ...],
    before_relations: tuple[tuple[str, str, str, float], ...],
    after_relations: tuple[tuple[str, str, str, float], ...],
    before_constraints: tuple[str, ...],
    after_constraints: tuple[str, ...],
    before_action: str | None,
    after_action: str | None,
    expected: ExpectedDelta,
) -> FixtureCase:
    return FixtureCase(
        case_id, partition, transform, title, frozenset(coverage),
        _state(case_id, "before", before_values, before_relations,
               before_constraints, before_action),
        _state(case_id, "after", after_values, after_relations,
               after_constraints, after_action),
        expected,
    )


_BASE = (("P", 0.4), ("EAF", 0.5), ("ACT", 0.6), ("V", 0.7), ("S", 0.8))
_BASE_R = (
    ("P", "EAF", "R-P-EAF", 0.8),
    ("P", "ACT", "R-P-ACT", 0.7),
    ("P", "V", "R-P-V", 0.6),
    ("P", "S", "R-P-S", 0.5),
)


CASES: Final[tuple[FixtureCase, ...]] = (
    _case(
        "DEV-P-001", DEVELOPMENT, P_REFRAME,
        "Cambio P con reorganizacion de R-P y accion estable",
        ("R-P", "RELATION_ONLY", "REORGANIZATION_WITHOUT_ACTION_CHANGE", "EXPANSION"),
        _BASE, _BASE, _BASE_R,
        _BASE_R + (("S", "P", "contextualizes", 0.9),),
        (), (), "hold", "hold",
        ExpectedDelta(True, False, "NEW", "NONE", 1, 0, "DECREASED", True),
    ),
    _case(
        "DEV-P-002", DEVELOPMENT, P_REFRAME,
        "Fusion de dos distinciones P sin cambiar accion",
        ("R-P", "DISTINCTION_MERGE", "RESTRICTION"),
        _BASE, _BASE,
        _BASE_R + (("V", "P", "competes", 0.4),),
        _BASE_R,
        ("P_FRAME_A", "P_FRAME_B"), ("P_FRAME_AB",), "hold", "hold",
        ExpectedDelta(True, False, "MERGED", "NONE", 0, 1, "DECREASED", True),
    ),
    _case(
        "DEV-S-001", DEVELOPMENT, S_CONSTRAINT_DISCOVERY,
        "Descubrimiento de limite situacional real",
        ("R-S", "REAL_LIMIT", "CONTRACTION", "TRANSITABILITY"),
        _BASE, _BASE, _BASE_R,
        _BASE_R[:-1], (), ("S_REAL_LIMIT:NO_P_TO_S_TRAVERSE",), "traverse:P->S", "hold",
        ExpectedDelta(True, True, "NONE", "REAL_LIMIT", 0, 1, "DECREASED", True),
    ),
    _case(
        "DEV-S-002", DEVELOPMENT, S_CONSTRAINT_DISCOVERY,
        "Retiro de restriccion situacional falsa",
        ("R-S", "FALSE_CONSTRAINT", "EXPANSION", "TRANSITABILITY"),
        _BASE, _BASE, _BASE_R[:-1], _BASE_R,
        ("S_FALSE_LIMIT:NO_P_TO_S_TRAVERSE",), (), "hold", "hold",
        ExpectedDelta(True, False, "NONE", "FALSE_REMOVED", 1, 0, "DECREASED", True),
    ),
    _case(
        "DEV-V-001", DEVELOPMENT, V_CLARIFICATION,
        "Clarificacion V cambia relacion y conserva modo de accion",
        ("R-V", "RELATION_ONLY", "REORGANIZATION_WITHOUT_ACTION_CHANGE"),
        _BASE, _BASE,
        _BASE_R, _BASE_R[:-2] + (("P", "V", "clarified_direction", 0.95),) + _BASE_R[-1:],
        (), (), "hold", "hold",
        ExpectedDelta(True, False, "REFINED", "NONE", 0, 0, "INCREASED", True),
    ),
    _case(
        "DEV-EAF-001", DEVELOPMENT, P_REFRAME,
        "Cambio exclusivamente relacional R-EAF",
        ("R-EAF", "RELATION_ONLY", "REORGANIZATION_WITHOUT_ACTION_CHANGE"),
        _BASE, _BASE, _BASE_R,
        (("P", "EAF", "reappraised", 0.85),) + _BASE_R[1:],
        (), (), "hold", "hold",
        ExpectedDelta(True, False, "REFINED", "NONE", 0, 0, "INCREASED", True),
    ),
    _case(
        "HOLD-ACT-001", TRANSFORMATION_HOLDOUT, ACT_MODE_REORGANIZATION,
        "Cambio de accion sin reorganizacion relacional",
        ("R-ACT", "ACTION_CHANGE_WITHOUT_REORGANIZATION", "NEGATIVE_CONTROL"),
        _BASE, _BASE, _BASE_R, _BASE_R, (), (), "hold", "select:ACT",
        ExpectedDelta(False, True, "NONE", "NONE", 0, 0, "SAME", False),
    ),
    _case(
        "HOLD-ACT-002", TRANSFORMATION_HOLDOUT, ACT_MODE_REORGANIZATION,
        "Reorganizacion R-ACT sin cambio de accion seleccionada",
        ("R-ACT", "RELATION_ONLY", "REORGANIZATION_WITHOUT_ACTION_CHANGE"),
        _BASE, _BASE, _BASE_R,
        _BASE_R[:1] + (("P", "ACT", "mode_reorganized", 0.9),) + _BASE_R[2:],
        (), (), "hold", "hold",
        ExpectedDelta(True, False, "REFINED", "NONE", 0, 0, "INCREASED", True),
    ),
    _case(
        "HOLD-REL-001", TRANSFORMATION_HOLDOUT, RELATION_REORGANIZATION,
        "Expansion relacional cruzada EAF-V",
        ("R-EAF", "R-V", "EXPANSION", "TRANSITABILITY"),
        _BASE, _BASE, _BASE_R,
        _BASE_R + (("EAF", "V", "informs", 0.75),),
        (), (), "hold", "hold",
        ExpectedDelta(True, False, "NEW", "NONE", 1, 0, "DECREASED", True),
    ),
    _case(
        "HOLD-REL-002", TRANSFORMATION_HOLDOUT, RELATION_REORGANIZATION,
        "Restriccion relacional elimina transitabilidad S-ACT",
        ("R-S", "R-ACT", "CONTRACTION", "REAL_LIMIT", "TRANSITABILITY"),
        _BASE, _BASE,
        _BASE_R + (("S", "ACT", "permits", 0.65),), _BASE_R,
        (), ("S_ACT_REAL_LIMIT",), "traverse:S->ACT", "hold",
        ExpectedDelta(True, True, "NONE", "REAL_LIMIT", 0, 1, "DECREASED", True),
    ),
    _case(
        "HOLD-DIST-001", TRANSFORMATION_HOLDOUT, DISTINCTION_REFINEMENT,
        "Nueva distincion EAF-S sin cambio marginal",
        ("R-EAF", "R-S", "DISTINCTION_NEW", "EXPANSION"),
        _BASE, _BASE, _BASE_R,
        _BASE_R + (("EAF", "S", "situated_affect", 0.7),),
        (), (), "hold", "hold",
        ExpectedDelta(True, False, "NEW", "NONE", 1, 0, "DECREASED", True),
    ),
    _case(
        "HOLD-CON-001", TRANSFORMATION_HOLDOUT, CONSTRAINT_RELABELING,
        "Reetiquetado de restriccion sin cambio estructural real",
        ("R-V", "CONSTRAINT_RELABEL", "NEGATIVE_CONTROL"),
        _BASE, _BASE, _BASE_R, _BASE_R,
        ("V_LIMIT:legacy_label",), ("V_LIMIT:canonical_neutral_label",), "hold", "hold",
        ExpectedDelta(False, False, "NONE", "RELABELED", 0, 0, "SAME", False),
    ),
)


DEVELOPMENT_CASES: Final[tuple[FixtureCase, ...]] = tuple(
    case for case in CASES if case.partition == DEVELOPMENT
)
TRANSFORMATION_HOLDOUT_CASES: Final[tuple[FixtureCase, ...]] = tuple(
    case for case in CASES if case.partition == TRANSFORMATION_HOLDOUT
)
CASE_BY_ID: Final[Mapping[str, FixtureCase]] = MappingProxyType(
    {case.case_id: case for case in CASES}
)


def _canonical_state(state: RelationalState) -> dict[str, object]:
    return {
        "D": sorted((key, value) for key, value in state.D.items()),
        "R": sorted((r.source, r.target, r.kind, r.weight) for r in state.R),
        "K": sorted(state.K),
        "generator": {
            "name": state.generator.name,
            "operations": list(state.generator.operations),
            "max_candidates": state.generator.max_candidates,
            "revision": state.generator.revision,
        },
        "selected_action": state.selected_action,
        "provenance": [
            {
                "event_id": event.event_id,
                "timestamp": event.timestamp,
                "actor": event.actor,
                "operation": event.operation,
                "target": event.target,
                "source_ids": list(event.source_ids),
                "source_type": event.source_type.value,
                "rationale": event.rationale,
                "reversible": event.reversible,
            }
            for event in state.provenance
        ],
    }


def canonical_payload() -> str:
    payload = {
        "schema": FIXTURE_SCHEMA,
        "author": FIXTURE_AUTHOR,
        "source": FIXTURE_SOURCE,
        "cases": [
            {
                "case_id": case.case_id,
                "partition": case.partition,
                "transform": case.transform,
                "title": case.title,
                "coverage": sorted(case.coverage),
                "before": _canonical_state(case.before),
                "after": _canonical_state(case.after),
                "expected": case.expected.__dict__,
                "epistemic_status": case.epistemic_status,
            }
            for case in CASES
        ],
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


FIXTURE_SET_SHA256: Final[str] = sha256(canonical_payload().encode("utf-8")).hexdigest()


def verify_fixture_integrity(expected_digest: str = FIXTURE_SET_SHA256) -> None:
    """Falla si el conjunto congelado no coincide con el digest esperado."""
    actual = sha256(canonical_payload().encode("utf-8")).hexdigest()
    if actual != expected_digest:
        raise AssertionError(f"fixture digest mismatch: expected={expected_digest} actual={actual}")
    if len(CASE_BY_ID) != len(CASES):
        raise AssertionError("fixture case_id values must be unique")
    for case in CASES:
        assert_well_formed(case.before)
        assert_well_formed(case.after)
        delta = compare_fields(generate_field(case.before), generate_field(case.after))
        if delta.expansion != case.expected.field_expansion:
            raise AssertionError(f"{case.case_id}: unexpected field expansion")
        if delta.contraction != case.expected.field_contraction:
            raise AssertionError(f"{case.case_id}: unexpected field contraction")


verify_fixture_integrity()


__all__ = [
    "CASES", "CASE_BY_ID", "DEVELOPMENT_CASES", "TRANSFORMATION_HOLDOUT_CASES",
    "FixtureCase", "ExpectedDelta", "FIXTURE_SET_SHA256", "canonical_payload",
    "verify_fixture_integrity", "P_REFRAME", "S_CONSTRAINT_DISCOVERY",
    "V_CLARIFICATION", "ACT_MODE_REORGANIZATION", "RELATION_REORGANIZATION",
    "DISTINCTION_REFINEMENT", "CONSTRAINT_RELABELING",
]
