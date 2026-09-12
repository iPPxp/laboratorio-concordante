import unittest

from benchmark import run_benchmark, run_case
from fixtures import CASES, DEVELOPMENT_CASES, TRANSFORMATION_HOLDOUT_CASES, verify_fixture_integrity
from isomorphism import compare_traces
from moc_reorganization import structural_diff
from oracle import ORACLE_AUTHOR, evaluate_fixture, verify_rubric


class IndependenceTests(unittest.TestCase):
    def test_fixtures_and_oracle_are_frozen_and_separate(self):
        verify_fixture_integrity()
        verify_rubric()
        self.assertNotEqual(ORACLE_AUTHOR, CASES[0].author)
        self.assertEqual((len(CASES), len(DEVELOPMENT_CASES),
                          len(TRANSFORMATION_HOLDOUT_CASES)), (12, 6, 6))

    def test_fixture_oracle_recovers_frozen_reorganization_labels(self):
        for case in CASES:
            with self.subTest(case=case.case_id):
                result = evaluate_fixture(case)
                self.assertEqual(result.reorganization_observed,
                                 case.expected.reorganization_expected)


class ReorganizationTests(unittest.TestCase):
    def test_structural_diff_does_not_depend_on_case_id(self):
        for case in CASES:
            with self.subTest(case=case.case_id):
                edits = structural_diff(case.before, case.after)
                self.assertNotIn(case.case_id, repr(edits))

    def test_b6_and_moc_r_reach_same_target_structure(self):
        for case in CASES:
            with self.subTest(case=case.case_id):
                results = run_case(case)
                for system in ("B6", "MOC_R"):
                    result = results[system]
                    self.assertEqual(dict(result.after.D), dict(case.after.D))
                    self.assertEqual(set(result.after.R), set(case.after.R))
                    self.assertEqual(result.after.K, case.after.K)

    def test_action_and_reorganization_are_crossed(self):
        action_only = next(c for c in CASES if c.case_id == "HOLD-ACT-001")
        same_action = next(c for c in CASES if c.case_id == "HOLD-ACT-002")
        self.assertFalse(action_only.expected.reorganization_expected)
        self.assertTrue(action_only.expected.action_changed)
        self.assertTrue(same_action.expected.reorganization_expected)
        self.assertFalse(same_action.expected.action_changed)

    def test_frozen_mapping_is_exact_on_development_and_holdout(self):
        for case in CASES:
            with self.subTest(case=case.case_id):
                results = run_case(case)
                self.assertTrue(compare_traces(results["B6"], results["MOC_R"]).exact)

    def test_b5_search_expansion_is_not_target_structure_edit(self):
        summary = run_benchmark()
        self.assertEqual(summary.aggregate["B5"]["target_structure_rate"], 0.0)
        self.assertEqual(summary.aggregate["B5"]["target_field_rate"], 0.0)
        self.assertTrue(any(
            run_case(case)["B5"].delta.expansion > 0 for case in CASES
        ))

    def test_b6_falsifies_algorithmic_uniqueness_in_test_domain(self):
        summary = run_benchmark()
        self.assertEqual(summary.aggregate["MOC_R"]["holdout_structure_rate"], 1.0)
        self.assertEqual(summary.aggregate["B6"]["holdout_structure_rate"], 1.0)
        self.assertEqual(summary.generic_isomorphism_holdout_rate, 1.0)
        self.assertEqual(summary.isomorphism_witnesses, ())


if __name__ == "__main__":
    unittest.main()
