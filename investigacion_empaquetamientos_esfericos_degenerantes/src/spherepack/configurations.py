"""Configuraciones de direcciones unitarias con proveniencia matematica explicita."""

from __future__ import annotations

from itertools import combinations
from math import cos, pi, sin, sqrt

import numpy as np

from .geometry import normalize_rows


def antipodal_pair() -> np.ndarray:
    return np.asarray(((1, 0, 0), (-1, 0, 0)), dtype=float)


def regular_tetrahedron() -> np.ndarray:
    return normalize_rows(((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)))


def regular_simplex(dimension: int) -> np.ndarray:
    """Vertices unitarios de un simplex regular en ``R^dimension``.

    Se usa una base de Helmert explicita para el hiperplano de suma cero. Por
    construccion hay ``dimension + 1`` filas, cada norma es uno y todo producto
    interno entre filas distintas es ``-1 / dimension``.
    """

    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 1:
        raise ValueError("dimension debe ser un entero positivo.")

    points = np.zeros((dimension + 1, dimension), dtype=float)
    for row in range(dimension + 1):
        for column in range(dimension):
            index = column + 1
            denominator = sqrt(index * (index + 1))
            if row <= column:
                points[row, column] = 1.0 / denominator
            elif row == column + 1:
                points[row, column] = -index / denominator
    return points * sqrt((dimension + 1.0) / dimension)


def regular_4_simplex() -> np.ndarray:
    """Cinco direcciones del 4-simplex regular en ``R^4``."""

    return regular_simplex(4)


def equatorial_square() -> np.ndarray:
    return np.asarray(((1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)), dtype=float)


def regular_octahedron() -> np.ndarray:
    return np.asarray(((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)), dtype=float)


def twenty_four_cell() -> np.ndarray:
    """Las 24 raices unitarias ``D4``, vertices exactos del 24-cell.

    Antes de normalizar, cada vector tiene exactamente dos coordenadas no nulas
    en ``{+1, -1}``. Esta realizacion es tambien la capa de 24 vecinos que
    alcanza el numero de besos en cuatro dimensiones.
    """

    scale = 1.0 / sqrt(2.0)
    points: list[tuple[float, float, float, float]] = []
    for first_axis, second_axis in combinations(range(4), 2):
        for first_sign in (-1.0, 1.0):
            for second_sign in (-1.0, 1.0):
                point = [0.0, 0.0, 0.0, 0.0]
                point[first_axis] = first_sign * scale
                point[second_axis] = second_sign * scale
                points.append(tuple(point))
    return np.asarray(points, dtype=float)


def cuboctahedron() -> np.ndarray:
    values: list[tuple[int, int, int]] = []
    for zero_axis in range(3):
        other = [axis for axis in range(3) if axis != zero_axis]
        for first in (-1, 1):
            for second in (-1, 1):
                point = [0, 0, 0]
                point[other[0]] = first
                point[other[1]] = second
                values.append(tuple(point))
    return normalize_rows(values)


def icosahedron() -> np.ndarray:
    phi = (1.0 + sqrt(5.0)) / 2.0
    # Tres pares de coordenadas, con la orientacion ciclica correcta. No se
    # deben permutar ingenuamente los dos valores: se perderia la arista comun.
    values: list[tuple[float, float, float]] = [
        (0.0, sign_a, sign_b * phi)
        for sign_a in (-1.0, 1.0) for sign_b in (-1.0, 1.0)
    ] + [
        (sign_a, sign_b * phi, 0.0)
        for sign_a in (-1.0, 1.0) for sign_b in (-1.0, 1.0)
    ] + [
        (sign_b * phi, 0.0, sign_a)
        for sign_a in (-1.0, 1.0) for sign_b in (-1.0, 1.0)
    ]
    return normalize_rows(values)


def hcp_neighbour_shell() -> np.ndarray:
    """Doce vecinos de un centro HCP ideal, escalados a direcciones unitarias.

    La descripcion es una base hexagonal mas dos capas B. HCP se representa como
    red con base, no como red de Bravais simple.
    """
    points: list[tuple[float, float, float]] = []
    for k in range(6):
        angle = k * pi / 3.0
        points.append((2.0 * cos(angle), 2.0 * sin(angle), 0.0))
    z = sqrt(8.0 / 3.0)
    radial = 2.0 / sqrt(3.0)
    for sign in (-1.0, 1.0):
        for k in range(3):
            angle = pi / 6.0 + 2.0 * pi * k / 3.0
            points.append((radial * cos(angle), radial * sin(angle), sign * z))
    return normalize_rows(points)


def named_configurations() -> dict[str, np.ndarray]:
    return {
        "n2_antipodal": antipodal_pair(),
        "n4_tetrahedron": regular_tetrahedron(),
        "n4_square_transition_witness": equatorial_square(),
        "n5_4_simplex": regular_4_simplex(),
        "n6_octahedron": regular_octahedron(),
        "n12_cuboctahedron_fcc_shell": cuboctahedron(),
        "n12_hcp_shell": hcp_neighbour_shell(),
        "n12_icosahedron_comparator": icosahedron(),
        "n24_24_cell_kissing_shell": twenty_four_cell(),
    }
