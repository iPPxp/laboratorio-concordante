import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_doc04_wide_tests


class AODoc04WideTests(unittest.TestCase):
    def test_doc04_wide_cases_pass_without_transforming(self) -> None:
        report = ao_doc04_wide_tests.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 8)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertFalse(report["scope_guard"]["modifica_doc04"])
        self.assertFalse(report["scope_guard"]["crea_nivel_c"])
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])
        self.assertTrue(report["debt_guard"]["confluencia_global_abierta"])
        self.assertEqual(report["report_layer_relation"]["estatus"], "local_pre_c")

    def test_cases_cover_positive_and_blocking_outputs(self) -> None:
        report = ao_doc04_wide_tests.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["AO-WIDE-001"], "equivalencia_local")
        self.assertEqual(outcomes["AO-WIDE-002"], "confluencia_local")
        self.assertEqual(outcomes["AO-WIDE-003"], "bloqueo_por_testigo")
        self.assertEqual(outcomes["AO-WIDE-004"], "no_autorizado_sin_transformar")
        self.assertEqual(outcomes["AO-WIDE-005"], "bloqueo_por_autoridad")
        self.assertEqual(outcomes["AO-WIDE-006"], "divergencia_clasificada")
        self.assertEqual(outcomes["AO-WIDE-007"], "bloqueo_exportacion_r4_gamma")
        self.assertEqual(outcomes["AO-WIDE-008"], "bloqueo_report_layer_incompleto")

    def test_report_layer_never_replaces_permission_or_level_c(self) -> None:
        report = ao_doc04_wide_tests.build_report()
        relation = report["report_layer_relation"]

        self.assertIn("permiso", relation["no_sustituye"])
        self.assertIn("Nivel_C", relation["no_sustituye"])
        self.assertFalse(report["scope_guard"]["autoriza_transformacion"])


if __name__ == "__main__":
    unittest.main()
