import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_tcs_rel_001


class AOTCSRel001Tests(unittest.TestCase):
    def test_ao_tcs_relation_passes_without_canonizing(self) -> None:
        report = ao_tcs_rel_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["tcs_relation_local"])
        self.assertFalse(report["tcs_canonical"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 10)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertGreaterEqual(report["summary"]["mapped_cases"], 7)

    def test_expected_tcs_mappings_are_present(self) -> None:
        report = ao_tcs_rel_001.build_report()
        mappings = {result["case_id"]: result["actual_tcs_failure"] for result in report["results"]}

        self.assertEqual(mappings["AO-TCS-001"], "TCS-F1")
        self.assertEqual(mappings["AO-TCS-002"], "TCS-F2")
        self.assertEqual(mappings["AO-TCS-003"], "TCS-F9")
        self.assertEqual(mappings["AO-TCS-004"], "TCS-F5")
        self.assertEqual(mappings["AO-TCS-005"], "TCS-F10")
        self.assertEqual(mappings["AO-TCS-007"], "TCS-F7")

    def test_defensive_blocks_are_classified(self) -> None:
        report = ao_tcs_rel_001.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["AO-TCS-006"], "no_comparable_clasificado")
        self.assertEqual(outcomes["AO-TCS-008"], "bloqueo_mapeo_incompleto")
        self.assertEqual(outcomes["AO-TCS-009"], "bloqueo_canonizacion_tcs")
        self.assertEqual(outcomes["AO-TCS-010"], "bloqueo_cierre_global")


if __name__ == "__main__":
    unittest.main()
