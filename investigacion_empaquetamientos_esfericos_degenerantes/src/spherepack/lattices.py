"""Descripciones declarativas de redes periodicas; no son simulaciones dinamicas."""

from __future__ import annotations

from math import sqrt


def lattice_catalog() -> dict[str, dict[str, object]]:
    a_fcc = 2.0 * sqrt(2.0)
    h = sqrt(8.0 / 3.0)
    return {
        "SC": {
            "kind": "BRAVAIS",
            "basis": [[0.0, 0.0, 0.0]],
            "vectors": [[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]],
            "coordination_number": 6,
            "nearest_shell": "regular_octahedron",
            "packing_fraction": "pi/6",
        },
        "FCC": {
            "kind": "BRAVAIS",
            "basis": [[0.0, 0.0, 0.0]],
            "vectors": [[0.0, a_fcc / 2, a_fcc / 2], [a_fcc / 2, 0.0, a_fcc / 2], [a_fcc / 2, a_fcc / 2, 0.0]],
            "coordination_number": 12,
            "nearest_shell": "cuboctahedron",
            "packing_fraction": "pi/(3*sqrt(2))",
        },
        "HCP": {
            "kind": "PERIODIC_LATTICE_WITH_BASIS_NOT_SIMPLE_BRAVAIS",
            "basis": [[0.0, 0.0, 0.0], [1.0, sqrt(3.0) / 3.0, h]],
            "vectors": [[2.0, 0.0, 0.0], [1.0, sqrt(3.0), 0.0], [0.0, 0.0, 2.0 * h]],
            "coordination_number": 12,
            "nearest_shell": "hcp_neighbour_shell",
            "packing_fraction": "pi/(3*sqrt(2))",
        },
        "BCC": {
            "kind": "BRAVAIS",
            "basis": [[0.0, 0.0, 0.0]],
            "vectors": [[2.0 / sqrt(3.0), 2.0 / sqrt(3.0), -2.0 / sqrt(3.0)], [2.0 / sqrt(3.0), -2.0 / sqrt(3.0), 2.0 / sqrt(3.0)], [-2.0 / sqrt(3.0), 2.0 / sqrt(3.0), 2.0 / sqrt(3.0)]],
            "coordination_number": 8,
            "nearest_shell": "cube",
            "packing_fraction": "sqrt(3)*pi/8",
        },
    }
