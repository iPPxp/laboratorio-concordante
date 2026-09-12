"""Contrato metodológico del programa de factorización MOC.

No contiene corpus, etiquetas experienciales ni una política de intervención.
Sólo fija las fronteras y controles que un dataset independiente deberá llenar.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from itertools import combinations


class Component(str, Enum):
    P = "P"
    EAF = "EAF"
    ACT = "ACT"
    V = "V"
    S = "S"


class DRole(str, Enum):
    STATE_PRIMITIVE = "STATE_PRIMITIVE"
    DIFFERENTIATION_OPERATION = "DIFFERENTIATION_OPERATION"
    DERIVED_RELATION = "DERIVED_RELATION"
    NOT_REQUIRED = "NOT_REQUIRED"


class Partition(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    CASE_HOLDOUT = "CASE_HOLDOUT"
    TRANSFORMATION_HOLDOUT = "TRANSFORMATION_HOLDOUT"
    DOMAIN_HOLDOUT = "DOMAIN_HOLDOUT"


@dataclass(frozen=True)
class Boundary:
    left: Component
    right: Component

    @property
    def boundary_id(self) -> str:
        return f"{self.left.value}__{self.right.value}"


@dataclass(frozen=True)
class ContrastSpec:
    contrast_id: str
    boundary: Boundary
    changed: Component
    held_approximately_constant: tuple[Component, ...]
    outcome_targets: tuple[str, ...]
    status: str = "DESIGN_ONLY_NO_DATA"


BOUNDARIES = tuple(Boundary(a, b) for a, b in combinations(Component, 2))


def build_contrast_specs() -> tuple[ContrastSpec, ...]:
    specs: list[ContrastSpec] = []
    for boundary in BOUNDARIES:
        for changed in (boundary.left, boundary.right):
            held = tuple(component for component in Component if component is not changed)
            specs.append(ContrastSpec(
                contrast_id=f"CF-{boundary.boundary_id}-{changed.value}",
                boundary=boundary,
                changed=changed,
                held_approximately_constant=held,
                outcome_targets=(
                    "NEXT_STATE", "POSSIBILITY_FIELD", "INTERVENTION_EFFECT",
                    "STABILITY", "UNCERTAINTY",
                ),
            ))
    return tuple(specs)


CONTRAST_SPECS = build_contrast_specs()


def canonical_manifest() -> str:
    rows = [
        {
            "id": spec.contrast_id,
            "boundary": spec.boundary.boundary_id,
            "changed": spec.changed.value,
            "held": [c.value for c in spec.held_approximately_constant],
            "targets": list(spec.outcome_targets),
            "status": spec.status,
        }
        for spec in CONTRAST_SPECS
    ]
    return json.dumps(rows, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))


MANIFEST_SHA256 = sha256(canonical_manifest().encode("utf-8")).hexdigest()


def verify_manifest() -> None:
    if len(BOUNDARIES) != 10 or len(CONTRAST_SPECS) != 20:
        raise AssertionError("five components require 10 boundaries and 20 directions")
    ids = {spec.contrast_id for spec in CONTRAST_SPECS}
    if len(ids) != len(CONTRAST_SPECS):
        raise AssertionError("contrast IDs must be unique")
    for boundary in BOUNDARIES:
        directions = {spec.changed for spec in CONTRAST_SPECS
                      if spec.boundary == boundary}
        if directions != {boundary.left, boundary.right}:
            raise AssertionError(f"missing inverse contrast for {boundary.boundary_id}")


verify_manifest()

