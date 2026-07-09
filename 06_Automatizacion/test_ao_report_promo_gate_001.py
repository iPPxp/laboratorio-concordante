import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_report_promo_gate_001


class AOReportPromoGate001Tests(unittest.TestCase):
    def test_report_layer_gate_passes_without_promotion(self):
        report = ao_report_promo_gate_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["report_layer_candidate_future"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["r4_gamma_global_export_authorized"])
        self.assertEqual(report["summary"]["cases"], 7)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_blocks_promotion_paths(self):
        report = ao_report_promo_gate_001.build_report()

        self.assertEqual(report["summary"]["future_candidate_cases"], 1)
        self.assertEqual(report["summary"]["blocked_cases"], 6)
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])
        self.assertFalse(report["scope_guard"]["modifica_nivel_c"])
        self.assertFalse(report["scope_guard"]["autoriza_transformacion"])


if __name__ == "__main__":
    unittest.main()
