"""Evaluador conjuntivo del Gate 0.1; no entrena ni modifica el corpus."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COMPONENTS = ("P", "EAF", "ACT", "V", "S")
SPLITS = ("train", "validation", "test")
COVERAGE_MIN = {
    "train": {"PRESENT": 8, "ABSENT": 6, "AMB_OR_UNK": 4},
    "validation": {"PRESENT": 2, "ABSENT": 2, "AMB_OR_UNK": 2},
    "test": {"PRESENT": 3, "ABSENT": 3, "AMB_OR_UNK": 2},
}


@dataclass(frozen=True)
class GateAudit:
    gate: dict[str, str]
    passed: int
    failed: int
    training_readiness: str
    raw_counts: dict[str, int]
    core_pair_cells: dict[str, list[str]]
    annotation_status_by_split: dict[str, dict[str, dict[str, dict[str, int]]]]
    adjudicated_status_counts: dict[str, dict[str, int]]
    raw_agreement: dict[str, float]
    binary_agreement: dict[str, float]
    unknown_rates: dict[str, dict[str, float]]
    absent_change_reason_count: dict[str, int]
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2, sort_keys=True)


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _coverage(rows: list[dict], raw_by_case: dict[str, dict]) -> dict:
    result: dict = {split: {c: Counter() for c in COMPONENTS} for split in SPLITS}
    for row in rows:
        split = str(raw_by_case[row["case_id"]]["split"])
        for component in COMPONENTS:
            result[split][component][row["components"][component]["status"]] += 1
    return {
        split: {c: dict(sorted(result[split][c].items())) for c in COMPONENTS}
        for split in SPLITS
    }


def _coverage_pass(coverage: dict) -> bool:
    for split in SPLITS:
        minimum = COVERAGE_MIN[split]
        for component in COMPONENTS:
            counts = coverage[split][component]
            if counts.get("PRESENT", 0) < minimum["PRESENT"]:
                return False
            if counts.get("ABSENT", 0) < minimum["ABSENT"]:
                return False
            if counts.get("AMBIGUOUS", 0) + counts.get("UNKNOWN", 0) < minimum["AMB_OR_UNK"]:
                return False
    return True


def audit_gate() -> GateAudit:
    world = _read_jsonl(ROOT / "world" / "world_states.jsonl")
    raw = _read_jsonl(ROOT / "raw" / "model_input.jsonl")
    outcomes = _read_jsonl(ROOT / "outcomes" / "outcomes.jsonl")
    ann_a = _read_jsonl(ROOT / "annotations_a" / "annotations.jsonl")
    ann_b = _read_jsonl(ROOT / "annotations_b" / "annotations.jsonl")
    adjudicated = _read_jsonl(ROOT / "adjudication" / "adjudicated.jsonl")
    confusion = json.loads(
        (ROOT / "adjudication" / "CONFUSION_MATRICES.json").read_text(encoding="utf-8")
    )
    permutation = json.loads(
        (ROOT / "LABEL_PERMUTATION_MANIFEST.json").read_text(encoding="utf-8")
    )
    raw_by_case = {row["case_id"]: row for row in raw}

    split_counts = Counter(row["split"] for row in raw)
    pair_cells: dict[str, set[str]] = defaultdict(set)
    for row in world:
        if row["design"] == "core":
            pair_cells[row["pair_block"]].add(row["cell"])
    neutral_pair_cells_pass = (
        len(pair_cells) == 10
        and all(cells == {"00", "01", "10", "11"} for cells in pair_cells.values())
    )
    moc_codebook_exists = (ROOT / "world" / "MOC_SLOT_CODEBOOK.json").exists()

    coverage_a = _coverage(ann_a, raw_by_case)
    coverage_b = _coverage(ann_b, raw_by_case)
    observed_coverage_pass = _coverage_pass(coverage_a) and _coverage_pass(coverage_b)

    agreement = confusion["raw_agreement"]
    binary = confusion["binary_present_vs_non_present"]
    unknown = confusion["unknown_rates"]
    agreement_pass = all(agreement[c]["rate"] >= 0.65 for c in COMPONENTS)
    agreement_pass &= all(binary[c]["rate"] >= 0.70 for c in COMPONENTS)
    unknown_pass = all(
        unknown[c][f"{annotator}_rate"] <= 0.65
        for c in COMPONENTS for annotator in ("A", "B")
    )

    adjudicated_counts = {c: Counter() for c in COMPONENTS}
    for row in adjudicated:
        for component in COMPONENTS:
            adjudicated_counts[component][row["components"][component]["status"]] += 1
    adjudicated_counts_dict = {c: dict(sorted(v.items())) for c, v in adjudicated_counts.items()}

    change_terms = ("no cambia", "no hay cambio", "sin modificar", "sin cambio",
                    "se mantiene", "permanece estable")
    absent_change_reason: dict[str, int] = {}
    for name, rows in (("A", ann_a), ("B", ann_b), ("ADJ", adjudicated)):
        count = 0
        for row in rows:
            for component in COMPONENTS:
                record = row["components"][component]
                reason = str(record.get("reason", "")).lower()
                if record["status"] == "ABSENT" and any(term in reason for term in change_terms):
                    count += 1
        absent_change_reason[name] = count

    unavailable = [row for row in outcomes if not row["intervention_available"]]
    unavailable_splits = Counter(row["split"] for row in unavailable)
    raw_unique = len({row["family_id"] for row in raw}) == len(raw) == 60
    text_unique = len({row["raw_text"] for row in raw}) == 60
    narrator_integrity = json.loads((ROOT / "INTEGRITY.json").read_text(encoding="utf-8"))
    template_pass = text_unique and narrator_integrity["checks"]["max_pairwise_5gram_jaccard"] < 0.20
    two_annotators = (
        len(ann_a) == len(ann_b) == 60
        and {r["case_id"] for r in ann_a} == {r["case_id"] for r in ann_b}
    )
    adjudication_complete = (
        len(adjudicated) == 60
        and all(not row["adjudication"]["unresolved_components"] for row in adjudicated)
    )
    outcome_independence = all(row["outcome_author"] == "F0_1_OUTCOME_AUTHOR_INDEPENDENT"
                               for row in outcomes)
    outcome_independence &= narrator_integrity["role"] == "NARRATOR"
    label_manifest_pass = (
        permutation["source"]["sha256"] == _sha(ROOT / "adjudication" / "adjudicated.jsonl")
        and set(permutation["per_component_cyclic_offsets"]) == set(COMPONENTS)
    )

    gate = {
        "EXACT_60_INDEPENDENT_FAMILIES": "PASS" if raw_unique else "FAIL",
        "SPLITS_35_10_15": "PASS" if split_counts == {"train": 35, "validation": 10, "test": 15} else "FAIL",
        "ALL_10_PAIRWISE_4_CELL_BLOCKS_NEUTRAL": "PASS" if neutral_pair_cells_pass else "FAIL",
        "MOC_PAIR_TO_SLOT_MAPPING_PREREGISTERED": "PASS" if moc_codebook_exists else "FAIL",
        "ALL_5_FACTORS_HAVE_POSITIVE_NEGATIVE_AMBIGUOUS_COVERAGE": "PASS" if observed_coverage_pass else "FAIL",
        "EAF_EXPLICIT_IMPLICIT_ABSENT_DECOY_OBSERVABLE": "PASS" if moc_codebook_exists and observed_coverage_pass else "FAIL",
        "TEST_INDEPENDENT_FAMILIES_GE_15": "PASS" if split_counts["test"] >= 15 else "FAIL",
        "TWO_BLIND_ANNOTATORS": "PASS" if two_annotators else "FAIL",
        "ANNOTATOR_AGREEMENT_THRESHOLDS": "PASS" if agreement_pass else "FAIL",
        "ADJUDICATION_COMPLETE": "PASS" if adjudication_complete else "FAIL",
        "OUTCOME_SOURCE_INDEPENDENCE": "PASS" if outcome_independence else "FAIL",
        "INTERVENTION_UNAVAILABLE_GE_12": "PASS" if len(unavailable) >= 12 else "FAIL",
        "INTERVENTION_NEGATIVES_EACH_SPLIT": "PASS" if all(unavailable_splits[s] >= 2 for s in SPLITS) else "FAIL",
        "TEMPLATE_CONTAMINATION_AUDIT": "PASS" if template_pass else "FAIL",
        "UNKNOWN_RATE_WITHIN_LIMIT": "PASS" if unknown_pass else "FAIL",
        "LABEL_PERMUTATION_MANIFEST": "PASS" if label_manifest_pass else "FAIL",
        "NO_HUMAN_OR_CLINICAL_DATA": "PASS" if all(row["synthetic_nonclinical"] for row in world) else "FAIL",
    }
    blockers = [name for name, status in gate.items() if status == "FAIL"]
    if any(absent_change_reason.values()):
        blockers.append("ABSENT_VS_STABLE_SEMANTIC_CONFUSION")
    if adjudicated_counts["S"].get("PRESENT", 0) == 60:
        blockers.append("S_ALWAYS_PRESENT_BY_PROJECTION_DESIGN")
    warnings: list[str] = []
    if permutation["performance_sanity_check"] == "PENDING_MODEL_PHASE":
        warnings.append("LABEL_PERMUTATION_PERFORMANCE_CHECK_PENDING")
    if len(adjudicated_counts["EAF"]) and adjudicated_counts["EAF"].get("PRESENT", 0) < 8:
        warnings.append("EAF_PRESENT_REMAINS_SPARSE")
    passed = sum(status == "PASS" for status in gate.values())
    failed = len(gate) - passed
    return GateAudit(
        gate, passed, failed, "SUPPORTED" if not blockers else "NOT_SUPPORTED",
        dict(sorted(split_counts.items())),
        {k: sorted(v) for k, v in sorted(pair_cells.items())},
        {"A": coverage_a, "B": coverage_b}, adjudicated_counts_dict,
        {c: agreement[c]["rate"] for c in COMPONENTS},
        {c: binary[c]["rate"] for c in COMPONENTS},
        {c: {"A": unknown[c]["A_rate"], "B": unknown[c]["B_rate"]}
         for c in COMPONENTS}, absent_change_reason, tuple(blockers), tuple(warnings),
    )


if __name__ == "__main__":
    print(audit_gate().to_json())

