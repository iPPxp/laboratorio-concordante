"""Auditor integrador F0: verifica integridad y detecta readiness ilusorio."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COMPONENTS = ("P", "EAF", "ACT", "V", "S")
ALLOWED_STATUSES = {"PRESENT", "ABSENT", "AMBIGUOUS", "UNKNOWN"}
RAW_KEYS = {"case_id", "raw_text", "time_index", "context_id", "family_id", "split"}
PROHIBITED_OUTCOME_KEYS = {"p", "eaf", "act", "v", "s", "d", "r", "k"}


@dataclass(frozen=True)
class AuditResult:
    raw_records: int
    annotation_records: int
    outcome_records: int
    effective_families: int
    family_counts_by_split: dict[str, int]
    visible_schema_exact: bool
    family_leakage: bool
    id_sets_match: bool
    raw_digest_ok: bool
    annotation_digest_ok: bool
    outcome_digest_ok: bool
    annotation_status_counts: dict[str, dict[str, int]]
    present_by_component: dict[str, int]
    cases_with_duplicated_component_evidence: int
    outcome_prohibited_key_matches: int
    independent_role_ids: bool
    external_outcome_source: bool
    intervention_unavailable_cases: int
    possibility_unknown_cases: int
    hard_integrity_ok: bool
    benchmark_ready: bool
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2, sort_keys=True)


def _read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def _digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _keys_recursive(value: object) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key).lower())
            keys |= _keys_recursive(child)
    elif isinstance(value, list):
        for child in value:
            keys |= _keys_recursive(child)
    return keys


def audit() -> AuditResult:
    raw_path = ROOT / "raw" / "model_input.jsonl"
    annotation_path = ROOT / "moc_annotations" / "annotations.jsonl"
    outcome_path = ROOT / "outcomes" / "outcomes.jsonl"
    raw = _read_jsonl(raw_path)
    annotations = _read_jsonl(annotation_path)
    outcomes = _read_jsonl(outcome_path)
    top_integrity = json.loads((ROOT / "INTEGRITY.json").read_text(encoding="utf-8"))
    annotation_integrity = json.loads(
        (ROOT / "moc_annotations" / "INTEGRITY.json").read_text(encoding="utf-8")
    )
    outcome_integrity = json.loads(
        (ROOT / "outcomes" / "INTEGRITY.json").read_text(encoding="utf-8")
    )

    visible_schema_exact = all(set(row) == RAW_KEYS for row in raw)
    raw_ids = {str(row["case_id"]) for row in raw}
    annotation_ids = {str(row["case_id"]) for row in annotations}
    outcome_ids = {str(row["case_id"]) for row in outcomes}
    id_sets_match = raw_ids == annotation_ids == outcome_ids

    family_splits: dict[str, set[str]] = defaultdict(set)
    family_counts_by_split: Counter[str] = Counter()
    for row in raw:
        family_splits[str(row["family_id"])].add(str(row["split"]))
    for family, splits in family_splits.items():
        if len(splits) == 1:
            family_counts_by_split[next(iter(splits))] += 1
    family_leakage = any(len(splits) != 1 for splits in family_splits.values())

    status_counts: dict[str, Counter[str]] = {c: Counter() for c in COMPONENTS}
    duplicated_evidence = 0
    for row in annotations:
        components = row.get("components", {})
        evidence: list[str] = []
        for component in COMPONENTS:
            record = components.get(component, {})
            status_counts[component][str(record.get("status"))] += 1
            item = str(record.get("evidence", ""))
            if item and item != "insufficient explicit evidence":
                evidence.append(item)
        if len(evidence) != len(set(evidence)):
            duplicated_evidence += 1

    prohibited_matches = sum(
        len(_keys_recursive(row) & PROHIBITED_OUTCOME_KEYS) for row in outcomes
    )
    annotation_actor = str(annotation_integrity.get("annotator_id"))
    outcome_actor = str(outcome_integrity.get("outcome_author"))
    source_actors = {
        str(row.get("provenance", {}).get("source_author")) for row in outcomes
    }
    designer_actor = next(iter(source_actors)) if len(source_actors) == 1 else "MIXED"
    independent_roles = len({annotation_actor, outcome_actor, designer_actor}) == 3
    external_outcome_source = all(
        str(row.get("provenance", {}).get("source_type")) != "SYNTHETIC"
        and str(row.get("provenance", {}).get("source_author")) != designer_actor
        for row in outcomes
    )
    intervention_unavailable = sum(not bool(row.get("intervention_available"))
                                   for row in outcomes)
    possibility_unknown = sum(row.get("possibility_change") == "UNKNOWN"
                              for row in outcomes)

    raw_digest_ok = _digest(raw_path) == str(top_integrity["raw_sha256"])
    annotation_digest_ok = (
        _digest(annotation_path) ==
        str(annotation_integrity["annotations"]["sha256"])
    )
    outcome_digest_ok = (
        _digest(outcome_path) ==
        str(outcome_integrity["sha256"]["outcomes/outcomes.jsonl"])
    )
    valid_statuses = all(
        set(counter) <= ALLOWED_STATUSES for counter in status_counts.values()
    )
    hard_integrity = all((
        visible_schema_exact, not family_leakage, id_sets_match,
        raw_digest_ok, annotation_digest_ok, outcome_digest_ok,
        valid_statuses, prohibited_matches == 0, independent_roles,
    ))

    present = {component: status_counts[component]["PRESENT"]
               for component in COMPONENTS}
    blockers: list[str] = []
    if any(count == 0 for count in present.values()):
        blockers.append("AT_LEAST_ONE_COMPONENT_HAS_ZERO_PRESENT_EXAMPLES")
    if not external_outcome_source:
        blockers.append("OUTCOME_SOURCE_IS_SYNTHETIC_DATASET_DESIGN")
    if intervention_unavailable == 0:
        blockers.append("NO_INTERVENTION_UNAVAILABLE_NEGATIVE_CONTROLS")
    if family_counts_by_split.get("test", 0) < 10:
        blockers.append("TEST_EFFECTIVE_FAMILIES_BELOW_10")
    blockers.extend((
        "SINGLE_INSTRUMENTAL_MOC_ANNOTATOR",
        "NO_INTER_RATER_RELIABILITY",
        "NO_INDEPENDENT_HUMAN_OR_NATURALISTIC_OUTCOMES",
    ))
    warnings: list[str] = []
    if duplicated_evidence:
        warnings.append("COMPONENT_EVIDENCE_REUSED_WITHIN_CASE")
    if possibility_unknown:
        warnings.append("POSSIBILITY_OUTCOME_PARTIALLY_UNKNOWN")

    benchmark_ready = hard_integrity and not blockers
    return AuditResult(
        len(raw), len(annotations), len(outcomes), len(family_splits),
        dict(sorted(family_counts_by_split.items())), visible_schema_exact,
        family_leakage, id_sets_match, raw_digest_ok, annotation_digest_ok,
        outcome_digest_ok,
        {c: dict(sorted(status_counts[c].items())) for c in COMPONENTS},
        present, duplicated_evidence, prohibited_matches, independent_roles,
        external_outcome_source, intervention_unavailable, possibility_unknown,
        hard_integrity, benchmark_ready, tuple(blockers), tuple(warnings),
    )


if __name__ == "__main__":
    print(audit().to_json())

