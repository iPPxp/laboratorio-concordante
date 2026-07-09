import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moc_canon_doc04_adopt_gate_001 as gate


class MocCanonDoc04AdoptGate001Tests(unittest.TestCase):
    def test_default_gate_is_ready_without_execution(self):
        report = gate.build_report(root=Path.cwd())
        self.assertEqual(report["resultado"], "ok")
        self.assertEqual(report["adoption_gate_result"], "lista_para_aplicacion_posterior")
        self.assertFalse(report["m000_adoption_recommended"])
        self.assertTrue(report["m001_adoption_recommended"])
        self.assertTrue(report["doc04_adoption_recommended"])
        self.assertFalse(report["official_file_edit_executed"])
        self.assertFalse(report["transformacion_permitida"])

    def test_official_edit_execution_blocks(self):
        data = gate.load_gate()
        data["flags"]["official_file_edit_executed"] = True
        result = gate.evaluate_gate(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertIn("flag_prohibido_activo:official_file_edit_executed", result["blockers"])

    def test_m000_adoption_blocks(self):
        data = gate.load_gate()
        data["flags"]["m000_adoption_recommended"] = True
        result = gate.evaluate_gate(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertIn("m000_no_debe_adoptarse", result["blockers"])

    def test_m001_and_doc04_need_explicit_apply_step(self):
        data = gate.load_gate()
        for item in data["surfaces"]:
            if item["surface"] == "DOC04":
                item["requires_explicit_apply_step"] = False
        result = gate.evaluate_gate(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertIn("doc04_sin_paso_explicito", result["blockers"])

    def test_prohibited_surface_must_block(self):
        data = gate.load_gate()
        for item in data["surfaces"]:
            if item["surface"] == "PROHIBIDO":
                item["recommendation"] = "lista_para_aplicacion_posterior"
        result = gate.evaluate_gate(data, Path.cwd())
        self.assertFalse(result["passed"])
        self.assertIn("prohibido_no_bloqueado", result["blockers"])


if __name__ == "__main__":
    unittest.main()
