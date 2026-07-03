import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auditor_v0


ROOT = Path(__file__).resolve().parents[1]


class AuditorV0Tests(unittest.TestCase):
    def test_default_cases_cover_c002_matrix(self) -> None:
        report = auditor_v0.build_report(ROOT)
        summary = report["summary"]

        self.assertTrue(report["conforme_c002"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(summary["cases_checked"], 10)
        self.assertEqual(summary["mandatory_missing"], [])
        self.assertEqual(summary["schema_errors"], [])
        self.assertEqual(summary["operator_reports"], 11)

    def test_all_reports_are_non_mutant(self) -> None:
        report = auditor_v0.build_report(ROOT)

        for case in report["cases"]:
            self.assertFalse(case["transformacion_permitida"])
            for item in case["reports"]:
                self.assertFalse(item["transformacion_permitida"])

    def test_expected_case_results_are_stable(self) -> None:
        report = auditor_v0.build_report(ROOT)
        results = {case["case_id"]: case["resultado"] for case in report["cases"]}

        self.assertEqual(results["AUD-T00"], "ok")
        self.assertEqual(results["AUD-T01"], "bloqueado")
        self.assertEqual(results["AUD-T02"], "advertencia")
        self.assertEqual(results["AUD-T03"], "bloqueado")
        self.assertEqual(results["AUD-T04"], "bloqueado")
        self.assertEqual(results["AUD-T05"], "bloqueado")
        self.assertEqual(results["AUD-T06"], "bloqueado")
        self.assertEqual(results["AUD-T07"], "bloqueado")
        self.assertEqual(results["AUD-T08"], "bloqueado")
        self.assertEqual(results["AUD-T09"], "advertencia")

    def test_malformed_case_is_blocked_without_crash(self) -> None:
        case = {"kind": "automaton", "automaton": {"transitions": [["q0", "a"]]}}

        result = auditor_v0.evaluate_case(case)

        self.assertEqual(result["resultado"], "bloqueado")
        self.assertEqual(result["reports"][0]["operador"], "Mp")
        self.assertIn("id ausente", result["reports"][0]["evidencia"])
        self.assertFalse(result["transformacion_permitida"])

    def test_duplicate_case_ids_break_conformity(self) -> None:
        report = auditor_v0.build_report_from_cases([auditor_v0.DEFAULT_CASES[0], auditor_v0.DEFAULT_CASES[0]])

        self.assertFalse(report["conforme_c002"])
        self.assertIn("case_id duplicado: AUD-T00", report["summary"]["schema_errors"])

    def test_report_schema_validator_rejects_mutation_permission(self) -> None:
        bad_report = auditor_v0.op_report(
            "AUD-TXX",
            "D",
            1,
            "ok",
            "sin_hallazgo_bloqueante",
            "integracion",
            "reporte de prueba",
            "evidencia",
            "definicion",
            ["aprobar"],
            "aprobar",
            "exito",
            "exito",
        )
        bad_report["transformacion_permitida"] = True

        errors = auditor_v0.report_schema_errors([bad_report])

        self.assertEqual(errors, ["AUDITOR-V0-001-AUD-TXX-D-01: transformacion_permitida debe ser false"])


if __name__ == "__main__":
    unittest.main()
