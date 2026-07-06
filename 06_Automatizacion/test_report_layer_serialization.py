import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report_layer_serialization


class ReportLayerSerializationTests(unittest.TestCase):
    def test_serialization_cases_pass_without_global_export(self) -> None:
        report = report_layer_serialization.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["serializacion_interfrente_local"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 10)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertFalse(report["scope_guard"]["crea_nivel_c"])
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])
        self.assertFalse(report["scope_guard"]["cierra_confluencia_global"])
        self.assertEqual(report["condition_effect"]["ao_ppi_gc_004"], "atendida_localmente_no_global")

    def test_serialization_classifies_expected_blockers(self) -> None:
        report = report_layer_serialization.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["RL-SERIAL-001"], "serializable_interfrente_no_mutante")
        self.assertEqual(outcomes["RL-SERIAL-004"], "serializable_interfrente_no_mutante")
        self.assertEqual(outcomes["RL-SERIAL-005"], "serializable_con_divergencia_clasificada")
        self.assertEqual(outcomes["RL-SERIAL-006"], "bloqueo_testigo")
        self.assertEqual(outcomes["RL-SERIAL-007"], "bloqueo_perdida_campo_protegido")
        self.assertEqual(outcomes["RL-SERIAL-008"], "bloqueo_autoridad")
        self.assertEqual(outcomes["RL-SERIAL-009"], "bloqueo_modo_mutante")
        self.assertEqual(outcomes["RL-SERIAL-010"], "bloqueo_version")

    def test_contract_preserves_protected_fields(self) -> None:
        report = report_layer_serialization.build_report()
        protected = set(report["contract"]["protected_fields"])
        required_map = set(report["contract"]["required_field_map"])

        self.assertIn("decision_emitida", protected)
        self.assertIn("transformacion_permitida", protected)
        self.assertIn("witness", protected)
        self.assertIn("emitted_decision", required_map)
        self.assertIn("transformation_allowed", required_map)
        self.assertIn("authority_claim", required_map)


if __name__ == "__main__":
    unittest.main()
