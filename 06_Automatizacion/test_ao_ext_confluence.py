import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_ext_confluence


class AOExtConfluenceTests(unittest.TestCase):
    def test_external_confluence_cases_pass_without_transforming(self) -> None:
        report = ao_ext_confluence.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 7)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertEqual(report["tests_executed"], ["EXT-CONF-001", "EXT-CONF-002"])
        self.assertFalse(report["scope_guard"]["modifica_doc04"])
        self.assertFalse(report["scope_guard"]["cierra_confluencia_global"])
        self.assertFalse(report["scope_guard"]["cierra_equivalencia_global"])
        self.assertTrue(report["debt_guard"]["maduracion_tcs_abierta"])

    def test_ext_conf_001_has_positive_blocking_and_divergent_cases(self) -> None:
        report = ao_ext_confluence.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["EXT-CONF-001A"], "confluencia_local")
        self.assertEqual(outcomes["EXT-CONF-001B"], "bloqueo_por_testigo")
        self.assertEqual(outcomes["EXT-CONF-001C"], "equivalencia_bajo_testigo")
        self.assertEqual(outcomes["EXT-CONF-001D"], "divergencia_clasificada")

    def test_second_external_test_is_non_regulated_package_case(self) -> None:
        report = ao_ext_confluence.build_report()
        ext_conf_002 = [result for result in report["results"] if result["test_id"] == "EXT-CONF-002"]

        self.assertEqual(len(ext_conf_002), 3)
        self.assertEqual({result["domain"] for result in ext_conf_002}, {"paquete_software_juguete"})
        self.assertTrue(all(result["passed"] for result in ext_conf_002))


if __name__ == "__main__":
    unittest.main()
