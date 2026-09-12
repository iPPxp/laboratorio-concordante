"""Estado relacional genérico para controles B4/B5/B6.

No contiene vocabulario, fixtures ni supuestos semánticos de dominio.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum
from hashlib import sha256
from typing import Mapping


class SourceType(str, Enum):
    EXTERNAL_INPUT = "EXTERNAL_INPUT"
    CONTROLLER_DERIVED = "CONTROLLER_DERIVED"
    CONTROLLER_INTERVENTION = "CONTROLLER_INTERVENTION"
    TEST_CONTROL = "TEST_CONTROL"


@dataclass(frozen=True)
class ProvenanceEvent:
    event_id: str
    timestamp: int
    actor: str
    operation: str
    target: str
    before_digest: str
    after_digest: str
    source_ids: tuple[str, ...]
    source_type: SourceType
    rationale: str
    reversible: bool


@dataclass(frozen=True)
class Relation:
    source: str
    target: str
    kind: str = "link"
    weight: float = 1.0


@dataclass(frozen=True)
class GeneratorSpec:
    name: str
    operations: tuple[str, ...]
    max_candidates: int
    revision: int = 0

    def __post_init__(self) -> None:
        if self.max_candidates < 1:
            raise ValueError("max_candidates must be positive")


@dataclass(frozen=True)
class RelationalState:
    """D: nodes/data; R: relations; K: constraints; G: generator."""

    D: Mapping[str, float]
    R: tuple[Relation, ...]
    K: frozenset[str]
    generator: GeneratorSpec
    provenance: tuple[ProvenanceEvent, ...] = ()
    selected_action: str | None = None

    def digest(self, *, include_provenance: bool = False) -> str:
        payload = (dict(self.D), self.R, self.K, self.generator,
                   self.selected_action)
        if include_provenance:
            payload += (self.provenance,)
        return sha256(repr(payload).encode("utf-8")).hexdigest()

    def structure_digest(self) -> str:
        return sha256(repr((dict(self.D), self.R, self.K, self.generator)).encode("utf-8")).hexdigest()


def record_edit(
    before: RelationalState,
    after: RelationalState,
    *,
    event_id: str,
    timestamp: int,
    actor: str,
    operation: str,
    target: str,
    source_ids: tuple[str, ...],
    source_type: SourceType,
    rationale: str,
    reversible: bool = True,
) -> RelationalState:
    event = ProvenanceEvent(
        event_id, timestamp, actor, operation, target,
        before.structure_digest(), after.structure_digest(), source_ids,
        source_type, rationale, reversible,
    )
    return replace(after, provenance=before.provenance + (event,))


def assert_well_formed(state: RelationalState) -> None:
    nodes = set(state.D)
    if any(rel.source not in nodes or rel.target not in nodes for rel in state.R):
        raise ValueError("every relation endpoint must exist in D")
    if len(set(state.R)) != len(state.R):
        raise ValueError("duplicate relations are not permitted")

