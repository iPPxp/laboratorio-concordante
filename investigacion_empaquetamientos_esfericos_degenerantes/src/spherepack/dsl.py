"""Validador de estructura para una DSL declarativa minima, sin ejecutar modelos."""

from __future__ import annotations

from math import isfinite
from typing import Any

REQUIRED_CASE_FIELDS = {
    "case_id",
    "kind",
    "n",
    "ambient_dimension",
    "outer_radius",
    "central_radius",
    "directions",
    "epistemic_status",
}
VALID_KINDS = {"CENTERED_CONFIGURATION", "LATTICE_REFERENCE", "TRANSITION_QUERY"}
VALID_LABELS = {
    "DEFINICION_PROPUESTA", "RESULTADO_CLASICO", "DEMOSTRADO_EN_ESTE_TRABAJO",
    "DERIVACION_SIMBOLICA", "RESULTADO_COMPUTADO", "OBSERVACION_NUMERICA",
    "OBSERVACION_VISUAL", "CONJETURA", "INTERPRETACION", "PENDIENTE_DE_VERIFICACION",
    "REFUTADO_POR_CONTRAEJEMPLO",
}


def _finite_number(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and isfinite(float(value))
    )


def validate_case(case: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_CASE_FIELDS - set(case)
    if missing:
        errors.append(f"missing_fields={sorted(missing)}")
    if case.get("kind") not in VALID_KINDS:
        errors.append("invalid_kind")
    n = case.get("n")
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        errors.append("invalid_n")
    dimension = case.get("ambient_dimension")
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 1:
        errors.append("invalid_ambient_dimension")
    if not _finite_number(case.get("outer_radius")) or case.get("outer_radius") != 1:
        errors.append("outer_radius_must_be_1")
    if not _finite_number(case.get("central_radius")) or case.get("central_radius", 0) <= 0:
        errors.append("central_radius_must_be_positive")
    directions = case.get("directions")
    cardinality_is_valid = isinstance(directions, list) and isinstance(n, int) and len(directions) == n
    if not cardinality_is_valid:
        errors.append("directions_cardinality_mismatch")
    if isinstance(directions, list) and isinstance(dimension, int) and dimension >= 1:
        rows_have_declared_dimension = all(
            isinstance(row, list) and len(row) == dimension
            for row in directions
        )
        if not rows_have_declared_dimension:
            errors.append("directions_dimension_mismatch")
        else:
            entries_are_finite = all(
                _finite_number(coordinate)
                for row in directions
                for coordinate in row
            )
            if not entries_are_finite:
                errors.append("directions_must_be_finite_numeric")
            elif any(all(float(coordinate) == 0.0 for coordinate in row) for row in directions):
                errors.append("directions_must_be_nonzero")
    if case.get("epistemic_status") not in VALID_LABELS:
        errors.append("invalid_epistemic_status")
    return errors
