import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moc_exp_graph_authorization_gate_001


class MOCExpGraphAuthorizationGate001Tests(unittest.TestCase):
    def test_default_manifest_authorizes_candidate_preparation_only(self) -> None:
        report = moc_exp_graph_authorization_gate_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["autorizacion_interna_preparatoria"])
        self.assertTrue(report["candidate_amendment_preparation_authorized"])
        self.assertFalse(report["official_canon_doc04_edit_authorized"])
        self.assertFalse(report["external_use_authorized"])
        self.assertFalse(report["legal_advice_provided"])
        self.assertTrue(report["requires_external_legal_review_for_publication"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["report_layer_promoted"])

    def test_external_publication_is_rejected(self) -> None:
        manifest = moc_exp_graph_authorization_gate_001.load_manifest()
        manifest["flags"]["external_publication_requested"] = True

        result = moc_exp_graph_authorization_gate_001.evaluate_manifest(manifest)

        self.assertEqual(result["actual"], "rechazo_por_alcance")
        self.assertIn("publicacion_externa_no_autorizada", result["blockers"])

    def test_official_edit_request_is_rejected(self) -> None:
        manifest = moc_exp_graph_authorization_gate_001.load_manifest()
        manifest["flags"]["official_edit_requested"] = True

        result = moc_exp_graph_authorization_gate_001.evaluate_manifest(manifest)

        self.assertEqual(result["actual"], "rechazo_por_autoridad")
        self.assertIn("edicion_oficial_directa_no_autorizada", result["blockers"])

    def test_missing_rights_holder_is_rejected_by_rights(self) -> None:
        manifest = moc_exp_graph_authorization_gate_001.load_manifest()
        manifest["rights_holder"] = ""

        result = moc_exp_graph_authorization_gate_001.evaluate_manifest(manifest)

        self.assertEqual(result["actual"], "rechazo_por_derechos")
        self.assertIn("titularidad_interna_ausente", result["blockers"])


if __name__ == "__main__":
    unittest.main()

