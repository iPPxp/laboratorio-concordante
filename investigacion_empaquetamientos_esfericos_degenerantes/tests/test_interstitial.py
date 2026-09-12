import math
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.interstitial import (
    cyclic_tangent_ring_report,
    descartes_inner_curvature,
    descartes_inner_radius,
    descartes_reflection,
    octahedral_gap_ratio,
    regular_ring_gap_ratio,
    simplex_gap_ratio,
    solve_central_gap_radius,
    tangent_central_angle,
)


class InterstitialTests(unittest.TestCase):
    def test_three_equal_circles_have_small_descartes_center(self):
        expected = 2.0 / math.sqrt(3.0) - 1.0
        self.assertAlmostEqual(regular_ring_gap_ratio(3), expected, places=12)
        self.assertAlmostEqual(descartes_inner_radius((1.0, 1.0, 1.0)), expected, places=12)

    def test_four_equal_circles_have_square_center(self):
        self.assertAlmostEqual(regular_ring_gap_ratio(4), math.sqrt(2.0) - 1.0, places=12)

    def test_six_equal_circles_have_equal_center(self):
        self.assertAlmostEqual(regular_ring_gap_ratio(6), 1.0, places=12)

    def test_cyclic_solver_recovers_regular_formulas(self):
        for n in range(3, 9):
            solved = solve_central_gap_radius([1.0] * n)
            self.assertAlmostEqual(solved, regular_ring_gap_ratio(n), places=10)

    def test_cyclic_solver_is_invariant_at_extreme_scales(self):
        expected_ratio = regular_ring_gap_ratio(3)
        for scale in (1e-200, 1e200):
            solved = solve_central_gap_radius([scale] * 3)
            self.assertTrue(math.isfinite(solved))
            self.assertAlmostEqual(solved / scale, expected_ratio, places=10)

    def test_tangent_angle_avoids_overflow_near_float_limit(self):
        self.assertAlmostEqual(
            tangent_central_angle(1e308, 1e308, 1e308),
            math.pi / 3.0,
            places=12,
        )

    def test_unequal_ring_checks_non_neighbour_overlap(self):
        report = cyclic_tangent_ring_report((1.0, 0.6, 1.4, 0.8))
        self.assertAlmostEqual(report["angle_sum"], 2.0 * math.pi, places=10)
        self.assertTrue(report["non_overlapping"])

    def test_descartes_reflection_generates_child_gap(self):
        inner = descartes_inner_curvature((1.0, 1.0, 1.0))
        reflected = descartes_reflection((1.0, 1.0, 1.0, inner), 0)
        self.assertGreater(reflected[0], inner)
        self.assertEqual(reflected[1:], (1.0, 1.0, inner))

    def test_simplex_formula_connects_triangle_and_tetrahedron(self):
        self.assertAlmostEqual(simplex_gap_ratio(2), regular_ring_gap_ratio(3), places=12)
        self.assertAlmostEqual(simplex_gap_ratio(3), math.sqrt(3.0 / 2.0) - 1.0, places=12)

    def test_square_and_octahedron_share_ratio_not_contact_graph(self):
        self.assertAlmostEqual(regular_ring_gap_ratio(4), octahedral_gap_ratio(), places=12)


if __name__ == "__main__":
    unittest.main()
