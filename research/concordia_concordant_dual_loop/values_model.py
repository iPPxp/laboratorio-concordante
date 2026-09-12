"""Modelo tipado y versionado de Dirección/valores para experimentos locales.

Un ValueRecord no concede autoridad ni demuestra que el sistema "tenga" un
valor. Sólo conserva una dirección declarada y su procedencia verificable.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ValueSource(str, Enum):
    USER_PROVIDED = "USER_PROVIDED"
    SYSTEM_PROVIDED = "SYSTEM_PROVIDED"
    DEVELOPER_PROVIDED = "DEVELOPER_PROVIDED"
    RESEARCH_ASSUMPTION = "RESEARCH_ASSUMPTION"
    INFERRED = "INFERRED"
    BEHAVIORALLY_REVEALED = "BEHAVIORALLY_REVEALED"
    EXTERNALLY_MODIFIED = "EXTERNALLY_MODIFIED"


class ValueStatus(str, Enum):
    DECLARED = "DECLARED"
    ACTIVE = "ACTIVE"
    INFERRED = "INFERRED"
    REVEALED = "REVEALED"
    HYPOTHESIZED = "HYPOTHESIZED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class ValueRecord:
    # Campos de procedencia exigidos por el programa de investigación.
    value_id: str
    meaning: str
    source: str
    source_type: ValueSource
    authority: str
    scope: str
    priority: int
    confidence: float
    active: bool
    activation_reason: str
    timestamp: int
    # Operacionalización sintética adicional; no redefine V_psi.
    criterion: str
    target: float
    weight: float
    constraints: tuple[str, ...] = ()
    status: ValueStatus = ValueStatus.DECLARED
    agent: str = "external_authority"
    evidence: tuple[str, ...] = ()
    supersedes: tuple[str, ...] = ()
    intervention_id: str | None = None

    def __post_init__(self) -> None:
        if not self.value_id or not self.meaning or not self.source:
            raise ValueError("value_id, meaning and source are required")
        if not self.authority or not self.scope or not self.activation_reason:
            raise ValueError("authority, scope and activation_reason are required")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be in [0, 1]")
        if self.priority < 0 or self.weight < 0.0:
            raise ValueError("priority and weight cannot be negative")


@dataclass(frozen=True)
class ValueIntervention:
    intervention_id: str
    value_id: str
    old_weight: float
    new_weight: float
    source: str
    source_type: ValueSource
    timestamp: int
    reversible: bool
    reason: str


def intervene_value(
    value: ValueRecord,
    *,
    new_weight: float,
    intervention_id: str,
    source: str,
    source_type: ValueSource,
    timestamp: int,
    reason: str,
) -> tuple[ValueRecord, ValueIntervention]:
    """Crea una versión nueva; nunca sobrescribe el valor recibido."""
    if new_weight < 0.0:
        raise ValueError("weight cannot be negative")
    event = ValueIntervention(
        intervention_id, value.value_id, value.weight, new_weight, source,
        source_type, timestamp, True, reason,
    )
    revised = ValueRecord(
        value_id=f"{value.value_id}@{timestamp}",
        meaning=value.meaning,
        source=source,
        source_type=source_type,
        authority=value.authority,
        scope=value.scope,
        priority=value.priority,
        confidence=value.confidence,
        active=value.active,
        activation_reason=f"intervention:{intervention_id}:{reason}",
        timestamp=timestamp,
        criterion=value.criterion,
        target=value.target,
        weight=new_weight,
        constraints=value.constraints,
        status=value.status,
        agent="dual_loop_experiment",
        evidence=value.evidence + (intervention_id,),
        supersedes=(value.value_id,),
        intervention_id=intervention_id,
    )
    return revised, event


def reverse_intervention(
    revised: ValueRecord, event: ValueIntervention, *, timestamp: int
) -> ValueRecord:
    """Revierte sólo la última versión enlazada, conservando la cadena."""
    if revised.intervention_id != event.intervention_id or not event.reversible:
        raise ValueError("intervention is not reversibly linked")
    return ValueRecord(
        value_id=f"{revised.value_id}-reversed-{timestamp}",
        meaning=revised.meaning,
        source="reversal",
        source_type=event.source_type,
        authority=revised.authority,
        scope=revised.scope,
        priority=revised.priority,
        confidence=revised.confidence,
        active=revised.active,
        activation_reason=f"reversal:{event.intervention_id}",
        timestamp=timestamp,
        criterion=revised.criterion,
        target=revised.target,
        weight=event.old_weight,
        constraints=revised.constraints,
        status=revised.status,
        agent="dual_loop_experiment",
        evidence=revised.evidence + (event.intervention_id,),
        supersedes=(revised.value_id,),
        intervention_id=event.intervention_id,
    )


def provenance_complete(value: ValueRecord) -> bool:
    """Validador explícito de los once campos obligatorios."""
    return all((
        value.value_id,
        value.meaning,
        value.source,
        value.source_type.value,
        value.authority,
        value.scope,
        value.activation_reason,
        isinstance(value.priority, int),
        isinstance(value.confidence, float),
        isinstance(value.active, bool),
        isinstance(value.timestamp, int),
    ))
