import math
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

import numpy as np

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.configurations import (
    antipodal_pair,
    named_configurations,
    regular_4_simplex,
    regular_octahedron,
    regular_simplex,
    regular_tetrahedron,
    twenty_four_cell,
)
from spherepack.geometry import (
    as_points,
    configuration_report,
    contact_edges,
    epsilon_threshold,
    normalize_rows,
)
from spherepack.interstitial import simplex_gap_ratio
from spherepack.transitions import direction_subset
from spherepack.visualization import write_interactive_html, write_shell_svg


class DimensionAgnosticGeometryTests(unittest.TestCase):
    def test_normalization_is_stable_for_extreme_finite_scales(self):
        expected = np.asarray(((1.0, 0.0), (0.0, -1.0)))
        for scale in (1e-200, 1e200, 1e308):
            np.testing.assert_allclose(normalize_rows(expected * scale), expected, atol=1e-15)
            self.assertAlmostEqual(epsilon_threshold(expected * scale), math.sqrt(2.0) - 1.0)

    def test_antipodal_epsilon_zero_is_typed_as_degenerate_limit(self):
        report = configuration_report("n2_antipodal", antipodal_pair())
        self.assertEqual(report["epsilon_infimum"], 0.0)
        self.assertEqual(report["central_radius_at_infimum"], 0.0)
        self.assertEqual(
            report["central_object_status_at_infimum"],
            "DEGENERATE_ZERO_RADIUS_LIMIT",
        )
        self.assertEqual(report["outer_contact_graph_at_infimum"]["edge_count"], 1)
        centered_graph = report["centered_contact_graph_at_infimum"]
        self.assertEqual(centered_graph["central_vertex_status"], "DEGENERATE_ZERO_RADIUS_LIMIT")
        self.assertEqual(centered_graph["edge_count"], 3)

    def test_regular_4_simplex_has_exact_gram_contract_and_k5_contacts(self):
        points = regular_4_simplex()
        self.assertEqual(points.shape, (5, 4))
        gram = points @ points.T
        np.testing.assert_allclose(np.diag(gram), np.ones(5), atol=1e-12)
        np.testing.assert_allclose(
            gram - np.eye(5),
            (np.ones((5, 5)) - np.eye(5)) * -0.25,
            atol=1e-12,
        )
        np.testing.assert_allclose(np.mean(points, axis=0), np.zeros(4), atol=1e-12)
        np.testing.assert_allclose(points.T @ points, np.eye(4) * 1.25, atol=1e-12)

        report = configuration_report("n5_4_simplex", points)
        self.assertEqual(report["ambient_dimension"], 4)
        self.assertEqual(report["affine_rank"], 4)
        self.assertEqual(
            report["centeredness_claim"],
            "CENTERED_FULL_DIMENSIONAL_BY_EQUAL_WEIGHT_CERTIFICATE",
        )
        self.assertAlmostEqual(report["minimum_unit_chord"], math.sqrt(5.0 / 2.0), places=12)
        self.assertAlmostEqual(report["epsilon_infimum"], math.sqrt(8.0 / 5.0) - 1.0, places=12)
        self.assertAlmostEqual(report["epsilon_infimum"], simplex_gap_ratio(4), places=12)
        self.assertEqual(report["central_object_status_at_infimum"], "POSITIVE_RADIUS_CENTRAL_SPHERE")
        self.assertEqual(report["contact_pair_count_at_infimum"], 10)
        self.assertEqual(report["central_contact_count_at_infimum"], 5)

        outer_graph = report["outer_contact_graph_at_infimum"]
        self.assertEqual(outer_graph["edge_count"], 10)
        self.assertEqual(outer_graph["degree_multiset"], [4] * 5)
        self.assertEqual(outer_graph["regular_degree"], 4)
        self.assertEqual(outer_graph["triangle_count"], 10)
        self.assertEqual(outer_graph["diameter"], 1)
        self.assertEqual(outer_graph["cycle_rank_beta1"], 6)
        self.assertTrue(outer_graph["is_complete"])

        centered_graph = report["centered_contact_graph_at_infimum"]
        self.assertEqual(centered_graph["central_vertex"], 5)
        self.assertEqual(centered_graph["edge_count"], 15)
        self.assertEqual(centered_graph["degree_multiset"], [5] * 6)
        self.assertTrue(centered_graph["is_complete"])

    def test_general_simplex_constructor_retains_tetrahedral_contract(self):
        simplex = regular_simplex(3)
        tetrahedron = regular_tetrahedron()
        self.assertEqual(simplex.shape, (4, 3))
        self.assertEqual(tetrahedron.shape[1], 3)
        np.testing.assert_allclose(simplex @ simplex.T, tetrahedron @ tetrahedron.T, atol=1e-12)

    def test_24_cell_has_d4_roots_and_expected_inner_product_distribution(self):
        points = twenty_four_cell()
        self.assertEqual(points.shape, (24, 4))
        self.assertEqual(len({tuple(row) for row in points}), 24)
        np.testing.assert_allclose(np.linalg.norm(points, axis=1), np.ones(24), atol=1e-12)
        self.assertTrue(np.all(np.count_nonzero(points, axis=1) == 2))
        np.testing.assert_allclose(
            np.abs(points[np.nonzero(points)]),
            np.full(48, 1.0 / math.sqrt(2.0)),
            atol=1e-12,
        )
        np.testing.assert_allclose(np.mean(points, axis=0), np.zeros(4), atol=1e-12)
        np.testing.assert_allclose(points.T @ points, np.eye(4) * 6.0, atol=1e-12)

        gram = points @ points.T
        products = np.round(gram[np.triu_indices(24, 1)], 12)
        self.assertEqual(
            Counter(products.tolist()),
            Counter({-1.0: 12, -0.5: 96, 0.0: 72, 0.5: 96}),
        )

    def test_24_cell_kissing_shell_contact_graph_invariants(self):
        report = configuration_report("n24_24_cell_kissing_shell", twenty_four_cell())
        self.assertEqual(report["n"], 24)
        self.assertEqual(report["ambient_dimension"], 4)
        self.assertEqual(report["affine_rank"], 4)
        self.assertAlmostEqual(report["minimum_unit_chord"], 1.0, places=12)
        self.assertAlmostEqual(report["epsilon_infimum"], 1.0, places=12)
        self.assertEqual(report["contact_pair_count_at_infimum"], 96)
        self.assertEqual(report["central_contact_count_at_infimum"], 24)

        outer_graph = report["outer_contact_graph_at_infimum"]
        self.assertEqual(outer_graph["vertex_count"], 24)
        self.assertEqual(outer_graph["edge_count"], 96)
        self.assertEqual(outer_graph["degree_multiset"], [8] * 24)
        self.assertEqual(outer_graph["regular_degree"], 8)
        self.assertEqual(outer_graph["component_count"], 1)
        self.assertEqual(outer_graph["diameter"], 3)
        self.assertEqual(outer_graph["triangle_count"], 96)
        self.assertEqual(outer_graph["cycle_rank_beta1"], 73)
        self.assertFalse(outer_graph["is_complete"])

        edges = {tuple(edge) for edge in outer_graph["edge_list"]}
        adjacency = {vertex: set() for vertex in range(24)}
        for left, right in edges:
            adjacency[left].add(right)
            adjacency[right].add(left)
        for left, right in edges:
            self.assertEqual(len(adjacency[left] & adjacency[right]), 3)
        for vertex, neighbours in adjacency.items():
            induced_degrees = {
                neighbour: len(adjacency[neighbour] & neighbours)
                for neighbour in neighbours
            }
            self.assertEqual(len(neighbours), 8, vertex)
            self.assertEqual(sorted(induced_degrees.values()), [3] * 8, vertex)
            self.assertEqual(sum(induced_degrees.values()) // 2, 12, vertex)

        centered_graph = report["centered_contact_graph_at_infimum"]
        self.assertEqual(centered_graph["central_vertex"], 24)
        self.assertEqual(centered_graph["vertex_count"], 25)
        self.assertEqual(centered_graph["edge_count"], 120)
        self.assertEqual(centered_graph["degree_multiset"], [9] * 24 + [24])
        self.assertEqual(centered_graph["diameter"], 2)
        self.assertEqual(centered_graph["triangle_count"], 192)

    def test_24_cell_contact_graph_is_invariant_under_extreme_radius_scales(self):
        directions = twenty_four_cell()
        for outer_radius in (1e-200, 1.0, 1e200):
            centers = directions * (2.0 * outer_radius)
            self.assertEqual(
                len(contact_edges(centers, outer_radius=outer_radius)),
                96,
            )

    def test_named_catalog_adds_4d_cases_without_removing_3d_cases(self):
        configurations = named_configurations()
        self.assertEqual(configurations["n5_4_simplex"].shape, (5, 4))
        self.assertEqual(configurations["n24_24_cell_kissing_shell"].shape, (24, 4))
        self.assertEqual(configurations["n6_octahedron"].shape, (6, 3))
        report = configuration_report("n6_octahedron", configurations["n6_octahedron"])
        self.assertEqual(report["ambient_dimension"], 3)
        self.assertEqual(report["affine_rank"], 3)
        self.assertEqual(report["contact_pair_count_at_infimum"], 12)

    def test_points_are_dimension_agnostic_but_transitions_require_same_dimension(self):
        self.assertEqual(as_points(((1.0, 0.0), (-1.0, 0.0))).shape, (2, 2))
        with self.assertRaisesRegex(ValueError, "mismo R\\^d"):
            direction_subset(regular_octahedron(), regular_4_simplex())

    def test_3d_visualizers_reject_4d_without_silent_coordinate_loss(self):
        points = twenty_four_cell()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "r4.svg"
            with self.assertRaisesRegex(ValueError, "solo R\\^3"):
                write_shell_svg(target, "24-cell", points)
            self.assertFalse(target.exists())

            target = Path(directory) / "r4.html"
            with self.assertRaisesRegex(ValueError, "solo R\\^3"):
                write_interactive_html(target, "24-cell", {"r4": points})
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
