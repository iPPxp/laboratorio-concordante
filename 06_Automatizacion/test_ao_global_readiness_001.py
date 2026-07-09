import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_global_readiness_001


class AOGlobalReadiness001Tests(unittest.TestCase):
    def test_readiness_keeps_global_not_authorized(self):
        report = ao_global_readiness_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertEqual(report["readiness_result"], "mantener_no_autorizado")
        self.assertFalse(report["ready_for_global_decision"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_equivalence_authorized"])
        self.assertFalse(report["global_confluence_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertFalse(report["r4_gamma_global_export_authorized"])

    def test_consolidates_all_fronts(self):
        report = ao_global_readiness_001.build_report()

        self.assertEqual(report["summary"]["conditions"], 6)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertEqual(report["summary"]["missing_global"], 2)
        self.assertEqual(report["summary"]["no_promotion"], 1)
        self.assertEqual(report["summary"]["no_export"], 1)
        self.assertEqual(report["summary"]["global_blocking"], 4)
        self.assertFalse(report["scope_guard"]["modifica_doc04"])
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])
        self.assertFalse(report["scope_guard"]["exporta_r4_gamma"])


if __name__ == "__main__":
    unittest.main()
