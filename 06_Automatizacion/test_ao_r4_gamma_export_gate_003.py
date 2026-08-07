import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_r4_gamma_export_gate_003


class AOR4GammaExportGate003Tests(unittest.TestCase):
    def test_prepares_export_profile_without_general_export(self):
        report = ao_r4_gamma_export_gate_003.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["r4_gamma_export_profile_prepared"])
        self.assertTrue(report["restricted_interoperable_profile_retained"])
        self.assertFalse(report["r4_gamma_general_export_authorized"])
        self.assertFalse(report["r4_gamma_global_export_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertEqual(report["summary"]["conditions"], 7)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_blocks_are_explicit(self):
        report = ao_r4_gamma_export_gate_003.build_report()

        self.assertEqual(report["summary"]["local_credit"], 3)
        self.assertEqual(report["summary"]["blocking_conditions"], 4)
        self.assertIn("AO-R4G-GE-004", report["blocking_reason"])
        self.assertIn("AO-R4G-GE-007", report["blocking_reason"])
        self.assertFalse(report["scope_guard"]["exporta_r4_gamma"])
        self.assertFalse(report["scope_guard"]["modifica_nivel_c"])


if __name__ == "__main__":
    unittest.main()
