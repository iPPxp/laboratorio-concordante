"""Geometria euclidea para esferas exteriores de radio unitario.

Las funciones producen cantidades geometricas; no deciden optimalidad global ni
rigidez mecanica. Las convenciones se documentan en INFORME_MATEMATICO_INICIAL.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import asin, isfinite
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
    if array.ndim != 2 or array.shape[1] < 1:
        raise ValueError("Se esperan puntos de R^d con forma (n, d), d >= 1.")
    if len(array) < 2:
        raise ValueError("Se requieren al menos dos centros exteriores.")
    if not np.all(np.isfinite(array)):
        raise ValueError("Todos los puntos de R^d deben ser finitos.")
    return array


def normalize_rows(points: Iterable[Iterable[float]]) -> np.ndarray:
    array = as_points(points)
    # Escalar fila por fila antes de calcular la norma evita tanto overflow
    # como underflow para vectores finitos extremos sin cambiar su direccion.
    scales = np.max(np.abs(array), axis=1)
    if np.any(scales == 0.0):
        raise ValueError("No se puede normalizar un vector nulo.")
    scaled = array / scales[:, None]
    norms = np.linalg.norm(scaled, axis=1)
    return scaled / norms[:, None]


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
    """Holguras por pares con clasificación relativa al radio exterior.

    Las distancias se comparan primero en unidades de ``outer_radius``. Esto
    conserva el grafo de contacto al cambiar de escala y evita que una
    tolerancia absoluta convierta toda una configuración minúscula en
    tangencias.
    """

    array = as_points(points)
    if not isfinite(outer_radius) or outer_radius <= 0.0:
        raise ValueError("outer_radius debe ser finito y positivo.")
    scaled_array = array / outer_radius
    reports: list[PairClearance] = []
    for i, j in combinations(range(len(array)), 2):
        distance_ratio = float(np.linalg.norm(scaled_array[i] - scaled_array[j]))
        clearance_ratio = distance_ratio - 2.0
        distance = distance_ratio * outer_radius
        value = clearance_ratio * outer_radius
        reports.append(
            PairClearance(
                i,
                j,
                distance,
                value,
                relation_from_clearance(clearance_ratio),
            )
        )
    return reports


def contact_edges(
    points: Iterable[Iterable[float]],
    outer_radius: float = 1.0,
) -> tuple[tuple[int, int], ...]:
    """Aristas de tangencia entre centros ya materializados."""

    return tuple(
        (item.i, item.j)
        for item in clearance_pairs(points, outer_radius)
        if item.relation == "TANGENCIA_EXACTA"
    )


def simple_graph_invariants(
    vertex_count: int,
    edges: Iterable[tuple[int, int]],
) -> dict[str, object]:
    """Invariantes elementales de un grafo simple etiquetado por enteros."""

    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count < 1:
        raise ValueError("vertex_count debe ser un entero positivo.")

    edge_set: set[tuple[int, int]] = set()
    for pair in edges:
        if len(pair) != 2:
            raise ValueError("Cada arista debe tener exactamente dos extremos.")
        left, right = pair
        if not isinstance(left, int) or not isinstance(right, int):
            raise ValueError("Los extremos deben ser indices enteros.")
        if left == right or left not in range(vertex_count) or right not in range(vertex_count):
            raise ValueError("Arista fuera del grafo simple declarado.")
        edge_set.add((min(left, right), max(left, right)))

    adjacency = {vertex: set() for vertex in range(vertex_count)}
    for left, right in edge_set:
        adjacency[left].add(right)
        adjacency[right].add(left)

    component_count = 0
    seen: set[int] = set()
    for start in range(vertex_count):
        if start in seen:
            continue
        component_count += 1
        frontier = [start]
        while frontier:
            vertex = frontier.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            frontier.extend(adjacency[vertex] - seen)

    diameter: int | None = 0 if vertex_count == 1 else None
    if component_count == 1:
        eccentricities: list[int] = []
        for start in range(vertex_count):
            distances = {start: 0}
            frontier = [start]
            for vertex in frontier:
                for neighbour in adjacency[vertex]:
                    if neighbour not in distances:
                        distances[neighbour] = distances[vertex] + 1
                        frontier.append(neighbour)
            eccentricities.append(max(distances.values()))
        diameter = max(eccentricities)

    triangle_count = sum(
        1
        for first, second, third in combinations(range(vertex_count), 3)
        if (
            (min(first, second), max(first, second)) in edge_set
            and (min(first, third), max(first, third)) in edge_set
            and (min(second, third), max(second, third)) in edge_set
        )
    )
    degrees = sorted(len(adjacency[vertex]) for vertex in range(vertex_count))
    regular_degree = degrees[0] if len(set(degrees)) == 1 else None
    return {
        "vertex_count": vertex_count,
        "edge_count": len(edge_set),
        "edge_list": [list(pair) for pair in sorted(edge_set)],
        "component_count": component_count,
        "degree_multiset": degrees,
        "regular_degree": regular_degree,
        "diameter": diameter,
        "triangle_count": triangle_count,
        "cycle_rank_beta1": len(edge_set) - vertex_count + component_count,
        "is_complete": len(edge_set) == vertex_count * (vertex_count - 1) // 2,
    }


def centeredness(points: Iterable[Iterable[float]]) -> dict[str, object]:
    """Chequeos suficientes, no un solucionador general de envolvente convexa.

    El origen es el baricentro de los conjuntos simetricos incluidos. Se informa
    rango afin para distinguir inclusion debil del origen y centralidad en R^d.
    """
    array = as_points(points)
    centroid = np.mean(array, axis=0)
    affine_rank = int(np.linalg.matrix_rank(array - centroid, tol=TOLERANCE))
    ambient_dimension = int(array.shape[1])
    centroid_at_origin = bool(np.linalg.norm(centroid) <= TOLERANCE)
    return {
        "centroid_at_origin": centroid_at_origin,
        "affine_rank": affine_rank,
        "ambient_dimension": ambient_dimension,
        "centeredness_claim": (
            "CENTERED_FULL_DIMENSIONAL_BY_EQUAL_WEIGHT_CERTIFICATE"
            if centroid_at_origin and affine_rank == ambient_dimension
            else "CENTERED_WEAK_OR_UNCERTIFIED"
        ),
    }


def configuration_report(name: str, unit_directions: Iterable[Iterable[float]]) -> dict[str, object]:
    directions = normalize_rows(unit_directions)
    threshold = epsilon_threshold(directions)
    centers_at_infimum = directions * (1.0 + threshold)
    outer_edges = contact_edges(centers_at_infimum)
    outer_graph = simple_graph_invariants(len(directions), outer_edges)
    center_vertex = len(directions)
    centered_edges = outer_edges + tuple((index, center_vertex) for index in range(len(directions)))
    centered_graph = simple_graph_invariants(len(directions) + 1, centered_edges)
    central_object_status = (
        "DEGENERATE_ZERO_RADIUS_LIMIT"
        if threshold == 0.0
        else "POSITIVE_RADIUS_CENTRAL_SPHERE"
    )
    report = {
        "name": name,
        "n": int(len(directions)),
        "minimum_unit_chord": minimum_pair_distance(directions),
        "epsilon_infimum": threshold,
        "central_radius_at_infimum": threshold,
        "central_object_status_at_infimum": central_object_status,
        "epsilon_realization_example": threshold + 1e-6,
        "contact_pair_count_at_infimum": len(outer_edges),
        "central_contact_count_at_infimum": int(len(directions)),
        "outer_contact_graph_at_infimum": outer_graph,
        "centered_contact_graph_at_infimum": {
            "central_vertex": center_vertex,
            "central_vertex_status": central_object_status,
            **centered_graph,
        },
    }
    report.update(centeredness(directions))
    return report
