import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report_layer_c002_gate


class ReportLayerC002GateTests(unittest.TestCase):
    def test_gate_cases_pass_without_transforming_or_promoting(self) -> None:
        report = report_layer_c002_gate.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["conforme_c002_no_mutante"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 8)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertFalse(report["scope_guard"]["crea_nivel_c"])
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])
        self.assertFalse(report["scope_guard"]["autoriza_transformacion"])

    def test_gate_covers_c002_blockers(self) -> None:
        report = report_layer_c002_gate.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["RL-C002-001"], "compatible_no_mutante")
        self.assertEqual(outcomes["RL-C002-002"], "compatible_no_mutante")
        self.assertEqual(outcomes["RL-C002-003"], "bloqueo_campos_minimos")
        self.assertEqual(outcomes["RL-C002-004"], "bloqueo_recomendacion_como_decision")
        self.assertEqual(outcomes["RL-C002-005"], "bloqueo_modo_mutante")
        self.assertEqual(outcomes["RL-C002-006"], "bloqueo_promocion_nivel_c")
        self.assertEqual(outcomes["RL-C002-007"], "bloqueo_historial_autoridad")
        self.assertEqual(outcomes["RL-C002-008"], "bloqueo_permiso_material")

    def test_required_fields_include_c002_report_contract(self) -> None:
        report = report_layer_c002_gate.build_report()
        fields = set(report["c002_guard"]["campos_requeridos"])

        self.assertIn("decision_emitida", fields)
        self.assertIn("transformacion_permitida", fields)
        self.assertIn("deudas_generadas", fields)
        self.assertTrue(report["c002_guard"]["separa_recomendacion_decision_permiso"])
        self.assertTrue(report["c002_guard"]["modo_mutante_bloqueado"])


if __name__ == "__main__":
    unittest.main()
