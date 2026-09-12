"""Construcción y comparación de campos genéricos de posibilidades."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from state_model import RelationalState


@dataclass(frozen=True, order=True)
class Candidate:
    action_id: str
    score: float
    origin_operation: str
    source_ids: tuple[str, ...]


@dataclass(frozen=True)
class PossibilityField:
    candidates: tuple[Candidate, ...]
    state_digest: str
    generator_revision: int

    @property
    def action_ids(self) -> frozenset[str]:
        return frozenset(candidate.action_id for candidate in self.candidates)


@dataclass(frozen=True)
class FieldDelta:
    added: frozenset[str]
    removed: frozenset[str]
    retained: frozenset[str]
    expansion: int
    contraction: int
    transitability: float


def generate_field(state: RelationalState) -> PossibilityField:
    candidates: list[Candidate] = []
    nodes = sorted(state.D)
    for operation in state.generator.operations:
        if operation == "select_node":
            candidates.extend(Candidate(f"select:{node}", state.D[node], operation,
                                        (node,)) for node in nodes)
        elif operation == "traverse_relation":
            candidates.extend(Candidate(f"traverse:{r.source}->{r.target}", r.weight,
                                        operation, (r.source, r.target)) for r in state.R)
        elif operation == "hold":
            candidates.append(Candidate("hold", 0.0, operation, ()))
        elif operation == "combine_pair":
            for index, left in enumerate(nodes):
                for right in nodes[index + 1:]:
                    candidates.append(Candidate(f"combine:{left}+{right}",
                                                state.D[left] + state.D[right],
                                                operation, (left, right)))
        else:
            raise ValueError(f"unsupported generic operation: {operation}")
    candidates = sorted(candidates, key=lambda c: (-c.score, c.action_id))
    return PossibilityField(tuple(candidates[:state.generator.max_candidates]),
                            state.structure_digest(), state.generator.revision)


def compare_fields(before: PossibilityField, after: PossibilityField) -> FieldDelta:
    added = after.action_ids - before.action_ids
    removed = before.action_ids - after.action_ids
    retained = before.action_ids & after.action_ids
    union = before.action_ids | after.action_ids
    transitability = len(retained) / len(union) if union else 1.0
    return FieldDelta(added, removed, retained, len(added), len(removed), transitability)


def select_best(field: PossibilityField) -> Candidate | None:
    return field.candidates[0] if field.candidates else None

