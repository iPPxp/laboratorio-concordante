"""Validador de estructura para una DSL declarativa minima, sin ejecutar modelos."""

from __future__ import annotations

from typing import Any

REQUIRED_CASE_FIELDS = {"case_id", "kind", "n", "outer_radius", "central_radius", "directions", "epistemic_status"}
VALID_KINDS = {"CENTERED_CONFIGURATION", "LATTICE_REFERENCE", "TRANSITION_QUERY"}
VALID_LABELS = {
    "DEFINICION_PROPUESTA", "RESULTADO_CLASICO", "DEMOSTRADO_EN_ESTE_TRABAJO",
    "DERIVACION_SIMBOLICA", "RESULTADO_COMPUTADO", "OBSERVACION_NUMERICA",
    "OBSERVACION_VISUAL", "CONJETURA", "INTERPRETACION", "PENDIENTE_DE_VERIFICACION",
    "REFUTADO_POR_CONTRAEJEMPLO",
}


def validate_case(case: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_CASE_FIELDS - set(case)
    if missing:
        errors.append(f"missing_fields={sorted(missing)}")
    if case.get("kind") not in VALID_KINDS:
        errors.append("invalid_kind")
    if not isinstance(case.get("n"), int) or case.get("n", 0) < 2:
        errors.append("invalid_n")
    if case.get("outer_radius") != 1:
        errors.append("outer_radius_must_be_1")
    if not isinstance(case.get("central_radius"), (int, float)) or case.get("central_radius", 0) <= 0:
        errors.append("central_radius_must_be_positive")
    directions = case.get("directions")
    if not isinstance(directions, list) or len(directions) != case.get("n"):
        errors.append("directions_cardinality_mismatch")
    if case.get("epistemic_status") not in VALID_LABELS:
        errors.append("invalid_epistemic_status")
    return errors
