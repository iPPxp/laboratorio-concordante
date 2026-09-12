"""Geometria exacta de centros intersticiales en anillos y configuraciones de Descartes.

Este modulo separa tres objetos que pueden compartir una imagen, pero no el
mismo contrato: anillos planos de circulos, configuraciones de Descartes y
huecos de esferas en dimension mayor.
"""

from __future__ import annotations

from math import asin, hypot, isfinite, pi, sin, sqrt
from typing import Iterable

import numpy as np

TOLERANCE = 1e-12


def _positive_radius(value: float, name: str) -> float:
    radius = float(value)
    if not isfinite(radius) or radius <= 0:
        raise ValueError(f"{name} debe ser un radio finito y positivo.")
    return radius


def regular_ring_gap_ratio(n: int) -> float:
    """Radio central / radio exterior para un anillo regular de n circulos.

    Los n circulos exteriores son congruentes, cada uno toca al centro y a sus
    dos vecinos ciclicos. El caso n=3 es el hueco triangular; n=4 es el hueco
    cuadrangular; n=6 produce un centro del mismo radio que los exteriores.
    """

    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError("n debe ser un entero mayor o igual que 3.")
    return 1.0 / sin(pi / n) - 1.0


def tangent_central_angle(left_radius: float, right_radius: float, center_radius: float) -> float:
    """Angulo subtendido por dos exteriores consecutivos tangentes.

    Las tres distancias son ``r+R_i``, ``r+R_j`` y ``R_i+R_j``. La formula
    de medio angulo evita restas inestables en la ley de cosenos.
    """

    left = _positive_radius(left_radius, "left_radius")
    right = _positive_radius(right_radius, "right_radius")
    center = _positive_radius(center_radius, "center_radius")
    # Normalizar antes de sumar evita overflow aun cerca del maximo de float.
    scale = max(left, right, center)
    left_scaled = left / scale
    right_scaled = right / scale
    center_scaled = center / scale
    sine_half_squared = (
        left_scaled / (center_scaled + left_scaled)
    ) * (
        right_scaled / (center_scaled + right_scaled)
    )
    sine_half = sqrt(min(1.0, max(0.0, sine_half_squared)))
    return 2.0 * asin(sine_half)


def cyclic_angle_sum(outer_radii: Iterable[float], center_radius: float) -> float:
    radii = tuple(_positive_radius(value, "outer_radius") for value in outer_radii)
    if len(radii) < 3:
        raise ValueError("Se requieren al menos tres circulos exteriores.")
    return sum(
        tangent_central_angle(radii[index], radii[(index + 1) % len(radii)], center_radius)
        for index in range(len(radii))
    )


def solve_central_gap_radius(
    outer_radii: Iterable[float],
    *,
    tolerance: float = TOLERANCE,
    max_iterations: int = 256,
) -> float:
    """Resuelve el radio central de un anillo ciclico tangente.

    Cada exterior toca al centro y a sus dos vecinos. La ecuacion de cierre es
    ``sum(theta_i(r)) = 2*pi``. La solucion se obtiene por biseccion monotona.
    La realizacion completa debe comprobar tambien los pares no vecinos.
    """

    radii = tuple(_positive_radius(value, "outer_radius") for value in outer_radii)
    if len(radii) < 3:
        raise ValueError("Se requieren al menos tres radios exteriores.")
    if tolerance <= 0:
        raise ValueError("tolerance debe ser positiva.")

    # Resolver en unidades del radio mayor hace invariante el algoritmo bajo
    # cambios de escala y mantiene la biseccion en un rango numerico estable.
    scale = max(radii)
    normalized = tuple(radius / scale for radius in radii)
    target = 2.0 * pi
    low = 0.0
    high = 1.0
    while cyclic_angle_sum(normalized, high) > target:
        high *= 2.0

    for _ in range(max_iterations):
        middle = (low + high) / 2.0
        current = cyclic_angle_sum(normalized, middle)
        if abs(current - target) <= tolerance:
            return middle * scale
        if current > target:
            low = middle
        else:
            high = middle
    return ((low + high) / 2.0) * scale


def cyclic_tangent_ring_report(outer_radii: Iterable[float]) -> dict[str, object]:
    """Construye el anillo y audita contactos vecinos y pares no vecinos."""

    radii = tuple(_positive_radius(value, "outer_radius") for value in outer_radii)
    center_radius = solve_central_gap_radius(radii)
    angles = [0.0]
    for index in range(len(radii) - 1):
        angles.append(
            angles[-1]
            + tangent_central_angle(radii[index], radii[index + 1], center_radius)
        )
    centers = np.asarray(
        [
            (
                (center_radius + radius) * np.cos(angle),
                (center_radius + radius) * np.sin(angle),
            )
            for radius, angle in zip(radii, angles, strict=True)
        ],
        dtype=float,
    )

    pair_reports: list[dict[str, object]] = []
    minimum_non_neighbour_clearance: float | None = None
    n = len(radii)
    for left in range(n):
        for right in range(left + 1, n):
            delta = centers[left] - centers[right]
            distance = hypot(float(delta[0]), float(delta[1]))
            gap = distance - (radii[left] + radii[right])
            neighbours = (right == left + 1) or (left == 0 and right == n - 1)
            pair_reports.append(
                {
                    "left": left,
                    "right": right,
                    "cyclic_neighbours": neighbours,
                    "clearance": gap,
                }
            )
            if not neighbours:
                minimum_non_neighbour_clearance = (
                    gap
                    if minimum_non_neighbour_clearance is None
                    else min(minimum_non_neighbour_clearance, gap)
                )

    return {
        "outer_radii": list(radii),
        "center_radius": center_radius,
        "angle_sum": cyclic_angle_sum(radii, center_radius),
        "minimum_non_neighbour_clearance": minimum_non_neighbour_clearance,
        "non_overlapping": minimum_non_neighbour_clearance is None
        or minimum_non_neighbour_clearance >= -1e-9,
        "centers": centers.tolist(),
        "pairs": pair_reports,
    }


def descartes_inner_curvature(curvatures: Iterable[float]) -> float:
    """Curvatura del circulo interior para tres circulos tangentes dados."""

    values = tuple(_positive_radius(value, "curvature") for value in curvatures)
    if len(values) != 3:
        raise ValueError("Se requieren exactamente tres curvaturas positivas.")
    b1, b2, b3 = values
    return b1 + b2 + b3 + 2.0 * sqrt(b1 * b2 + b2 * b3 + b3 * b1)


def descartes_inner_radius(radii: Iterable[float]) -> float:
    values = tuple(_positive_radius(value, "radius") for value in radii)
    if len(values) != 3:
        raise ValueError("Se requieren exactamente tres radios positivos.")
    return 1.0 / descartes_inner_curvature(1.0 / radius for radius in values)


def descartes_reflection(curvatures: Iterable[float], index: int) -> tuple[float, ...]:
    """Sustituye un circulo de una cuadrupla de Descartes por la otra solucion."""

    values = tuple(float(value) for value in curvatures)
    if len(values) != 4 or not all(isfinite(value) for value in values):
        raise ValueError("Se requieren cuatro curvaturas finitas.")
    if index not in range(4):
        raise IndexError("index debe estar entre 0 y 3.")
    reflected = 2.0 * sum(value for position, value in enumerate(values) if position != index) - values[index]
    result = list(values)
    result[index] = reflected
    return tuple(result)


def simplex_gap_ratio(dimension: int) -> float:
    """Hueco central entre d+1 esferas iguales en un d-simplex regular."""

    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 2:
        raise ValueError("dimension debe ser un entero mayor o igual que 2.")
    return sqrt((2.0 * dimension) / (dimension + 1.0)) - 1.0


def octahedral_gap_ratio() -> float:
    """Hueco central entre seis esferas iguales en vertices octaedricos."""

    return sqrt(2.0) - 1.0
