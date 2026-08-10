import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.configurations import named_configurations
from spherepack.geometry import configuration_report
from spherepack.transitions import transition_report


class ConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.configurations = named_configurations()

    def test_requested_cardinalities_exist(self):
        counts = {len(points) for points in self.configurations.values()}
        self.assertTrue({2, 4, 6, 12}.issubset(counts))

    def test_fcc_and_hcp_shells_have_twelve_contacts_at_infimum(self):
        for name in ("n12_cuboctahedron_fcc_shell", "n12_hcp_shell"):
            report = configuration_report(name, self.configurations[name])
            self.assertEqual(report["n"], 12)
            self.assertAlmostEqual(report["epsilon_infimum"], 1.0, places=10)
            self.assertEqual(report["centeredness_claim"], "CENTERED_FULL_DIMENSIONAL_BY_EQUAL_WEIGHT_CERTIFICATE")

    def test_square_to_octahedron_is_literal_witness_only(self):
        report = transition_report(
            "square", self.configurations["n4_square_transition_witness"],
            "octa", self.configurations["n6_octahedron"],
        )
        self.assertTrue(report["literal_direction_inclusion"])
        self.assertEqual(report["scope"], "ONLY_NAMED_REPRESENTATIVES_AND_LITERAL_DIRECTION_INCLUSION")

    def test_tetrahedron_is_not_literal_subset_of_octahedron(self):
        report = transition_report(
            "tetra", self.configurations["n4_tetrahedron"], "octa", self.configurations["n6_octahedron"]
        )
        self.assertFalse(report["literal_direction_inclusion"])


if __name__ == "__main__":
    unittest.main()
