"""Geometria euclidea para esferas exteriores de radio unitario.

Las funciones producen cantidades geometricas; no deciden optimalidad global ni
rigidez mecanica. Las convenciones se documentan en INFORME_MATEMATICO_INICIAL.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import asin
from typing import Iterable

import numpy as np

TOLERANCE = 1e-9


@dataclass(frozen=True)
class PairClearance:
    i: int
    j: int
    distance: float
    clearance: float
    relation: str


def as_points(points: Iterable[Iterable[float]]) -> np.ndarray:
    array = np.asarray(list(points), dtype=float)
    if array.ndim != 2 or array.shape[1] != 3:
        raise ValueError("Se esperan puntos finitos de R^3 con forma (n, 3).")
    if len(array) < 2:
        raise ValueError("Se requieren al menos dos centros exteriores.")
    return array


def normalize_rows(points: Iterable[Iterable[float]]) -> np.ndarray:
    array = as_points(points)
    norms = np.linalg.norm(array, axis=1)
    if np.any(norms <= TOLERANCE):
        raise ValueError("No se puede normalizar un vector nulo.")
    return array / norms[:, None]


def pairwise_distances(points: Iterable[Iterable[float]]) -> np.ndarray:
    array = as_points(points)
    delta = array[:, None, :] - array[None, :, :]
    return np.linalg.norm(delta, axis=2)


def minimum_pair_distance(points: Iterable[Iterable[float]]) -> float:
    distances = pairwise_distances(points)
    np.fill_diagonal(distances, np.inf)
    return float(np.min(distances))


def epsilon_threshold(unit_directions: Iterable[Iterable[float]]) -> float:
    """Infimo epsilon para que las exteriores unitarias no se solapen.

    Si d_min es la menor cuerda entre direcciones unitarias, la condicion es
    (1+epsilon) d_min >= 2, por lo que epsilon_* = max(0, 2/d_min - 1).
    """
    directions = normalize_rows(unit_directions)
    d_min = minimum_pair_distance(directions)
    return max(0.0, 2.0 / d_min - 1.0)


def angular_lower_bound(epsilon: float) -> float:
    if epsilon <= 0:
        raise ValueError("El modelo de esfera central requiere epsilon > 0.")
    return 2.0 * asin(1.0 / (1.0 + epsilon))


def scaled_centers(unit_directions: Iterable[Iterable[float]], epsilon: float) -> np.ndarray:
    if epsilon <= 0:
        raise ValueError("epsilon debe ser estrictamente positivo al materializar C_n.")
    return normalize_rows(unit_directions) * (1.0 + epsilon)


def clearance(distance: float, r_i: float = 1.0, r_j: float = 1.0) -> float:
    return distance - (r_i + r_j)


def relation_from_clearance(value: float, tolerance: float = TOLERANCE) -> str:
    if value > tolerance:
        return "SEPARACION"
    if value < -tolerance:
        return "SOLAPAMIENTO_FISICO"
    return "TANGENCIA_EXACTA"


def clearance_pairs(points: Iterable[Iterable[float]], outer_radius: float = 1.0) -> list[PairClearance]:
    array = as_points(points)
    reports: list[PairClearance] = []
    for i, j in combinations(range(len(array)), 2):
        distance = float(np.linalg.norm(array[i] - array[j]))
        value = clearance(distance, outer_radius, outer_radius)
        reports.append(PairClearance(i, j, distance, value, relation_from_clearance(value)))
    return reports


def centeredness(points: Iterable[Iterable[float]]) -> dict[str, object]:
    """Chequeos suficientes, no un solucionador general de envolvente convexa.

    El origen es el baricentro de los conjuntos simetricos incluidos. Se informa
    rango affine para distinguir inclusion debil del origen y centralidad 3D.
    """
    array = as_points(points)
    centroid = np.mean(array, axis=0)
    affine_rank = int(np.linalg.matrix_rank(array - centroid, tol=TOLERANCE))
    centroid_at_origin = bool(np.linalg.norm(centroid) <= TOLERANCE)
    return {
        "centroid_at_origin": centroid_at_origin,
        "affine_rank": affine_rank,
        "centeredness_claim": (
            "CENTERED_FULL_DIMENSIONAL_BY_EQUAL_WEIGHT_CERTIFICATE"
            if centroid_at_origin and affine_rank == 3
            else "CENTERED_WEAK_OR_UNCERTIFIED"
        ),
    }


def configuration_report(name: str, unit_directions: Iterable[Iterable[float]]) -> dict[str, object]:
    directions = normalize_rows(unit_directions)
    threshold = epsilon_threshold(directions)
    report = {
        "name": name,
        "n": int(len(directions)),
        "minimum_unit_chord": minimum_pair_distance(directions),
        "epsilon_infimum": threshold,
        "epsilon_realization_example": threshold + 1e-6,
        "contact_pair_count_at_infimum": sum(
            1
            for item in clearance_pairs(directions * (1.0 + threshold))
            if item.relation == "TANGENCIA_EXACTA"
        ),
    }
    report.update(centeredness(directions))
    return report
