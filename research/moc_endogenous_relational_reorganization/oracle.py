"""Oracle estructural ciego para reorganizacion relacional endogena.

Autoría separada: ORACLE_AUTHOR. Este módulo no importa controladores, políticas,
benchmarks ni implementaciones MOC. Evalúa exclusivamente before/after, campos,
traza y, opcionalmente, expectativas congeladas de un fixture.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from hashlib import sha256
import json
from typing import Iterable, Mapping

try:
    from .state_model import ProvenanceEvent, RelationalState, assert_well_formed
    from .possibility_field import (
        FieldDelta,
        PossibilityField,
        compare_fields,
        generate_field,
    )
    from .fixtures import ExpectedDelta, FixtureCase
except ImportError:  # pragma: no cover - ejecución local desde esta carpeta
    from state_model import ProvenanceEvent, RelationalState, assert_well_formed  # type: ignore
    from possibility_field import (  # type: ignore
        FieldDelta,
        PossibilityField,
        compare_fields,
        generate_field,
    )
    from fixtures import ExpectedDelta, FixtureCase  # type: ignore


ORACLE_AUTHOR = "FASE2_INDEPENDENT_ORACLE_AGENT"
ORACLE_SCHEMA = "MOC-ERR-STRUCTURAL-ORACLE-001/v1"


class ChangeStatus(str, Enum):
    CHANGED = "CHANGED"
    UNCHANGED = "UNCHANGED"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class Agreement(str, Enum):
    AGREE = "AGREE"
    DISAGREE = "DISAGREE"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@dataclass(frozen=True)
class StructuralChanges:
    distinctions: ChangeStatus
    relations: ChangeStatus
    constraints: ChangeStatus
    generator: ChangeStatus
    distinction_added: tuple[str, ...]
    distinction_removed: tuple[str, ...]
    distinction_value_changed: tuple[str, ...]
    relation_added: tuple[tuple[str, str, str, float], ...]
    relation_removed: tuple[tuple[str, str, str, float], ...]
    constraint_added: tuple[str, ...]
    constraint_removed: tuple[str, ...]
    generator_fields_changed: tuple[str, ...]


@dataclass(frozen=True)
class PossibilityChanges:
    added: tuple[str, ...]
    removed: tuple[str, ...]
    retained: tuple[str, ...]
    PE: int
    PR: int
    PC: int
    transitability_overlap: float
    candidate_score_changed: tuple[str, ...]
    TC: ChangeStatus


@dataclass(frozen=True)
class ProvenanceAssessment:
    available: bool
    ordered: bool
    event_ids_unique: bool
    after_digest_matches: bool
    chain_digest_consistent: bool
    target_matches_fixture: Agreement
    fixture_source_present: Agreement
    actor_separation_preserved: bool
    issues: tuple[str, ...]


@dataclass(frozen=True)
class FixtureAgreement:
    relation_changed: Agreement
    action_changed: Agreement
    field_expansion: Agreement
    field_contraction: Agreement
    transitability_relation: Agreement
    reorganization_expected: Agreement
    distinction_expectation_observable_from_D: Agreement
    constraint_expectation_observable_from_K: Agreement
    notes: tuple[str, ...]


@dataclass(frozen=True)
class OracleResult:
    schema: str
    oracle_author: str
    rubric_sha256: str
    case_id: str | None
    before_structure_digest: str
    after_structure_digest: str
    structural: StructuralChanges
    possibilities: PossibilityChanges
    selected_action_before: str | None
    selected_action_after: str | None
    action_changed: bool
    action_independent_of_structure: bool
    structure_independent_of_action: bool
    provenance: ProvenanceAssessment
    fixture_agreement: FixtureAgreement | None
    reorganization_observed: bool
    reorganization_with_action_unchanged: bool
    action_change_without_reorganization: bool
    determination_basis: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        """Representación JSON-compatible, estable y sin objetos de política."""
        return _jsonable(asdict(self))


_RUBRIC = {
    "version": ORACLE_SCHEMA,
    "blind_to": ["controller_identity", "MOC_vocabulary", "policy_name"],
    "reorganization_rule": (
        "observed D, R or generator edit, or nontrivial K edit; "
        "valid provenance required; action change neither necessary nor sufficient"
    ),
    "constraint_relabel_rule": (
        "a pure one-for-one K replacement is structural but not sufficient by itself "
        "when the fixture declares a relabel negative control"
    ),
    "unknown_rule": "fixture semantic labels never become observations automatically",
    "field_rule": "PE/PR/PC are set deltas; TC includes scores for retained actions",
}
RUBRIC_SHA256 = sha256(
    json.dumps(_RUBRIC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()


def _jsonable(value: object) -> object:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    return value


def rubric_digest() -> str:
    return RUBRIC_SHA256


def verify_rubric(expected_digest: str = RUBRIC_SHA256) -> None:
    actual = sha256(
        json.dumps(_RUBRIC, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    if actual != expected_digest:
        raise AssertionError(f"oracle rubric digest mismatch: {actual} != {expected_digest}")
    if ORACLE_AUTHOR == "FASE2_INDEPENDENT_FIXTURE_AGENT":
        raise AssertionError("oracle and fixture authors must remain separate")


def _relation_key(relation: object) -> tuple[str, str, str, float]:
    return (relation.source, relation.target, relation.kind, relation.weight)  # type: ignore[attr-defined]


def _structural_changes(before: RelationalState, after: RelationalState) -> StructuralChanges:
    before_d, after_d = dict(before.D), dict(after.D)
    before_keys, after_keys = set(before_d), set(after_d)
    value_changed = sorted(k for k in before_keys & after_keys if before_d[k] != after_d[k])
    d_changed = before_d != after_d

    before_r = {_relation_key(r) for r in before.R}
    after_r = {_relation_key(r) for r in after.R}
    relation_added = tuple(sorted(after_r - before_r))
    relation_removed = tuple(sorted(before_r - after_r))

    constraint_added = tuple(sorted(after.K - before.K))
    constraint_removed = tuple(sorted(before.K - after.K))

    generator_fields = tuple(
        name for name in ("name", "operations", "max_candidates", "revision")
        if getattr(before.generator, name) != getattr(after.generator, name)
    )
    return StructuralChanges(
        ChangeStatus.CHANGED if d_changed else ChangeStatus.UNCHANGED,
        ChangeStatus.CHANGED if before_r != after_r else ChangeStatus.UNCHANGED,
        ChangeStatus.CHANGED if before.K != after.K else ChangeStatus.UNCHANGED,
        ChangeStatus.CHANGED if generator_fields else ChangeStatus.UNCHANGED,
        tuple(sorted(after_keys - before_keys)),
        tuple(sorted(before_keys - after_keys)),
        tuple(value_changed), relation_added, relation_removed,
        constraint_added, constraint_removed, generator_fields,
    )


def _possibility_changes(before: PossibilityField, after: PossibilityField) -> PossibilityChanges:
    delta: FieldDelta = compare_fields(before, after)
    bs = {c.action_id: c.score for c in before.candidates}
    aps = {c.action_id: c.score for c in after.candidates}
    score_changed = tuple(sorted(a for a in delta.retained if bs[a] != aps[a]))
    tc = ChangeStatus.CHANGED if (delta.added or delta.removed or score_changed) else ChangeStatus.UNCHANGED
    return PossibilityChanges(
        tuple(sorted(delta.added)), tuple(sorted(delta.removed)),
        tuple(sorted(delta.retained)), delta.expansion, delta.contraction,
        len(delta.added | delta.removed), delta.transitability,
        score_changed, tc,
    )


def _provenance(
    before: RelationalState,
    after: RelationalState,
    events: tuple[ProvenanceEvent, ...],
    case: FixtureCase | None,
) -> ProvenanceAssessment:
    issues: list[str] = []
    available = bool(events)
    ordered = all(a.timestamp <= b.timestamp for a, b in zip(events, events[1:]))
    unique = len({e.event_id for e in events}) == len(events)
    after_match = bool(events) and events[-1].after_digest == after.structure_digest()
    chain_ok = True
    for left, right in zip(events, events[1:]):
        if right.before_digest not in {left.after_digest, "DECLARED_IN_CASE"}:
            chain_ok = False
    if not available: issues.append("NO_PROVENANCE_EVENTS")
    if not ordered: issues.append("NON_MONOTONIC_TIMESTAMPS")
    if not unique: issues.append("DUPLICATE_EVENT_ID")
    if not after_match: issues.append("FINAL_AFTER_DIGEST_MISMATCH")
    if not chain_ok: issues.append("DIGEST_CHAIN_BREAK")

    if case is None:
        target_match = source_present = Agreement.NOT_APPLICABLE
    else:
        target_match = Agreement.AGREE if events and events[-1].target == case.case_id else Agreement.DISAGREE
        source_present = Agreement.AGREE if any(case.source in e.source_ids for e in events) else Agreement.DISAGREE
        if target_match is Agreement.DISAGREE: issues.append("FIXTURE_TARGET_MISMATCH")
        if source_present is Agreement.DISAGREE: issues.append("FIXTURE_SOURCE_MISSING")
    actors = {e.actor for e in events}
    separated = ORACLE_AUTHOR not in actors
    if not separated: issues.append("ORACLE_APPEARS_AS_TRACE_ACTOR")
    return ProvenanceAssessment(
        available, ordered, unique, after_match, chain_ok,
        target_match, source_present, separated, tuple(issues),
    )


def _agree(actual: object, expected: object) -> Agreement:
    return Agreement.AGREE if actual == expected else Agreement.DISAGREE


def _fixture_agreement(
    case: FixtureCase,
    structural: StructuralChanges,
    possibilities: PossibilityChanges,
    action_changed: bool,
    observed: bool,
) -> FixtureAgreement:
    expected: ExpectedDelta = case.expected
    relation_changed = structural.relations is ChangeStatus.CHANGED
    if possibilities.TC is ChangeStatus.UNCHANGED:
        actual_t = "SAME"
    elif possibilities.PE or possibilities.PR:
        actual_t = "DECREASED"  # fixture metric is overlap/Jaccard-like, not directional access
    else:
        actual_t = "INCREASED" if possibilities.candidate_score_changed else "SAME"

    notes: list[str] = []
    # D in the neutral interface is node/value state, not a semantic distinction ledger.
    if expected.distinction_change == "NONE":
        d_observable = _agree(structural.distinctions, ChangeStatus.UNCHANGED)
    elif structural.distinctions is ChangeStatus.CHANGED:
        d_observable = Agreement.AGREE
    else:
        d_observable = Agreement.UNKNOWN
        notes.append("EXPECTED_DISTINCTION_CHANGE_NOT_OBSERVABLE_IN_NEUTRAL_D")

    # K diffs reveal membership change, but not semantic classes such as FALSE_REMOVED vs REAL_LIMIT.
    if expected.constraint_change == "NONE":
        k_observable = _agree(structural.constraints, ChangeStatus.UNCHANGED)
    elif structural.constraints is ChangeStatus.CHANGED:
        k_observable = Agreement.AGREE
        notes.append("CONSTRAINT_MEMBERSHIP_CHANGED; SEMANTIC_SUBTYPE_COMES_FROM_FIXTURE")
    else:
        k_observable = Agreement.DISAGREE

    return FixtureAgreement(
        _agree(relation_changed, expected.relation_changed),
        _agree(action_changed, expected.action_changed),
        _agree(possibilities.PE, expected.field_expansion),
        _agree(possibilities.PR, expected.field_contraction),
        _agree(actual_t, expected.transitability_relation),
        _agree(observed, expected.reorganization_expected),
        d_observable, k_observable, tuple(notes),
    )


def evaluate(
    before: RelationalState,
    after: RelationalState,
    *,
    before_field: PossibilityField | None = None,
    after_field: PossibilityField | None = None,
    trace: Iterable[ProvenanceEvent] | None = None,
    fixture: FixtureCase | None = None,
) -> OracleResult:
    """Evalúa una transición sin conocer el controlador que la produjo."""
    verify_rubric()
    assert_well_formed(before)
    assert_well_formed(after)
    bf = before_field or generate_field(before)
    af = after_field or generate_field(after)
    if bf.state_digest != before.structure_digest():
        raise ValueError("before_field does not correspond to before state")
    if af.state_digest != after.structure_digest():
        raise ValueError("after_field does not correspond to after state")

    structural = _structural_changes(before, after)
    possibilities = _possibility_changes(bf, af)
    events = tuple(trace) if trace is not None else tuple(after.provenance)
    provenance = _provenance(before, after, events, fixture)
    action_changed = before.selected_action != after.selected_action

    substantive = any(status is ChangeStatus.CHANGED for status in (
        structural.distinctions, structural.relations, structural.generator
    ))
    constraint_only = (
        structural.constraints is ChangeStatus.CHANGED and not substantive
    )
    pure_relabel_control = bool(
        fixture and fixture.expected.constraint_change == "RELABELED"
        and not fixture.expected.reorganization_expected
    )
    trace_valid = (
        provenance.available and provenance.ordered and provenance.event_ids_unique
        and provenance.after_digest_matches and provenance.chain_digest_consistent
        and provenance.actor_separation_preserved
    )
    observed = bool((substantive or constraint_only) and not pure_relabel_control and trace_valid)

    basis = [
        "ACTION_CHANGE_IS_NEITHER_NECESSARY_NOR_SUFFICIENT",
        "STRUCTURE_ASSESSED_WITHOUT_CONTROLLER_IDENTITY",
        "PROVENANCE_REQUIRED_FOR_CAUSAL_REORGANIZATION_LABEL",
    ]
    if constraint_only: basis.append("CONSTRAINT_ONLY_EDIT_OBSERVED")
    if pure_relabel_control: basis.append("PURE_RELABEL_NEGATIVE_CONTROL")
    if not trace_valid: basis.append("TRACE_INVALID_OR_INCOMPLETE")

    agreement = None if fixture is None else _fixture_agreement(
        fixture, structural, possibilities, action_changed, observed
    )
    return OracleResult(
        ORACLE_SCHEMA, ORACLE_AUTHOR, RUBRIC_SHA256,
        fixture.case_id if fixture else None,
        before.structure_digest(), after.structure_digest(),
        structural, possibilities,
        before.selected_action, after.selected_action, action_changed,
        action_changed and not observed,
        observed and not action_changed,
        provenance, agreement, observed,
        observed and not action_changed,
        action_changed and not observed,
        tuple(basis),
    )


def evaluate_fixture(case: FixtureCase) -> OracleResult:
    """Atajo determinista que no inspecciona ninguna política/controlador."""
    return evaluate(case.before, case.after, fixture=case)


verify_rubric()

__all__ = [
    "ORACLE_AUTHOR", "ORACLE_SCHEMA", "RUBRIC_SHA256", "ChangeStatus",
    "Agreement", "StructuralChanges", "PossibilityChanges",
    "ProvenanceAssessment", "FixtureAgreement", "OracleResult",
    "rubric_digest", "verify_rubric", "evaluate", "evaluate_fixture",
]
