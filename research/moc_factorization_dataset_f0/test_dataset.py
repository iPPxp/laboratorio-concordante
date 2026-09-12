import unittest

from audit_dataset import audit


class F0DatasetAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit()

    def test_all_layers_have_same_72_ids(self):
        self.assertEqual(
            (self.result.raw_records, self.result.annotation_records,
             self.result.outcome_records), (72, 72, 72)
        )
        self.assertTrue(self.result.id_sets_match)

    def test_raw_schema_is_exact_and_family_split_is_sealed(self):
        self.assertTrue(self.result.visible_schema_exact)
        self.assertFalse(self.result.family_leakage)
        self.assertEqual(self.result.effective_families, 24)

    def test_all_primary_digests_match(self):
        self.assertTrue(self.result.raw_digest_ok)
        self.assertTrue(self.result.annotation_digest_ok)
        self.assertTrue(self.result.outcome_digest_ok)

    def test_outcomes_do_not_expose_moc_field_names(self):
        self.assertEqual(self.result.outcome_prohibited_key_matches, 0)

    def test_role_identifiers_are_separate(self):
        self.assertTrue(self.result.independent_role_ids)

    def test_integrity_passes_but_confirmatory_readiness_does_not(self):
        self.assertTrue(self.result.hard_integrity_ok)
        self.assertFalse(self.result.benchmark_ready)

    def test_eaf_zero_present_is_preserved_as_blocker(self):
        self.assertEqual(self.result.present_by_component["EAF"], 0)
        self.assertIn("AT_LEAST_ONE_COMPONENT_HAS_ZERO_PRESENT_EXAMPLES",
                      self.result.blockers)

    def test_synthetic_outcome_source_is_not_called_external(self):
        self.assertFalse(self.result.external_outcome_source)
        self.assertIn("OUTCOME_SOURCE_IS_SYNTHETIC_DATASET_DESIGN",
                      self.result.blockers)

    def test_intervention_negative_control_gap_is_visible(self):
        self.assertEqual(self.result.intervention_unavailable_cases, 0)
        self.assertIn("NO_INTERVENTION_UNAVAILABLE_NEGATIVE_CONTROLS",
                      self.result.blockers)

    def test_effective_test_size_is_family_not_paraphrase_count(self):
        self.assertEqual(self.result.family_counts_by_split["test"], 4)
        self.assertIn("TEST_EFFECTIVE_FAMILIES_BELOW_10", self.result.blockers)


if __name__ == "__main__":
    unittest.main()
