import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_ext_cov_001


class AOExtCov001Tests(unittest.TestCase):
    def test_external_coverage_passes_without_global_closure(self) -> None:
        report = ao_ext_cov_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["external_coverage_local"])
        self.assertFalse(report["external_coverage_global"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 8)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertEqual(report["summary"]["coverage_local"], 4)

    def test_external_cases_are_classified(self) -> None:
        report = ao_ext_cov_001.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["AO-EXT-COV-001"], "cobertura_externa_local")
        self.assertEqual(outcomes["AO-EXT-COV-005"], "conflicto_autoridades_clasificado")
        self.assertEqual(outcomes["AO-EXT-COV-006"], "divergencia_clasificada")
        self.assertEqual(outcomes["AO-EXT-COV-007"], "bloqueo_testigo")
        self.assertEqual(outcomes["AO-EXT-COV-008"], "bloqueo_autoridad")

    def test_no_regulated_or_mutant_scope_is_enabled(self) -> None:
        report = ao_ext_cov_001.build_report()

        self.assertFalse(report["scope_guard"]["dominios_regulados"])
        self.assertFalse(report["scope_guard"]["autoriza_transformacion"])
        self.assertFalse(report["scope_guard"]["crea_nivel_c"])
        self.assertFalse(report["scope_guard"]["promueve_report_layer"])


if __name__ == "__main__":
    unittest.main()
