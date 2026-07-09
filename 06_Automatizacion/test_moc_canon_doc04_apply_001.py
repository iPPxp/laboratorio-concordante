import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moc_canon_doc04_apply_001 as apply_check


class MocCanonDoc04Apply001Tests(unittest.TestCase):
    def test_default_application_is_verified(self):
        report = apply_check.build_report(root=Path.cwd())
        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["official_application_verified"])
        self.assertTrue(report["official_application_executed"])
        self.assertFalse(report["m000_text_changed"])
        self.assertTrue(report["m001_official_section_added"])
        self.assertTrue(report["doc04_official_section_added"])
        self.assertFalse(report["transformacion_permitida"])

    def test_mutating_mode_blocks(self):
        data = apply_check.load_application()
        data["flags"]["mutating_mode_authorized"] = True
        result = apply_check.evaluate_application(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertIn("flag_prohibido_activo:mutating_mode_authorized", result["blockers"])

    def test_m000_text_change_blocks(self):
        data = apply_check.load_application()
        data["flags"]["m000_text_changed"] = True
        result = apply_check.evaluate_application(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertIn("flag_prohibido_activo:m000_text_changed", result["blockers"])

    def test_required_marker_missing_blocks(self):
        data = apply_check.load_application()
        for surface in data["official_surfaces"]:
            if surface["surface"] == "M001":
                surface["required_markers"].append("MARCADOR_INEXISTENTE_MOC_APPLY")
        result = apply_check.evaluate_application(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertTrue(any(item.startswith("marcador_ausente:M001") for item in result["blockers"]))

    def test_forbidden_term_in_doc04_section_blocks(self):
        data = apply_check.load_application()
        for surface in data["official_surfaces"]:
            if surface["surface"] == "DOC04":
                surface["section_forbidden_terms"].append("operator_trace_graph")
        result = apply_check.evaluate_application(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertIn("termino_prohibido_en_seccion:DOC04:operator_trace_graph", result["blockers"])


if __name__ == "__main__":
    unittest.main()
