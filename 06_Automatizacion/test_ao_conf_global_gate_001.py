import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_conf_global_gate_001


class AOConfGlobalGate001Tests(unittest.TestCase):
    def test_gate_passes_without_global_confluence(self):
        report = ao_conf_global_gate_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertFalse(report["global_confluence_authorized"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertEqual(report["summary"]["conditions"], 7)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_global_confluence_blockers_remain_visible(self):
        report = ao_conf_global_gate_001.build_report()

        self.assertEqual(report["summary"]["missing_global"], 1)
        self.assertEqual(report["summary"]["scope_blocked"], 1)
        self.assertEqual(report["summary"]["global_blocking"], 2)
        self.assertFalse(report["scope_guard"]["cierra_confluencia_global"])
        self.assertFalse(report["scope_guard"]["autoriza_transformacion"])


if __name__ == "__main__":
    unittest.main()
