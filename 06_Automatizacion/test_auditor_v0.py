import unittest
import contextlib
import io
import json
import os
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

    def test_malformed_mandatory_case_breaks_conformity(self) -> None:
        cases = list(auditor_v0.DEFAULT_CASES)
        cases[0] = {
            "id": "AUD-T00",
            "kind": "automaton",
            "declaration": {"deterministic": True, "complete": True},
            "automaton": {
                "states": ["q0"],
                "alphabet": ["a"],
                "initial": "q0",
                "finals": ["q0"],
                "transitions": [["q0", "a", 1]],
            },
        }

        report = auditor_v0.build_report_from_cases(cases)

        self.assertFalse(report["conforme_c002"])
        self.assertIn(
            "AUD-T00: cada transicion debe tener forma [origen, simbolo, destino] de textos",
            report["summary"]["schema_errors"],
        )

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

    def test_json_output_is_active(self) -> None:
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            code = auditor_v0.main(["--format", "json"])

        report = json.loads(stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertTrue(report["conforme_c002"])
        self.assertEqual(report["summary"]["schema_errors"], [])

    def test_external_json_cases_are_active(self) -> None:
        stdout = io.StringIO()
        rel_path = "06_Automatizacion/fixtures/auditor_v0_cases.json"

        cwd = Path.cwd()
        try:
            os.chdir(ROOT)
            with contextlib.redirect_stdout(stdout):
                code = auditor_v0.main(["--format", "json", "--case-file", rel_path])
        finally:
            os.chdir(cwd)

        report = json.loads(stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertTrue(report["conforme_c002"])
        self.assertEqual(report["summary"]["cases_checked"], 10)

    def test_external_case_schema_artifact_is_declared(self) -> None:
        schema_path = ROOT / "06_Automatizacion" / "fixtures" / "auditor_v0_case_schema.json"

        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        kind_branches = [
            branch["if"]["properties"]["kind"]["const"]
            for branch in schema["$defs"]["case"]["allOf"]
        ]

        self.assertEqual(schema["$id"], "AUDITOR-V0-CASE-SCHEMA-001")
        self.assertEqual(schema["required"], ["cases"])
        self.assertIn("fixture_id", schema["properties"])
        self.assertIn("status", schema["properties"])
        self.assertIn("case", schema["$defs"])
        self.assertIn("automaton", schema["$defs"])
        self.assertEqual(kind_branches, ["automaton", "claim", "authority", "level_change", "term"])

    def test_documental_fixture_runs_as_partial_non_mutant(self) -> None:
        rel_path = "06_Automatizacion/fixtures/auditor_v0_documental_cases.json"

        report = auditor_v0.build_report(ROOT, rel_path)
        results = {case["case_id"]: case["resultado"] for case in report["cases"]}

        self.assertFalse(report["conforme_c002"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases_checked"], 4)
        self.assertEqual(report["summary"]["mandatory_missing"], auditor_v0.CASE_IDS)
        self.assertEqual(report["summary"]["schema_errors"], [])
        self.assertEqual(
            results,
            {
                "AUD-DOC01": "bloqueado",
                "AUD-DOC02": "bloqueado",
                "AUD-DOC03": "bloqueado",
                "AUD-DOC04": "advertencia",
            },
        )
        self.assertTrue(all(not case["transformacion_permitida"] for case in report["cases"]))
        self.assertTrue(
            all(not item["transformacion_permitida"] for case in report["cases"] for item in case["reports"])
        )

    def test_documental_case_shape_errors_break_conformity(self) -> None:
        report = auditor_v0.build_report_from_cases(
            [
                {
                    "id": "AUD-DOC-BAD",
                    "kind": "claim",
                    "claim": "afirmacion sin dependencia materializada",
                    "required_dependency": "dependencia documental",
                }
            ]
        )

        self.assertFalse(report["conforme_c002"])
        self.assertEqual(report["cases"][0]["resultado"], "bloqueado")
        self.assertIn(
            "AUD-DOC-BAD: dependency_materialized ausente o debe ser booleano",
            report["summary"]["schema_errors"],
        )
        self.assertTrue(
            all(not item["transformacion_permitida"] for case in report["cases"] for item in case["reports"])
        )


if __name__ == "__main__":
    unittest.main()
