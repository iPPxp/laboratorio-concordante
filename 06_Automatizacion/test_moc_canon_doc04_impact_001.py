import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moc_canon_doc04_impact_001 as impact


class MocCanonDoc04Impact001Tests(unittest.TestCase):
    def test_default_matrix_accepts_candidate_only(self):
        report = impact.build_report()
        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["impact_matrix_accepted"])
        self.assertTrue(report["candidate_proposal_prepared"])
        self.assertFalse(report["official_canon_edit_authorized"])
        self.assertFalse(report["official_doc04_edit_authorized"])
        self.assertFalse(report["transformacion_permitida"])

    def test_m000_has_no_text_change_recommended(self):
        report = impact.build_report()
        self.assertFalse(report["m000_text_change_recommended"])
        self.assertIn("M000", report["result"]["surfaces"])

    def test_m001_and_doc04_are_candidate_amendments(self):
        report = impact.build_report()
        self.assertTrue(report["m001_candidate_amendment_recommended"])
        self.assertTrue(report["doc04_candidate_amendment_recommended"])

    def test_forbidden_rows_must_reject(self):
        matrix = impact.load_matrix()
        matrix["rows"] = [
            {
                "id": "BAD-PROH",
                "surface": "PROHIBIDO",
                "target": "H-Xi",
                "candidate_action": "propuesta_candidata",
                "official_edit_authorized": False,
            }
        ]
        matrix["required_surfaces"] = ["PROHIBIDO"]
        result = impact.evaluate_matrix(matrix)
        self.assertFalse(result["passed"])
        self.assertIn("prohibido_no_rechazado:BAD-PROH", result["blockers"])

    def test_official_edit_blocks(self):
        matrix = impact.load_matrix()
        matrix["rows"][0]["official_edit_authorized"] = True
        result = impact.evaluate_matrix(matrix)
        self.assertFalse(result["passed"])
        self.assertIn("edicion_oficial_en_fila:MOC-IMPACT-M000-001", result["blockers"])


if __name__ == "__main__":
    unittest.main()
