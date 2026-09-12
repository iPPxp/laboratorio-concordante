"""Modelo reproducible y acotado para configuraciones esfericas centradas."""

from .configurations import named_configurations, regular_4_simplex, regular_simplex, twenty_four_cell
from .geometry import configuration_report, contact_edges, epsilon_threshold, simple_graph_invariants

__all__ = [
    "named_configurations",
    "regular_simplex",
    "regular_4_simplex",
    "twenty_four_cell",
    "configuration_report",
    "contact_edges",
    "simple_graph_invariants",
    "epsilon_threshold",
]
