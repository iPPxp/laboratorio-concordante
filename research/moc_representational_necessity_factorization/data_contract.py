"""Frontera de datos que evita entregar el oracle estructural a los modelos."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Mapping

try:
    from .protocol import Partition
except ImportError:  # pragma: no cover
    from protocol import Partition


MODEL_INPUT_FIELDS = frozenset({"case_id", "raw_text", "time_index", "context_id"})
FORBIDDEN_MODEL_INPUT_FIELDS = frozenset({
    "P", "EAF", "ACT", "V", "S", "D", "R", "K", "oracle_structure",
    "target_edit", "future_state", "intervention_effect",
})


@dataclass(frozen=True)
class RawObservation:
    case_id: str
    raw_text: str
    time_index: int
    context_id: str
    scenario_family: str
    partition: Partition

    def model_view(self) -> Mapping[str, object]:
        return {
            "case_id": self.case_id,
            "raw_text": self.raw_text,
            "time_index": self.time_index,
            "context_id": self.context_id,
        }


@dataclass(frozen=True)
class Annotation:
    case_id: str
    annotator_id: str
    P: str | None
    EAF: str | None
    ACT: str | None
    V: str | None
    S: str | None
    relations: tuple[tuple[str, str, str], ...]
    uncertainty: float
    provenance_ids: tuple[str, ...]


@dataclass(frozen=True)
class Outcome:
    case_id: str
    next_case_id: str
    possibilities_added: tuple[str, ...]
    possibilities_removed: tuple[str, ...]
    intervention_id: str | None
    observed_effect: float | None
    source_ids: tuple[str, ...]


def audit_model_view(view: Mapping[str, object]) -> None:
    keys = set(view)
    if keys != MODEL_INPUT_FIELDS:
        raise AssertionError(f"model view keys differ from contract: {sorted(keys)}")
    leaked = keys & FORBIDDEN_MODEL_INPUT_FIELDS
    if leaked:
        raise AssertionError(f"structural oracle leakage: {sorted(leaked)}")


def audit_group_splits(observations: tuple[RawObservation, ...]) -> None:
    seen: dict[str, Partition] = {}
    for observation in observations:
        previous = seen.setdefault(observation.scenario_family, observation.partition)
        if previous is not observation.partition:
            raise AssertionError(
                f"scenario family leaked across partitions: {observation.scenario_family}"
            )


def dataset_digest(observations: tuple[RawObservation, ...]) -> str:
    payload = [
        {
            "case_id": row.case_id, "raw_text": row.raw_text,
            "time_index": row.time_index, "context_id": row.context_id,
            "scenario_family": row.scenario_family,
            "partition": row.partition.value,
        }
        for row in observations
    ]
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True,
                     separators=(",", ":"))
    return sha256(raw.encode("utf-8")).hexdigest()

