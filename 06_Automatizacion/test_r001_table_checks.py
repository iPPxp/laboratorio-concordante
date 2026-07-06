import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r001_table_checks


class R001TableChecksTests(unittest.TestCase):
    def test_default_checks_pass_without_transforming(self) -> None:
        report = r001_table_checks.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertFalse(report["transformacion_permitida"])
        self.assertEqual(report["summary"]["checks"], 20)
        self.assertEqual(report["summary"]["failed"], 0)
        self.assertEqual(report["relacion_formal_ao"]["id"], "R001-TB-001")
        self.assertEqual(report["relacion_formal_ao"]["ao_bridge"], "AO-PPI-BRIDGE-001")
        self.assertFalse(report["scope_guard"]["canoniza_xi"])
        self.assertFalse(report["scope_guard"]["admite_h_xi"])
        self.assertFalse(report["scope_guard"]["cierra_p200"])

    def test_p200_depends_on_declared_observations(self) -> None:
        xi_direct, xi_reach = r001_table_checks.build_finite_couplings()

        self.assertEqual(
            r001_table_checks.compare_by_oadm(xi_direct, xi_reach, ["A->B", "B->C"]),
            r001_table_checks.EQUIVALENT,
        )
        self.assertEqual(
            r001_table_checks.compare_by_oadm(xi_direct, xi_reach, ["A=>C"]),
            r001_table_checks.NON_EQUIVALENT,
        )

    def test_decouple_blocks_when_layered_cost_is_not_lower(self) -> None:
        case = r001_table_checks.DecoupleCase(
            case_id="cost_guard",
            omega_stable=True,
            phi_independent=True,
            p000_preserved=True,
            p200_result=r001_table_checks.EQUIVALENT,
            c_xi=3,
            c_pi=1,
            c_r=1,
            c_s=1,
            expected_status=r001_table_checks.BLOCKED_COST,
        )

        self.assertEqual(r001_table_checks.decouple_status(case), r001_table_checks.BLOCKED_COST)


if __name__ == "__main__":
    unittest.main()
