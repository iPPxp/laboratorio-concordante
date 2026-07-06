import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_ppi_bridge_004


class AOPPIBridge004Tests(unittest.TestCase):
    def test_default_matrix_passes_without_global_closure(self):
        report = ao_ppi_bridge_004.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["global_export_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertEqual(report["summary"]["conditions"], 12)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_recalculated_conditions_keep_global_debts_open(self):
        report = ao_ppi_bridge_004.build_report()
        by_id = {item["condition_id"]: item for item in report["condition_results"]}

        self.assertEqual(by_id["AO-PPI-GC-004"]["status"], "satisfecha_local")
        self.assertEqual(by_id["AO-PPI-GC-005"]["status"], "parcial_local")
        self.assertEqual(by_id["AO-PPI-GC-006"]["status"], "parcial_local")
        self.assertEqual(by_id["AO-PPI-GC-007"]["status"], "satisfecha_local")
        self.assertEqual(by_id["AO-PPI-GC-010"]["status"], "faltante_global")
        self.assertEqual(by_id["AO-PPI-GC-012"]["status"], "faltante_global")
        self.assertEqual(report["summary"]["satisfied_local"], 5)
        self.assertEqual(report["summary"]["partial_local"], 2)
        self.assertEqual(report["summary"]["missing_global"], 2)
        self.assertEqual(report["summary"]["scope_blocked"], 3)

    def test_scope_guard_prevents_promotion_and_reopening(self):
        report = ao_ppi_bridge_004.build_report()
        guard = report["scope_guard"]

        self.assertFalse(guard["modifica_doc04"])
        self.assertFalse(guard["modifica_canon"])
        self.assertFalse(guard["modifica_nivel_c"])
        self.assertFalse(guard["crea_nivel_c"])
        self.assertFalse(guard["reabre_p_pi_0"])
        self.assertFalse(guard["reabre_p_pi_1"])
        self.assertFalse(guard["cierra_confluencia_global"])
        self.assertFalse(guard["cierra_equivalencia_global"])
        self.assertFalse(guard["promueve_report_layer"])
        self.assertFalse(guard["exporta_r4_gamma"])
        self.assertFalse(guard["autoriza_transformacion"])


if __name__ == "__main__":
    unittest.main()
