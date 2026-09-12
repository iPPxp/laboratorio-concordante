import math
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.configurations import antipodal_pair, regular_octahedron, regular_tetrahedron
from spherepack.geometry import (
    angular_lower_bound,
    epsilon_threshold,
    minimum_pair_distance,
    scaled_centers,
)


class GeometryTests(unittest.TestCase):
    def test_antipodal_infimum_is_zero(self):
        self.assertAlmostEqual(epsilon_threshold(antipodal_pair()), 0.0, places=12)

    def test_tiny_positive_center_between_two_has_twice_its_radius_as_gap(self):
        for epsilon in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6):
            centers = scaled_centers(antipodal_pair(), epsilon)
            host_distance = minimum_pair_distance(centers)
            self.assertAlmostEqual(host_distance, 2.0 * (1.0 + epsilon), places=12)
            self.assertAlmostEqual(host_distance - 2.0, 2.0 * epsilon, places=12)

    def test_tetrahedron_threshold(self):
        self.assertAlmostEqual(epsilon_threshold(regular_tetrahedron()), math.sqrt(3 / 2) - 1, places=12)

    def test_octahedron_threshold(self):
        self.assertAlmostEqual(epsilon_threshold(regular_octahedron()), math.sqrt(2) - 1, places=12)

    def test_scaled_octahedron_has_no_overlap_above_threshold(self):
        centers = scaled_centers(regular_octahedron(), math.sqrt(2) - 1 + 1e-6)
        distances = [math.dist(a, b) for position, a in enumerate(centers) for b in centers[position + 1:]]
        self.assertGreaterEqual(min(distances), 2.0)

    def test_angular_bound_is_defined_for_positive_epsilon(self):
        bound = angular_lower_bound(0.2)
        self.assertGreater(bound, 0)
        self.assertLess(bound, math.pi)


if __name__ == "__main__":
    unittest.main()
