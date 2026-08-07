import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_global_reconsider_001


class AOGlobalReconsider001Tests(unittest.TestCase):
    def test_reconsideration_keeps_global_not_authorized(self):
        report = ao_global_reconsider_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertEqual(report["global_reconsideration_result"], "mantener_no_autorizado_con_perfiles_formales_preparados")
        self.assertTrue(report["external_evidence_ready"])
        self.assertTrue(report["report_layer_formal_profile_prepared"])
        self.assertTrue(report["r4_gamma_export_profile_prepared"])
        self.assertFalse(report["ready_for_global_decision"])
        self.assertFalse(report["report_layer_formal_promotion_authorized"])
        self.assertFalse(report["r4_gamma_general_export_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_closure_authorized"])

    def test_next_logical_route_is_validation_packet(self):
        report = ao_global_reconsider_001.build_report()

        self.assertEqual(report["next_logical_route"], "AO-EXT-VALIDATION-PACKET-001")
        self.assertEqual(report["summary"]["local_credit"], 3)
        self.assertEqual(report["summary"]["blocking_conditions"], 4)
        self.assertFalse(report["scope_guard"]["ejecuta_validacion_externa"])
        self.assertIn("AO-GR2-004", report["blocking_reason"])


if __name__ == "__main__":
    unittest.main()
