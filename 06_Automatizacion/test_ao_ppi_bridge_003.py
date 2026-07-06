import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_ppi_bridge_003


class AOPPIBridge003Tests(unittest.TestCase):
    def test_default_matrix_passes_without_global_closure(self):
        report = ao_ppi_bridge_003.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertEqual(report["summary"]["conditions"], 10)
        self.assertEqual(report["summary"]["report_layer_cases"], 9)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_missing_conditions_block_global_closure(self):
        report = ao_ppi_bridge_003.build_report()

        self.assertGreater(report["condition_summary"]["missing_or_blocking"], 0)
        self.assertGreater(report["condition_summary"]["by_status"]["faltante_global"], 0)
        self.assertGreater(report["condition_summary"]["by_status"]["bloqueada_por_alcance"], 0)
        self.assertFalse(report["scope_guard"]["cierra_confluencia_global"])
        self.assertFalse(report["scope_guard"]["cierra_equivalencia_global"])
        self.assertFalse(report["scope_guard"]["reabre_p_pi_0"])
        self.assertFalse(report["scope_guard"]["reabre_p_pi_1"])

    def test_report_layer_heterogeneous_cases_are_classified(self):
        report = ao_ppi_bridge_003.build_report()
        outcomes = {item["case_id"]: item["actual"] for item in report["report_layer_results"]}

        self.assertEqual(outcomes["RL-HET-001"], "compatible_heterogeneo_no_mutante")
        self.assertEqual(outcomes["RL-HET-004"], "compatible_heterogeneo_no_mutante")
        self.assertEqual(outcomes["RL-HET-005"], "divergencia_clasificada")
        self.assertEqual(outcomes["RL-HET-006"], "bloqueo_testigo")
        self.assertEqual(outcomes["RL-HET-007"], "bloqueo_recomendacion_como_decision")
        self.assertEqual(outcomes["RL-HET-008"], "bloqueo_autoridad")
        self.assertEqual(outcomes["RL-HET-009"], "bloqueo_modo_mutante")


if __name__ == "__main__":
    unittest.main()
