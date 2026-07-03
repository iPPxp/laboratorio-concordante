import contextlib
import io
import json
import os
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auditor_do_check_adapter


ROOT = Path(__file__).resolve().parents[1]


class AuditorDoCheckAdapterTests(unittest.TestCase):
    def test_ok_report_projects_non_mutant_report_item(self) -> None:
        source = {
            "report_id": "DO-CHECK-MED-TEST",
            "algoritmo": "DO-CHECK-MED-001",
            "resultado": "ok",
            "recomendacion": "aprobar_lectura",
            "transformacion_permitida": False,
            "fuentes_minimas": ["CURRENT_STATE.md"],
            "findings": [],
        }

        report = auditor_do_check_adapter.adapt_report(source)

        self.assertTrue(report["conforme_c002"])
        self.assertEqual(report["decision_emitida"], "no_aplica")
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["report_items"], 1)
        self.assertEqual(report["report_items"][0]["clase_reporte"], "sin_hallazgo_bloqueante")
        self.assertEqual(report["report_items"][0]["decision_emitida"], "no_aplica")

    def test_warning_finding_projects_as_calculation_failure(self) -> None:
        source = {
            "report_id": "DO-CHECK-MIN-TEST",
            "resultado": "advertencia",
            "recomendacion": "continuar_sin_transformar",
            "transformacion_permitida": False,
            "findings": [
                {
                    "severity": "warning",
                    "kind": "referencia_no_materializada",
                    "file": "03_Expedientes/AUT-001.md",
                    "detail": "referencia faltante",
                }
            ],
        }

        report = auditor_do_check_adapter.adapt_report(source)

        self.assertTrue(report["conforme_c002"])
        self.assertEqual(report["report_items"][0]["clase_reporte"], "calculo_falla")
        self.assertEqual(report["report_items"][0]["objeto"], "03_Expedientes/AUT-001.md")
        self.assertFalse(report["report_items"][0]["transformacion_permitida"])

    def test_source_transform_permission_breaks_conformity(self) -> None:
        source = {
            "report_id": "DO-CHECK-BAD",
            "resultado": "ok",
            "recomendacion": "aprobar_lectura",
            "transformacion_permitida": True,
            "findings": [],
        }

        report = auditor_do_check_adapter.adapt_report(source)

        self.assertFalse(report["conforme_c002"])
        self.assertIn("transformacion_permitida debe ser false", report["summary"]["adapter_errors"])

    def test_cli_adapts_existing_do_check_report(self) -> None:
        stdout = io.StringIO()
        cwd = Path.cwd()
        try:
            os.chdir(ROOT)
            with contextlib.redirect_stdout(stdout):
                code = auditor_do_check_adapter.main([
                    "06_Automatizacion/reportes/do_check_med_repo.json",
                    "--format",
                    "json",
                ])
        finally:
            os.chdir(cwd)

        report = json.loads(stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertTrue(report["conforme_c002"])
        self.assertEqual(report["fuente_algoritmo"], "DO-CHECK-MED-001")
        self.assertFalse(report["transformacion_permitida"])


if __name__ == "__main__":
    unittest.main()
