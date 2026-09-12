import unittest

from data_contract import (
    FORBIDDEN_MODEL_INPUT_FIELDS, RawObservation, audit_group_splits,
    audit_model_view,
)
from evaluation import (
    BinaryPrediction, accuracy, brier, expected_calibration_error,
    paired_effect,
)
from fairness import Budget, compare_budgets
from protocol import BOUNDARIES, CONTRAST_SPECS, Component, Partition, verify_manifest


class FactorizationProtocolTests(unittest.TestCase):
    def test_all_ten_pairwise_boundaries_and_inverse_directions_exist(self):
        verify_manifest()
        self.assertEqual(len(BOUNDARIES), 10)
        self.assertEqual(len(CONTRAST_SPECS), 20)

    def test_each_contrast_changes_exactly_one_named_component(self):
        for spec in CONTRAST_SPECS:
            self.assertNotIn(spec.changed, spec.held_approximately_constant)
            self.assertEqual(set(spec.held_approximately_constant),
                             set(Component) - {spec.changed})

    def test_model_view_excludes_structural_oracle(self):
        row = RawObservation("C1", "texto crudo", 0, "ctx", "family-1",
                             Partition.DEVELOPMENT)
        audit_model_view(row.model_view())
        self.assertFalse(set(row.model_view()) & FORBIDDEN_MODEL_INPUT_FIELDS)

    def test_group_split_leakage_is_rejected(self):
        rows = (
            RawObservation("C1", "a", 0, "x", "family", Partition.DEVELOPMENT),
            RawObservation("C2", "b", 1, "x", "family", Partition.DOMAIN_HOLDOUT),
        )
        with self.assertRaises(AssertionError):
            audit_group_splits(rows)

    def test_equal_budget_requires_equal_concept_supervision(self):
        generic = Budget(100, 0, 100, 1000, 10000, 100, 10)
        moc = Budget(100, 500, 100, 1000, 10000, 100, 10)
        audit = compare_budgets(generic, moc)
        self.assertFalse(audit.matched)
        self.assertIn("CONCEPT_SUPERVISION_NOT_MATCHED", audit.violations)

    def test_equal_budgets_pass(self):
        budget = Budget(100, 500, 100, 1000, 10000, 100, 10)
        self.assertTrue(compare_budgets(budget, budget).matched)

    def test_prediction_metrics_are_not_replaced_by_accuracy(self):
        calibrated = (BinaryPrediction(1, .8), BinaryPrediction(0, .2))
        overconfident = (BinaryPrediction(1, 1.0), BinaryPrediction(0, 0.0))
        self.assertEqual(accuracy(calibrated), accuracy(overconfident))
        self.assertNotEqual(brier(calibrated), brier(overconfident))
        self.assertGreater(expected_calibration_error(calibrated), 0.0)

    def test_paired_effect_uses_same_cases(self):
        self.assertAlmostEqual(paired_effect((.8, .7), (.6, .6)), .15)


if __name__ == "__main__":
    unittest.main()
