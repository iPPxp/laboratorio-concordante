"""Benchmark congelado B4/B5/B6/MOC_R para los fixtures independientes."""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import json

try:
    from .fixtures import CASES, FixtureCase, TRANSFORMATION_HOLDOUT
    from .generic_controllers import (
        B4RelationalSelector, B5GenerativeReplanner, B6StructureEditor,
        ControllerResult,
    )
    from .isomorphism import compare_traces
    from .moc_reorganization import MOCReorganization, StructuralEdit, structural_diff
    from .oracle import Agreement, OracleResult, evaluate
    from .possibility_field import compare_fields, generate_field, select_best
    from .state_model import RelationalState, SourceType, record_edit
except ImportError:  # pragma: no cover
    from fixtures import CASES, FixtureCase, TRANSFORMATION_HOLDOUT
    from generic_controllers import (
        B4RelationalSelector, B5GenerativeReplanner, B6StructureEditor,
        ControllerResult,
    )
    from isomorphism import compare_traces
    from moc_reorganization import MOCReorganization, StructuralEdit, structural_diff
    from oracle import Agreement, OracleResult, evaluate
    from possibility_field import compare_fields, generate_field, select_best
    from state_model import RelationalState, SourceType, record_edit


SYSTEMS = ("B4", "B5", "B6", "MOC_R")


@dataclass(frozen=True)
class CaseScore:
    case_id: str
    partition: str
    transform: str
    system: str
    target_structure_match: bool
    target_field_match: bool
    action_match: bool
    reorganization_match: bool
    trace_valid: bool
    structural_trace_fidelity: float
    causal_attribution: bool
    edit_count: int


@dataclass(frozen=True)
class BenchmarkSummary:
    cases: int
    development_cases: int
    holdout_cases: int
    scores: tuple[CaseScore, ...]
    aggregate: dict[str, dict[str, float]]
    generic_isomorphism_rate: float
    generic_isomorphism_holdout_rate: float
    isomorphism_witnesses: tuple[str, ...]

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2, sort_keys=True)


def _same_structure(left: RelationalState, right: RelationalState) -> bool:
    return (
        dict(left.D) == dict(right.D) and set(left.R) == set(right.R)
        and left.K == right.K and left.generator == right.generator
    )


def _with_requested_action(result: ControllerResult, case: FixtureCase) -> ControllerResult:
    """Separa elección de la edición; la misma acción solicitada se da a todos."""
    requested = case.after.selected_action
    if requested is not None and requested not in result.field_after.action_ids:
        requested = select_best(result.field_after).action_id if result.field_after.candidates else None
    after = replace(result.after, selected_action=requested)
    return replace(result, after=after, action_after=requested,
                   action_before=case.before.selected_action)


def _commit(result: ControllerResult, case: FixtureCase) -> ControllerResult:
    """Añade envelope común de caso para que el oracle audite source/target."""
    committed = record_edit(
        result.after, result.after,
        event_id=f"{case.case_id}:{result.controller}:COMMIT",
        timestamp=1000, actor=f"{result.controller}:EVALUATOR_ADAPTER",
        operation="TRANSITION_COMMIT", target=case.case_id,
        source_ids=(case.source, case.case_id), source_type=SourceType.TEST_CONTROL,
        rationale="Common evaluator envelope; no structural mutation.",
        reversible=True,
    )
    return replace(result, after=committed)


def _identity_result(name: str, state: RelationalState) -> ControllerResult:
    field = generate_field(state)
    selected = select_best(field)
    action = selected.action_id if selected else None
    after = replace(state, selected_action=action)
    return ControllerResult(name, state, after, field, field,
                            compare_fields(field, field), action, action, False)


def _run_b6(case: FixtureCase, edits: tuple[StructuralEdit, ...]) -> ControllerResult:
    if not edits:
        return _identity_result("B6_STRUCTURE", case.before)
    editor = B6StructureEditor()
    current = case.before
    first_field = generate_field(current)
    for index, edit in enumerate(edits):
        step = editor.run(
            current, target=edit.target, operation=edit.operation,
            payload=edit.payload, event_id=f"{case.case_id}:B6:{index}",
            timestamp=index + 1, rationale=edit.rationale,
        )
        current = step.after
    final_field = generate_field(current)
    before_action = select_best(first_field)
    after_action = select_best(final_field)
    return ControllerResult(
        "B6_STRUCTURE", case.before, current, first_field, final_field,
        compare_fields(first_field, final_field),
        before_action.action_id if before_action else None,
        after_action.action_id if after_action else None,
        case.before.structure_digest() != current.structure_digest(),
    )


def run_case(case: FixtureCase) -> dict[str, ControllerResult]:
    edits = structural_diff(case.before, case.after)
    raw = {
        "B4": B4RelationalSelector().run(case.before),
        "B5": B5GenerativeReplanner().run(
            case.before, add_operation="combine_pair",
            event_id=f"{case.case_id}:B5:0", timestamp=1,
            rationale="matched-budget generic search expansion",
        ),
        "B6": _run_b6(case, edits),
        "MOC_R": MOCReorganization().run(
            case.before, edits=edits, event_prefix=f"{case.case_id}:MOCR",
            timestamp=1,
        ),
    }
    return {name: _commit(_with_requested_action(result, case), case)
            for name, result in raw.items()}


def _oracle_for(result: ControllerResult, case: FixtureCase) -> OracleResult:
    trace = result.after.provenance[len(case.before.provenance):]
    return evaluate(
        case.before, result.after,
        before_field=result.field_before, after_field=result.field_after,
        trace=trace, fixture=case,
    )


def _score(result: ControllerResult, case: FixtureCase,
           oracle: OracleResult, system: str) -> CaseScore:
    target_field = generate_field(case.after)
    target_structure = _same_structure(result.after, case.after)
    field_match = result.field_after.action_ids == target_field.action_ids
    action_match = result.after.selected_action == case.after.selected_action
    expected_reorg = case.expected.reorganization_expected
    reorg_match = oracle.reorganization_observed == expected_reorg
    trace_valid = not oracle.provenance.issues
    components = (
        dict(result.after.D) == dict(case.after.D),
        set(result.after.R) == set(case.after.R),
        result.after.K == case.after.K,
        result.after.generator == case.after.generator,
        field_match,
    )
    trace_fidelity = sum(components) / len(components)
    causal = trace_valid and target_structure and (
        oracle.fixture_agreement is not None
        and oracle.fixture_agreement.reorganization_expected is Agreement.AGREE
    )
    edit_count = len(result.after.provenance) - len(case.before.provenance) - 1
    return CaseScore(
        case.case_id, case.partition, case.transform, system,
        target_structure, field_match, action_match, reorg_match, trace_valid,
        trace_fidelity, causal, max(0, edit_count),
    )


def run_benchmark() -> BenchmarkSummary:
    scores: list[CaseScore] = []
    exact_flags: list[bool] = []
    holdout_flags: list[bool] = []
    witnesses: list[str] = []
    for case in CASES:
        results = run_case(case)
        for system in SYSTEMS:
            scores.append(_score(results[system], case,
                                 _oracle_for(results[system], case), system))
        iso = compare_traces(results["B6"], results["MOC_R"])
        exact_flags.append(iso.exact)
        if case.partition == TRANSFORMATION_HOLDOUT:
            holdout_flags.append(iso.exact)
        if not iso.exact:
            witnesses.append(f"{case.case_id}:{iso.first_witness}")

    aggregate: dict[str, dict[str, float]] = {}
    for system in SYSTEMS:
        rows = [row for row in scores if row.system == system]
        holdout = [row for row in rows if row.partition == TRANSFORMATION_HOLDOUT]
        aggregate[system] = {
            "target_structure_rate": sum(r.target_structure_match for r in rows) / len(rows),
            "target_field_rate": sum(r.target_field_match for r in rows) / len(rows),
            "action_rate": sum(r.action_match for r in rows) / len(rows),
            "reorganization_classification_rate": sum(r.reorganization_match for r in rows) / len(rows),
            "trace_valid_rate": sum(r.trace_valid for r in rows) / len(rows),
            "trace_fidelity_mean": sum(r.structural_trace_fidelity for r in rows) / len(rows),
            "causal_attribution_rate": sum(r.causal_attribution for r in rows) / len(rows),
            "holdout_structure_rate": sum(r.target_structure_match for r in holdout) / len(holdout),
            "holdout_trace_fidelity_mean": sum(r.structural_trace_fidelity for r in holdout) / len(holdout),
        }
    return BenchmarkSummary(
        len(CASES), sum(c.partition != TRANSFORMATION_HOLDOUT for c in CASES),
        sum(c.partition == TRANSFORMATION_HOLDOUT for c in CASES), tuple(scores),
        aggregate, sum(exact_flags) / len(exact_flags),
        sum(holdout_flags) / len(holdout_flags), tuple(witnesses),
    )


if __name__ == "__main__":
    print(run_benchmark().to_json())
