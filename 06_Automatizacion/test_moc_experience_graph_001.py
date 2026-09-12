import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moc_experience_graph_001


class MOCExperienceGraph001Tests(unittest.TestCase):
    def test_default_suite_passes_without_authorizing_global_flags(self) -> None:
        report = moc_experience_graph_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertEqual(report["summary"]["cases"], 16)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertEqual(report["summary"]["operator_traces"], 16)
        self.assertFalse(report["transformacion_permitida"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["global_equivalence_authorized"])
        self.assertFalse(report["global_confluence_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertFalse(report["r4_gamma_global_export_authorized"])
        self.assertFalse(report["scope_guard"]["admite_h_xi"])
        self.assertFalse(report["scope_guard"]["uso_clinico"])
        self.assertEqual(report["source_evidence"], ["external:MOC-GEO-METR-001"])
        self.assertEqual(report["source_provenance"]["document_id"], "MOC-GEO-METR-001")
        self.assertEqual(report["source_provenance"]["location_policy"], "logical_identifier_only")
        self.assertFalse(report["source_provenance"]["runtime_dependency"])

    def test_outputs_cover_imported_cases_036_to_043(self) -> None:
        report = moc_experience_graph_001.build_report()
        outputs = set(report["summary"]["by_output"])

        self.assertIn("concordancia_local", outputs)
        self.assertIn("friccion_relevante", outputs)
        self.assertIn("discordancia_local", outputs)
        self.assertIn("reorganizacion_local_habilitada", outputs)
        self.assertIn("disolucion_local", outputs)
        self.assertIn("fuera_de_alcance", outputs)

    def test_rules_apply_to_boundary_cases(self) -> None:
        report = moc_experience_graph_001.build_report()
        cases = {result["external_case"]: result for result in report["results"]}

        self.assertEqual(cases["038B"]["rule_id"], "G2-MINIMOS-GEOMETRICOS")
        self.assertEqual(cases["037A"]["rule_id"], "G3-DISCORDANCIA-DIRECCION")
        self.assertEqual(cases["040B"]["rule_id"], "G4-EXPECTATIVA-FIJA")
        self.assertEqual(cases["042B"]["rule_id"], "G0-ALCANCE")
        self.assertEqual(cases["043A"]["rule_id"], "G5-REORGANIZACION-LOCAL")

    def test_ao_bridge_uses_operator_trace_without_closure(self) -> None:
        report = moc_experience_graph_001.build_report()

        for result in report["results"]:
            self.assertEqual(result["operator_trace"]["operator_id"], "OP_MOC_GEO_GRAPH")
            self.assertFalse(result["ao_bridge"]["closes_equivalence_global"])
            self.assertFalse(result["ao_bridge"]["closes_confluence_global"])
            self.assertFalse(result["ao_bridge"]["modifies_doc04"])
            self.assertFalse(result["ao_bridge"]["transformacion_permitida"])

    def test_graph_template_contains_required_minimum(self) -> None:
        suite = moc_experience_graph_001.load_suite()
        valid, blockers, warnings = moc_experience_graph_001._graph_validation(suite)

        self.assertTrue(valid)
        self.assertEqual(blockers, ())
        self.assertEqual(warnings, ())


if __name__ == "__main__":
    unittest.main()
