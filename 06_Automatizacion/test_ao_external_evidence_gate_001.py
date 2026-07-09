import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_external_evidence_gate_001


class AOExternalEvidenceGate001Tests(unittest.TestCase):
    def test_default_suite_prepares_gate_without_authorizing_global_closure(self):
        report = ao_external_evidence_gate_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["external_evidence_ready"])
        self.assertFalse(report["external_evidence_executed"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_equivalence_authorized"])
        self.assertFalse(report["global_confluence_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertFalse(report["r4_gamma_global_export_authorized"])
        self.assertEqual(report["summary"]["manifests"], 5)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertEqual(report["summary"]["pending_real_source"], 1)
        self.assertEqual(report["summary"]["rejected_domain"], 1)
        self.assertEqual(report["summary"]["rejected_authority"], 1)
        self.assertEqual(report["summary"]["rejected_scope"], 1)
        self.assertEqual(report["summary"]["admissible_preliminary"], 1)

    def test_real_external_manifest_suite_is_ready_but_does_not_authorize_global_closure(self):
        case_file = Path(__file__).resolve().parent / "fixtures" / "ao_external_evidence_real_001_manifests.json"
        report = ao_external_evidence_gate_001.build_report(case_file=case_file)

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["external_evidence_ready"])
        self.assertFalse(report["external_evidence_executed"])
        self.assertEqual(report["recomendacion"], "solicitar_decision_global_posterior")
        self.assertEqual(report["summary"]["manifests"], 2)
        self.assertEqual(report["summary"]["admissible_real_non_control"], 2)
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_equivalence_authorized"])
        self.assertFalse(report["global_confluence_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertFalse(report["r4_gamma_global_export_authorized"])

    def test_valid_manifest_without_real_source_is_pending(self):
        result = ao_external_evidence_gate_001.evaluate_manifest(
            {
                "manifest_id": "T",
                "artifact_type": "registro_politicas",
                "source_family": "externa_pendiente",
                "real_external_source": False,
                "source_identifiable": True,
                "comparable_unit_present": True,
                "witness_present": True,
                "restrictions": ["no_regulado"],
                "authority": "documental_externa_identificada",
                "traceability_present": True,
                "expected": "pendiente_fuente_real",
            }
        )

        self.assertEqual(result.actual, "pendiente_fuente_real")
        self.assertTrue(result.passed)

    def test_clinical_or_regulated_manifest_is_rejected(self):
        result = ao_external_evidence_gate_001.evaluate_manifest(
            {
                "manifest_id": "T",
                "artifact_type": "registro_clinico",
                "source_family": "dominio_no_autorizado",
                "real_external_source": True,
                "source_identifiable": True,
                "comparable_unit_present": True,
                "witness_present": True,
                "restrictions": ["no_uso"],
                "authority": "documental_externa_identificada",
                "traceability_present": True,
                "clinical_domain": True,
                "regulated_domain": True,
                "expected": "rechazada_por_dominio",
            }
        )

        self.assertEqual(result.actual, "rechazada_por_dominio")
        self.assertIn("dominio_clinico_no_autorizado", result.blockers)

    def test_historical_direct_authority_is_rejected(self):
        result = ao_external_evidence_gate_001.evaluate_manifest(
            {
                "manifest_id": "T",
                "artifact_type": "extracto_historico",
                "source_family": "historial",
                "real_external_source": True,
                "source_identifiable": True,
                "comparable_unit_present": True,
                "witness_present": True,
                "restrictions": ["solo_trazabilidad"],
                "authority": "registro_historico",
                "traceability_present": True,
                "expected": "rechazada_por_autoridad",
            }
        )

        self.assertEqual(result.actual, "rechazada_por_autoridad")
        self.assertIn("autoridad_historica_directa", result.blockers)

    def test_non_comparable_unit_is_rejected_by_scope(self):
        result = ao_external_evidence_gate_001.evaluate_manifest(
            {
                "manifest_id": "T",
                "artifact_type": "registro_tecnico",
                "source_family": "externa",
                "real_external_source": True,
                "source_identifiable": True,
                "comparable_unit_present": False,
                "witness_present": True,
                "restrictions": ["no_regulado"],
                "authority": "documental_externa_identificada",
                "traceability_present": True,
                "expected": "rechazada_por_alcance",
            }
        )

        self.assertEqual(result.actual, "rechazada_por_alcance")
        self.assertIn("unidad_comparable_ausente", result.blockers)

    def test_complete_control_manifest_can_be_preliminarily_admissible_without_closure(self):
        result = ao_external_evidence_gate_001.evaluate_manifest(
            {
                "manifest_id": "T",
                "artifact_type": "registro_politicas",
                "source_family": "control",
                "source_uri": "urn:control",
                "real_external_source": True,
                "source_identifiable": True,
                "control_manifest": True,
                "comparable_unit_present": True,
                "witness_present": True,
                "restrictions": ["no_regulado"],
                "authority": "documental_externa_identificada",
                "traceability_present": True,
                "expected": "admisible_preliminar",
            }
        )

        self.assertEqual(result.actual, "admisible_preliminar")
        self.assertIn("admisible_solo_como_control_de_compuerta", result.warnings)


if __name__ == "__main__":
    unittest.main()
