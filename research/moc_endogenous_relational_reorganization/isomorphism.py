"""Falsador ejecutable de isomorfismo simple entre trazas B6 y MOC_R."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json

try:
    from .generic_controllers import ControllerResult
except ImportError:  # pragma: no cover
    from generic_controllers import ControllerResult


MAPPING_VERSION = "B6-MOCR-ALPHA-001"


@dataclass(frozen=True)
class IsomorphismResult:
    exact: bool
    outcome_only: bool
    first_witness: str | None
    left_digest: str
    right_digest: str


def _relation(rel) -> tuple[str, str, str, float]:
    return rel.source, rel.target, rel.kind, rel.weight


def normalize_trace(result: ControllerResult) -> dict[str, object]:
    """Elimina nombres de actores/IDs, pero conserva estructura y causalidad."""
    events = [
        {
            "operation": event.operation,
            "target": event.target,
            "before": event.before_digest,
            "after": event.after_digest,
            "source_arity": len(event.source_ids),
            "source_type": event.source_type.value,
            "reversible": event.reversible,
        }
        for event in result.after.provenance[len(result.before.provenance):]
    ]
    return {
        "before": {
            "D": sorted(result.before.D.items()),
            "R": sorted(_relation(r) for r in result.before.R),
            "K": sorted(result.before.K),
            "G": (result.before.generator.operations,
                  result.before.generator.max_candidates,
                  result.before.generator.revision),
        },
        "after": {
            "D": sorted(result.after.D.items()),
            "R": sorted(_relation(r) for r in result.after.R),
            "K": sorted(result.after.K),
            "G": (result.after.generator.operations,
                  result.after.generator.max_candidates,
                  result.after.generator.revision),
        },
        "field_before": sorted(result.field_before.action_ids),
        "field_after": sorted(result.field_after.action_ids),
        "decision": (result.action_before, result.action_after),
        "events": events,
    }


def _digest(value: object) -> str:
    return sha256(json.dumps(value, sort_keys=True, default=list,
                             separators=(",", ":")).encode("utf-8")).hexdigest()


def compare_traces(left: ControllerResult,
                   right: ControllerResult) -> IsomorphismResult:
    lnorm, rnorm = normalize_trace(left), normalize_trace(right)
    witness = None
    for key in ("before", "after", "field_before", "field_after", "decision", "events"):
        if lnorm[key] != rnorm[key]:
            witness = key
            break
    outcome_only = (
        lnorm["field_after"] == rnorm["field_after"]
        and lnorm["decision"] == rnorm["decision"]
    )
    return IsomorphismResult(lnorm == rnorm, outcome_only, witness,
                             _digest(lnorm), _digest(rnorm))


__all__ = ["MAPPING_VERSION", "IsomorphismResult", "normalize_trace", "compare_traces"]
