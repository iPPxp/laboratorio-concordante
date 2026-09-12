"""Métricas de predicción, calibración, intervención y minimalidad."""

from __future__ import annotations

from dataclasses import dataclass
from math import log


@dataclass(frozen=True)
class BinaryPrediction:
    truth: int
    probability: float

    def __post_init__(self) -> None:
        if self.truth not in (0, 1) or not 0.0 <= self.probability <= 1.0:
            raise ValueError("invalid binary prediction")


def accuracy(rows: tuple[BinaryPrediction, ...]) -> float:
    return sum((row.probability >= 0.5) == bool(row.truth) for row in rows) / len(rows)


def brier(rows: tuple[BinaryPrediction, ...]) -> float:
    return sum((row.probability - row.truth) ** 2 for row in rows) / len(rows)


def log_loss(rows: tuple[BinaryPrediction, ...], eps: float = 1e-12) -> float:
    total = 0.0
    for row in rows:
        probability = min(1 - eps, max(eps, row.probability))
        total -= row.truth * log(probability) + (1 - row.truth) * log(1 - probability)
    return total / len(rows)


def expected_calibration_error(rows: tuple[BinaryPrediction, ...], bins: int = 10) -> float:
    error = 0.0
    for index in range(bins):
        low, high = index / bins, (index + 1) / bins
        bucket = tuple(row for row in rows
                       if low <= row.probability < high
                       or (index == bins - 1 and row.probability == 1.0))
        if bucket:
            confidence = sum(row.probability for row in bucket) / len(bucket)
            frequency = sum(row.truth for row in bucket) / len(bucket)
            error += len(bucket) / len(rows) * abs(confidence - frequency)
    return error


def paired_effect(moc_scores: tuple[float, ...], generic_scores: tuple[float, ...]) -> float:
    if len(moc_scores) != len(generic_scores) or not moc_scores:
        raise ValueError("paired non-empty scores required")
    return sum(m - g for m, g in zip(moc_scores, generic_scores)) / len(moc_scores)


def drop_one_importance(full_score: float, dropped_scores: dict[str, float]) -> dict[str, float]:
    return {component: full_score - score for component, score in dropped_scores.items()}

