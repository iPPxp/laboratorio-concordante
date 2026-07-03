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


if __name__ == "__main__":
    unittest.main()
