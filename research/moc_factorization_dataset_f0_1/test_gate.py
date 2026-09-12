import unittest

from audit_gate import audit_gate


class F01GateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = audit_gate()

    def test_sixty_independent_families_and_splits_pass(self):
        self.assertEqual(self.audit.gate["EXACT_60_INDEPENDENT_FAMILIES"], "PASS")
        self.assertEqual(self.audit.raw_counts, {"test": 15, "train": 35, "validation": 10})

    def test_neutral_four_cell_design_passes(self):
        self.assertEqual(self.audit.gate["ALL_10_PAIRWISE_4_CELL_BLOCKS_NEUTRAL"], "PASS")
        self.assertTrue(all(cells == ["00", "01", "10", "11"]
                            for cells in self.audit.core_pair_cells.values()))

    def test_missing_moc_slot_mapping_is_not_invented_post_hoc(self):
        self.assertEqual(self.audit.gate["MOC_PAIR_TO_SLOT_MAPPING_PREREGISTERED"], "FAIL")

    def test_two_annotators_and_adjudication_exist(self):
        self.assertEqual(self.audit.gate["TWO_BLIND_ANNOTATORS"], "PASS")
        self.assertEqual(self.audit.gate["ADJUDICATION_COMPLETE"], "PASS")

    def test_v_agreement_and_unknown_limits_fail(self):
        self.assertLess(self.audit.raw_agreement["V"], 0.65)
        self.assertGreater(self.audit.unknown_rates["V"]["B"], 0.65)
        self.assertEqual(self.audit.gate["ANNOTATOR_AGREEMENT_THRESHOLDS"], "FAIL")
        self.assertEqual(self.audit.gate["UNKNOWN_RATE_WITHIN_LIMIT"], "FAIL")

    def test_factor_coverage_gate_fails(self):
        self.assertEqual(
            self.audit.gate["ALL_5_FACTORS_HAVE_POSITIVE_NEGATIVE_AMBIGUOUS_COVERAGE"],
            "FAIL",
        )

    def test_outcomes_and_intervention_negatives_pass(self):
        self.assertEqual(self.audit.gate["OUTCOME_SOURCE_INDEPENDENCE"], "PASS")
        self.assertEqual(self.audit.gate["INTERVENTION_UNAVAILABLE_GE_12"], "PASS")
        self.assertEqual(self.audit.gate["INTERVENTION_NEGATIVES_EACH_SPLIT"], "PASS")

    def test_template_audit_and_label_manifest_pass(self):
        self.assertEqual(self.audit.gate["TEMPLATE_CONTAMINATION_AUDIT"], "PASS")
        self.assertEqual(self.audit.gate["LABEL_PERMUTATION_MANIFEST"], "PASS")

    def test_absent_stable_confusion_is_visible(self):
        self.assertGreater(self.audit.absent_change_reason_count["A"], 0)
        self.assertIn("ABSENT_VS_STABLE_SEMANTIC_CONFUSION", self.audit.blockers)

    def test_training_readiness_fails_conjunctively(self):
        self.assertEqual(self.audit.training_readiness, "NOT_SUPPORTED")
        self.assertGreater(self.audit.failed, 0)


if __name__ == "__main__":
    unittest.main()
