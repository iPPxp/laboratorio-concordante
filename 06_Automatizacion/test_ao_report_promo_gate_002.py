import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_report_promo_gate_002


class AOReportPromoGate002Tests(unittest.TestCase):
    def test_prepares_formal_profile_without_promotion(self):
        report = ao_report_promo_gate_002.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["report_layer_formal_profile_prepared"])
        self.assertTrue(report["report_layer_candidate_future"])
        self.assertFalse(report["report_layer_formal_promotion_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertEqual(report["summary"]["conditions"], 7)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_blocks_are_explicit(self):
        report = ao_report_promo_gate_002.build_report()

        self.assertEqual(report["summary"]["local_credit"], 3)
        self.assertEqual(report["summary"]["blocking_conditions"], 4)
        self.assertIn("AO-RL-FP-004", report["blocking_reason"])
        self.assertIn("AO-RL-FP-007", report["blocking_reason"])
        self.assertFalse(report["scope_guard"]["crea_nivel_c"])
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])


if __name__ == "__main__":
    unittest.main()
