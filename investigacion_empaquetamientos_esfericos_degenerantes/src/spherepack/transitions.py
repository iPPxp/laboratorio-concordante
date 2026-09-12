"""Analisis limitado de transiciones entre configuraciones nombradas.

Una respuesta negativa aqui refuta solo la inclusion literal de direcciones en
los representantes canonicos introducidos, no toda posible deformacion ni una
transicion fisica. Este limite es deliberado.
"""

from __future__ import annotations

import numpy as np

from .geometry import TOLERANCE, epsilon_threshold, normalize_rows


def direction_subset(source: np.ndarray, target: np.ndarray, tolerance: float = TOLERANCE) -> bool:
    source = normalize_rows(source)
    target = normalize_rows(target)
    if source.shape[1] != target.shape[1]:
        raise ValueError("source y target deben pertenecer al mismo R^d.")
    return all(any(np.linalg.norm(point - candidate) <= tolerance for candidate in target) for point in source)


def transition_report(source_name: str, source: np.ndarray, target_name: str, target: np.ndarray) -> dict[str, object]:
    source_threshold = epsilon_threshold(source)
    target_threshold = epsilon_threshold(target)
    literal = direction_subset(source, target)
    return {
        "source": source_name,
        "target": target_name,
        "cardinality_delta": int(len(target) - len(source)),
        "source_epsilon_infimum": source_threshold,
        "target_epsilon_infimum": target_threshold,
        "literal_direction_inclusion": literal,
        "preserves_nonoverlap_at_target_infimum": source_threshold <= target_threshold + TOLERANCE,
        "scope": "ONLY_NAMED_REPRESENTATIVES_AND_LITERAL_DIRECTION_INCLUSION",
        "conclusion": (
            "WITNESS_FOR_THIS_REPRESENTATIVE_ONLY"
            if literal and source_threshold <= target_threshold + TOLERANCE
            else "NO_LITERAL_INCLUSION_WITNESS_FOR_THIS_REPRESENTATIVE"
        ),
    }
