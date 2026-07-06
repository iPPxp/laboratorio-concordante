import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moc_eval


class MOCEvalTests(unittest.TestCase):
    def test_default_cases_pass_without_transforming(self) -> None:
        report = moc_eval.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 11)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertFalse(report["scope_guard"]["admite_h_xi"])
        self.assertFalse(report["scope_guard"]["canoniza_xi"])
        self.assertFalse(report["scope_guard"]["uso_clinico"])
        self.assertTrue(report["debt_guard"]["moc_provisional_abierto"])
        self.assertTrue(report["debt_guard"]["confluencia_global_abierta"])

    def test_xi_outputs_cover_required_cases(self) -> None:
        report = moc_eval.build_report()
        outputs = {result["actual_xi"] for result in report["results"]}

        self.assertEqual(
            outputs,
            {"redundante", "util_acotado", "limitado", "no_comparable", "bloqueado"},
        )

    def test_moc_states_cover_protocol_targets(self) -> None:
        report = moc_eval.build_report()
        states = {result["actual_moc"] for result in report["results"]}

        self.assertEqual(
            states,
            {
                "concordancia_local",
                "concordancia_parcial",
                "friccion_operativa",
                "discordancia_global",
                "bloqueo_de_concordancia",
                "no_comparable",
            },
        )

    def test_evaluator_protocol_records_exact_partial_and_disagreement(self) -> None:
        report = moc_eval.build_report()
        summary = report["evaluator_summary"]

        self.assertGreater(summary["coincidencia_exacta"], 0)
        self.assertGreater(summary["coincidencia_parcial"], 0)
        self.assertGreater(summary["desacuerdo_justificado"], 0)

    def test_route_002_cases_are_present(self) -> None:
        report = moc_eval.build_report()
        cases = {result["case_id"]: result for result in report["results"]}

        self.assertEqual(cases["MOC-CASE-008"]["agreement"]["kind"], "desacuerdo_justificado")
        self.assertEqual(cases["MOC-CASE-008"]["disagreement_class"], "ambiguedad_de_regla")
        self.assertEqual(cases["MOC-CASE-009"]["actual_moc"], "concordancia_parcial")
        self.assertEqual(cases["MOC-CASE-010"]["actual_moc"], "friccion_operativa")
        self.assertEqual(cases["MOC-CASE-011"]["agreement"]["kind"], "desacuerdo_justificado")

    def test_route_003_operator_traces_define_priority(self) -> None:
        report = moc_eval.build_report()
        cases = {result["case_id"]: result for result in report["results"]}

        self.assertIn("MOC-TCS-BRIDGE-001", report["tests_executed"])
        self.assertEqual(
            cases["MOC-CASE-006"]["operator_trace"]["state"]["rule_id"],
            "STATE-R3-CONFLICTO-GLOBAL",
        )
        self.assertEqual(
            cases["MOC-CASE-008"]["operator_trace"]["xi"]["rule_id"],
            "XI-R5-CONFLICTO-SIN-ESTABILIDAD",
        )
        self.assertEqual(
            cases["MOC-CASE-009"]["operator_trace"]["tcs"]["rule_id"],
            "TCS-R2-EJE-SECUNDARIO-FALTANTE",
        )
        self.assertEqual(
            cases["MOC-CASE-011"]["operator_trace"]["state"]["rule_id"],
            "STATE-R6-CONCORDANCIA-PARCIAL",
        )

    def test_route_004_ao_bridge_uses_operator_trace_without_global_closure(self) -> None:
        report = moc_eval.build_report()
        cases = {result["case_id"]: result for result in report["results"]}

        self.assertIn("MOC-AO-BRIDGE-001", report["tests_executed"])
        self.assertEqual(
            cases["MOC-CASE-002"]["ao_bridge"]["ao_role"],
            "evidencia_auxiliar_equivalencia_local",
        )
        self.assertEqual(
            cases["MOC-CASE-003"]["ao_bridge"]["ao_role"],
            "evidencia_friccion_confluencia_local",
        )
        self.assertEqual(
            cases["MOC-CASE-006"]["ao_bridge"]["ao_role"],
            "deuda_global_no_cierre",
        )
        self.assertEqual(
            cases["MOC-CASE-005"]["ao_bridge"]["ao_role"],
            "bloqueo_seguridad_sin_uso_positivo",
        )
        self.assertEqual(
            cases["MOC-CASE-009"]["ao_bridge"]["pi_moc_trace"]["tcs_rule"],
            "TCS-R2-EJE-SECUNDARIO-FALTANTE",
        )
        for result in report["results"]:
            self.assertFalse(result["ao_bridge"]["closes_equivalence_global"])
            self.assertFalse(result["ao_bridge"]["closes_confluence_global"])
            self.assertFalse(result["ao_bridge"]["modifies_doc04"])
            self.assertFalse(result["ao_bridge"]["transformacion_permitida"])

    def test_route_005_protocol_v02_uses_trace_for_disagreement_review(self) -> None:
        report = moc_eval.build_report()
        cases = {result["case_id"]: result for result in report["results"]}

        self.assertIn("MOC-EVAL-PROTO-002", report["tests_executed"])
        self.assertEqual(report["protocol_v02_summary"]["review_required"], 2)
        self.assertEqual(report["protocol_v02_summary"]["blocked_positive_use"], 2)
        self.assertEqual(
            cases["MOC-CASE-003"]["protocol_v02"]["treatment"],
            "aceptar_operator_trace_con_deuda_visible",
        )
        self.assertEqual(
            cases["MOC-CASE-005"]["protocol_v02"]["treatment"],
            "aceptar_bloqueo_sin_uso_positivo",
        )
        self.assertTrue(cases["MOC-CASE-008"]["protocol_v02"]["review_required"])
        self.assertIn("regla_xi", cases["MOC-CASE-008"]["protocol_v02"]["disagreement_axes"])
        self.assertIn("rol_ao", cases["MOC-CASE-011"]["protocol_v02"]["disagreement_axes"])
        for result in report["results"]:
            self.assertTrue(result["protocol_v02"]["does_not_override_evaluators"])
            self.assertFalse(result["protocol_v02"]["modifies_doc04"])
            self.assertFalse(result["protocol_v02"]["clinical_use"])


if __name__ == "__main__":
    unittest.main()
