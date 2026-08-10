"""Verificaciones algebraicas del caso antipodal n=2.

Este módulo no define fuerzas ni energías. Un vector es una dirección y el
Q-tensor representa un eje apolar porque Q(u) = Q(-u).
"""

from __future__ import annotations

import numpy as np

TOLERANCE = 1e-12


def unit(vector: np.ndarray | list[float]) -> np.ndarray:
    value = np.asarray(vector, dtype=float)
    if value.shape != (3,):
        raise ValueError("Se requiere un vector de R^3.")
    norm = np.linalg.norm(value)
    if norm <= TOLERANCE:
        raise ValueError("El vector nulo no determina una dirección proyectiva.")
    return value / norm


def q_tensor(vector: np.ndarray | list[float], scalar_order: float = 1.0) -> np.ndarray:
    """Q = s (u tensor u - I/3), invariante bajo u -> -u."""
    direction = unit(vector)
    return scalar_order * (np.outer(direction, direction) - np.eye(3) / 3.0)


def pair_gram(first: np.ndarray | list[float], second: np.ndarray | list[float]) -> np.ndarray:
    a, b = unit(first), unit(second)
    return np.asarray(((a @ a, a @ b), (b @ a, b @ b)), dtype=float)


def is_antipodal(first: np.ndarray | list[float], second: np.ndarray | list[float]) -> bool:
    return bool(np.linalg.norm(unit(first) + unit(second)) <= TOLERANCE)


def antipodality_indicator(first: np.ndarray | list[float], second: np.ndarray | list[float]) -> int:
    return int(is_antipodal(first, second))


def additive_cross_difference() -> float:
    """Certificado finito de que el indicador no es suma de términos unarios.

    Si F(x,y)=f(x)+g(y), toda diferencia rectangular debe ser cero. Para dos
    direcciones ortogonales u,w se obtiene 1+1-0-0=2.
    """
    u = np.asarray((1.0, 0.0, 0.0))
    w = np.asarray((0.0, 1.0, 0.0))
    return float(
        antipodality_indicator(u, -u)
        + antipodality_indicator(w, -w)
        - antipodality_indicator(u, -w)
        - antipodality_indicator(w, -u)
    )


def verification_report() -> dict[str, object]:
    u = np.asarray((1.0, 0.0, 0.0))
    gram = pair_gram(u, -u)
    eigenvalues = np.linalg.eigvalsh(gram)
    kernel_vector = np.asarray((1.0, 1.0))
    return {
        "epistemic_status": "RESULTADO_COMPUTADO",
        "scope": "n2_antipodal_algebra_only",
        "q_sign_invariance_residual": float(np.linalg.norm(q_tensor(u) - q_tensor(-u))),
        "gram": gram.tolist(),
        "gram_rank": int(np.linalg.matrix_rank(gram, tol=TOLERANCE)),
        "gram_eigenvalues": eigenvalues.tolist(),
        "gram_kernel_residual": float(np.linalg.norm(gram @ kernel_vector)),
        "pair_sum_residual": float(np.linalg.norm(u + (-u))),
        "additive_cross_difference": additive_cross_difference(),
        "relational_nonadditivity_witness": additive_cross_difference() != 0.0,
        "physical_energy_claim": "NONE",
        "central_source_claim": "NOT_DETERMINED",
    }
