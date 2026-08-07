from __future__ import annotations

import copy
import os
import sys
import unittest
from pathlib import Path


PACKAGE_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = PACKAGE_DIR / "src"
sys.path.insert(0, str(SOURCE_DIR))

from moc_extractor_001_c import (
    EXPECTED_BANK_SHA256,
    EXPECTED_INVENTORY,
    ContractError,
    bank_inventory,
    canonicalize_candidate_spans,
    compare_semantics,
    gold_batch,
    load_bank,
    project_model_input,
    strict_json_loads,
    validate_structure,
)


DEFAULT_BANK = Path(
    r"C:\Users\IximM\Downloads\MOC-EXTRACTOR-001-B_EXP-A-DEV_v3.1.json"
)


class ExtractorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bank_path = Path(os.environ.get("MOC_EXTRACTOR_DEV_BANK", DEFAULT_BANK))
        cls.bank = load_bank(cls.bank_path, EXPECTED_BANK_SHA256)

    def test_authoritative_inventory(self) -> None:
        self.assertEqual(bank_inventory(self.bank), EXPECTED_INVENTORY)

    def test_projection_excludes_annotations(self) -> None:
        projected = project_model_input(self.bank)
        serialized = str(projected)
        for forbidden_key in (
            "expected_claims",
            "constraint_candidates",
            "expected_unknowns",
            "expected_frictions",
            "forbidden_inferences",
            "acceptance_notes",
        ):
            if forbidden_key == "constraint_candidates":
                self.assertNotIn(forbidden_key, projected["cases"][0])
            else:
                self.assertNotIn(forbidden_key, serialized)

    def test_strict_parser_rejects_duplicate_keys(self) -> None:
        with self.assertRaisesRegex(ContractError, "duplicate JSON key"):
            strict_json_loads('{"schema_version":"1.0.0","schema_version":"1.0.0"}')

    def test_gold_fixture_has_zero_contract_errors(self) -> None:
        candidate = gold_batch(self.bank)
        issues = validate_structure(candidate, self.bank)
        semantic_issues, metrics = compare_semantics(candidate, self.bank)
        self.assertEqual(issues, [])
        self.assertEqual(semantic_issues, [])
        for metric in metrics["by_category"].values():
            self.assertEqual(metric["expected"], metric["predicted"])
            self.assertEqual(metric["expected"], metric["exact"])

    def test_invalid_unicode_span_is_detected(self) -> None:
        candidate = copy.deepcopy(gold_batch(self.bank))
        candidate["cases"][0]["claims"][0]["evidence_span"]["start"] += 1
        issues = validate_structure(candidate, self.bank)
        self.assertIn("invalid_span", {issue.category for issue in issues})

    def test_unique_evidence_text_canonicalizes_span_only(self) -> None:
        candidate = copy.deepcopy(gold_batch(self.bank))
        record = candidate["cases"][0]["claims"][0]
        original_text = record["evidence_span"]["text"]
        original_start = record["evidence_span"]["start"]
        original_normalized = record["normalized_value"]
        record["evidence_span"]["start"] += 1
        parsed, notes = canonicalize_candidate_spans(candidate, self.bank)
        parsed_record = parsed["cases"][0]["claims"][0]
        self.assertEqual(parsed_record["evidence_span"]["text"], original_text)
        self.assertEqual(parsed_record["normalized_value"], original_normalized)
        self.assertEqual(parsed_record["evidence_span"]["start"], original_start)
        self.assertEqual(notes[0]["status"], "canonicalized")

    def test_broken_claim_reference_is_detected(self) -> None:
        candidate = copy.deepcopy(gold_batch(self.bank))
        candidate["cases"][0]["frictions"][0]["claim_refs"][0] = "DEV001-C99"
        issues = validate_structure(candidate, self.bank)
        self.assertIn("broken_reference", {issue.category for issue in issues})

    def test_must_not_produce_is_detected(self) -> None:
        candidate = copy.deepcopy(gold_batch(self.bank))
        candidate["cases"][0]["matrix_q"] = {}
        issues = validate_structure(candidate, self.bank)
        categories = {issue.category for issue in issues}
        self.assertIn("schema_error", categories)
        self.assertIn("must_not_produce", categories)

    def test_semantic_taxonomy_separates_failure_classes(self) -> None:
        candidate = copy.deepcopy(gold_batch(self.bank))
        first_case = candidate["cases"][0]
        first_case["claims"].pop()
        first_case["claims"][0]["normalized_value"] = "normalizacion_incorrecta"
        extra = copy.deepcopy(first_case["claims"][0])
        extra["claim_id"] = "DEV001-C99"
        extra["field"] = "estado_factual"
        first_case["claims"].append(extra)
        issues, _ = compare_semantics(candidate, self.bank)
        categories = {issue.category for issue in issues}
        self.assertIn("omission", categories)
        self.assertIn("spurious_extraction", categories)
        self.assertIn("incorrect_normalization", categories)


if __name__ == "__main__":
    unittest.main()
