import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_r4_gamma_export_gate_002


class AOR4GammaExportGate002Tests(unittest.TestCase):
    def test_export_gate_passes_without_general_export(self):
        report = ao_r4_gamma_export_gate_002.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["restricted_interoperable_profile_retained"])
        self.assertFalse(report["r4_gamma_global_export_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertEqual(report["summary"]["cases"], 7)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_blocks_export_paths(self):
        report = ao_r4_gamma_export_gate_002.build_report()

        self.assertEqual(report["summary"]["restricted_interoperable_cases"], 1)
        self.assertEqual(report["summary"]["blocked_cases"], 6)
        self.assertFalse(report["scope_guard"]["exporta_r4_gamma"])
        self.assertFalse(report["scope_guard"]["modifica_nivel_c"])
        self.assertFalse(report["scope_guard"]["autoriza_transformacion"])


if __name__ == "__main__":
    unittest.main()
