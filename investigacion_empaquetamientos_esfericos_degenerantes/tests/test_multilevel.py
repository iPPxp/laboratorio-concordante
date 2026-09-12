import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.multilevel import (
    Cell,
    ProjectedSegment,
    all_matchings,
    architecture_edges,
    complete_edges,
    graph_invariants,
    is_single_cycle,
    projected_intersection_kind,
    star_refinement_delta,
    star_refine,
    triad_nodes,
)


class MultilevelTests(unittest.TestCase):
    def test_exactly_six_labelled_matchings(self):
        self.assertEqual(len(all_matchings()), 6)
        self.assertEqual(len(set(all_matchings())), 6)

    def test_prism_and_octahedron_partition_cross_edges(self):
        nodes = triad_nodes("H") + triad_nodes("A")
        for permutation in all_matchings():
            components = architecture_edges(permutation)
            self.assertEqual(len(components["matching"]), 3)
            self.assertEqual(len(components["cross_cycle"]), 6)
            self.assertTrue(is_single_cycle(nodes, components["cross_cycle"]))
            self.assertEqual(components["prism"] & components["octahedron"], components["internal_triads"])
            self.assertEqual(components["prism"] | components["octahedron"], complete_edges(nodes))

    def test_prism_and_octahedron_degree_sequences(self):
        components = architecture_edges((0, 1, 2))
        nodes = triad_nodes("H") + triad_nodes("A")
        for node in nodes:
            prism_degree = sum(node in pair for pair in components["prism"])
            octahedron_degree = sum(node in pair for pair in components["octahedron"])
            self.assertEqual(prism_degree, 3)
            self.assertEqual(octahedron_degree, 4)

    def test_prism_and_octahedron_cycle_invariants(self):
        components = architecture_edges((0, 1, 2))
        nodes = triad_nodes("H") + triad_nodes("A")
        prism = graph_invariants(nodes, components["prism"])
        octahedron = graph_invariants(nodes, components["octahedron"])
        self.assertEqual(prism["cycle_rank_beta1"], 4)
        self.assertEqual(prism["simple_cycle_counts"], {"3": 2, "4": 3, "5": 6, "6": 3})
        self.assertEqual(octahedron["cycle_rank_beta1"], 7)
        self.assertEqual(octahedron["simple_cycle_counts"], {"3": 8, "4": 15, "5": 24, "6": 16})

    def test_triangle_and_square_refine_at_next_level(self):
        triangle = star_refine(Cell("triangle", 0, ("a", "b", "c")), "g3")
        square = star_refine(Cell("square", 0, ("a", "b", "c", "d")), "g4")
        self.assertEqual(len(triangle.children), 3)
        self.assertEqual(len(square.children), 4)
        self.assertTrue(all(child.kind == "F3" and child.level == 1 for child in triangle.children))
        self.assertTrue(all(child.kind == "F3" and child.level == 1 for child in square.children))
        self.assertEqual(square.parent.kind, "F4")
        self.assertIn("CENTRO_DE_CELDA_PADRE", square.roles[0])
        self.assertIn("VERTICE_DE_FRONTERA_DE_CELDAS_HIJAS", square.roles[1])
        self.assertEqual(star_refinement_delta(3), (1, 3, 2))
        self.assertEqual(star_refinement_delta(4), (1, 4, 3))

    def test_visual_crossing_is_not_promoted_to_vertex(self):
        first = ProjectedSegment("h", "triangular", "h0", "h1", (-1.0, -1.0), (1.0, 1.0))
        second = ProjectedSegment("a", "quadrangular", "a0", "a1", (-1.0, 1.0), (1.0, -1.0))
        self.assertEqual(
            projected_intersection_kind(first, second),
            "CRUCE_DE_PROYECCION_NO_VERTICE",
        )

    def test_visual_crossing_is_invariant_under_scale(self):
        for scale in (1e-100, 1e-6, 1.0, 1e100):
            first = ProjectedSegment(
                "h", "triangular", "h0", "h1",
                (-scale, -scale), (scale, scale),
            )
            second = ProjectedSegment(
                "a", "quadrangular", "a0", "a1",
                (-scale, scale), (scale, -scale),
            )
            self.assertEqual(
                projected_intersection_kind(first, second),
                "CRUCE_DE_PROYECCION_NO_VERTICE",
            )

    def test_shared_endpoint_is_a_declared_vertex(self):
        first = ProjectedSegment("h", "triangular", "x", "h1", (0.0, 0.0), (1.0, 0.0))
        second = ProjectedSegment("a", "quadrangular", "x", "a1", (0.0, 0.0), (0.0, 1.0))
        self.assertEqual(projected_intersection_kind(first, second), "VERTICE_COMPARTIDO")


if __name__ == "__main__":
    unittest.main()
