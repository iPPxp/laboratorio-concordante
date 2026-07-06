import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_authority_global_001


class AOAuthorityGlobal001Tests(unittest.TestCase):
    def test_authority_matrix_passes_without_global_authority(self) -> None:
        report = ao_authority_global_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["authority_criterion_local"])
        self.assertFalse(report["global_authority_authorized"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["cases"], 12)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertGreaterEqual(report["summary"]["local_comparable"], 5)

    def test_passive_and_external_evidence_are_not_authority(self) -> None:
        report = ao_authority_global_001.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["AO-AUTH-006"], "evidencia_pasiva_no_autoridad")
        self.assertEqual(outcomes["AO-AUTH-007"], "evidencia_externa_no_autoridad")

    def test_authority_blocks_are_classified(self) -> None:
        report = ao_authority_global_001.build_report()
        outcomes = {result["case_id"]: result["actual"] for result in report["results"]}

        self.assertEqual(outcomes["AO-AUTH-008"], "bloqueo_historial_autoridad")
        self.assertEqual(outcomes["AO-AUTH-009"], "bloqueo_autoridad_por_repeticion")
        self.assertEqual(outcomes["AO-AUTH-010"], "bloqueo_recomendacion_como_decision")
        self.assertEqual(outcomes["AO-AUTH-011"], "bloqueo_autoridad_global_no_declarada")
        self.assertEqual(outcomes["AO-AUTH-012"], "bloqueo_testigo")


if __name__ == "__main__":
    unittest.main()
