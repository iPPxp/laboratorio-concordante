import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_eq_global_gate_001


class AOEQGlobalGate001Tests(unittest.TestCase):
    def test_gate_passes_without_global_equivalence(self):
        report = ao_eq_global_gate_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertFalse(report["global_equivalence_authorized"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertEqual(report["summary"]["conditions"], 8)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_global_gaps_remain_visible(self):
        report = ao_eq_global_gate_001.build_report()

        self.assertEqual(report["summary"]["missing_global"], 1)
        self.assertEqual(report["summary"]["scope_blocked"], 1)
        self.assertEqual(report["summary"]["global_blocking"], 2)
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])
        self.assertFalse(report["scope_guard"]["exporta_r4_gamma"])


if __name__ == "__main__":
    unittest.main()
