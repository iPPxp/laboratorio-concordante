import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_ppi_bridge_002


class AOPPIBridge002Tests(unittest.TestCase):
    def test_default_suite_passes(self):
        report = ao_ppi_bridge_002.build_report()
        self.assertEqual(report["resultado"], "ok")
        self.assertEqual(report["summary"]["cases"], 8)
        self.assertEqual(report["summary"]["passed"], 8)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_scope_guards_preserve_global_debts(self):
        report = ao_ppi_bridge_002.build_report()
        self.assertFalse(report["transformacion_permitida"])
        self.assertFalse(report["scope_guard"]["cierra_confluencia_global"])
        self.assertFalse(report["scope_guard"]["cierra_equivalencia_global"])
        self.assertFalse(report["scope_guard"]["reabre_p_pi_0"])
        self.assertFalse(report["scope_guard"]["reabre_p_pi_1"])
        self.assertTrue(report["debt_guard"]["confluencia_global_abierta"])
        self.assertTrue(report["debt_guard"]["equivalencia_global_abierta"])

    def test_negative_cases_are_classified_not_hidden(self):
        report = ao_ppi_bridge_002.build_report()
        outcomes = {item["case_id"]: item["actual"] for item in report["results"]}
        self.assertEqual(outcomes["AO-PPI-STRONG-003"], "divergencia_clasificada")
        self.assertEqual(outcomes["AO-PPI-STRONG-006"], "bloqueo_por_testigo")
        self.assertEqual(outcomes["AO-PPI-STRONG-007"], "bloqueo_report_layer_incompleto")
        self.assertEqual(outcomes["AO-PPI-STRONG-008"], "bloqueo_por_autoridad")


if __name__ == "__main__":
    unittest.main()
