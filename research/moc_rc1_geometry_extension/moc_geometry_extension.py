"""MOC-RC1-GEOMETRY-EXTENSION-001.

Non-mutating, optional geometry sidecar for MOC Base 1.0-RC1.

The extension represents five typed component observations, candidate
relations, temporal comparisons, provenance, combinatorial inventories and
declared geometric projections.  It deliberately does *not* infer MOC
semantics from RC1 row names, geometric symmetry, distance, a centroid or a
two-dimensional drawing.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, field, fields, is_dataclass
from enum import Enum
from itertools import combinations
from types import MappingProxyType
from typing import Any, Iterable, Mapping, Sequence


EXTENSION_ID = "MOC-RC1-GEOMETRY-EXTENSION-001"
EXTENSION_VERSION = "0.1.0-candidate"
RC1_RELEASE = "1.0-RC1"


class Component(str, Enum):
    P = "P"
    EAF = "Eaf"
    ACT = "Act"
    V = "V"
    S = "S"


COMPONENTS: tuple[Component, ...] = tuple(Component)


class PresenceStatus(str, Enum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    AMBIGUOUS = "AMBIGUOUS"
    UNKNOWN = "UNKNOWN"


class ChangeStatus(str, Enum):
    CHANGED = "CHANGED"
    STABLE = "STABLE"
    AMBIGUOUS = "AMBIGUOUS"
    UNKNOWN = "UNKNOWN"
    NOT_COMPARABLE = "NOT_COMPARABLE"


class Attribution(str, Enum):
    SUBJECT = "SUBJECT"
    QUOTE = "QUOTE"
    HYPOTHESIS = "HYPOTHESIS"
    CONTEXT = "CONTEXT"


class EpistemicStatus(str, Enum):
    SOURCE_SUPPORTED = "SOURCE_SUPPORTED"
    CANDIDATE = "CANDIDATE"
    HYPOTHESIS = "HYPOTHESIS"
    NOT_SUPPORTED = "NOT_SUPPORTED"


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    source_id: str
    span: str
    attribution: Attribution
    confidence: float
    source_provenance: str = "unknown"

    def __post_init__(self) -> None:
        if not self.evidence_id.strip() or not self.source_id.strip():
            raise ValueError("evidence_id and source_id must be non-empty")
        if not self.span.strip():
            raise ValueError("evidence span must be non-empty")
        _require_unit_interval(self.confidence, "evidence confidence")


@dataclass(frozen=True)
class ComponentObservation:
    component: Component
    presence: PresenceStatus
    change: ChangeStatus = ChangeStatus.NOT_COMPARABLE
    value: tuple[float, ...] | None = None
    evidence: tuple[Evidence, ...] = ()
    comparison_basis: tuple[str, ...] = ()
    uncertainty_note: str | None = None

    def __post_init__(self) -> None:
        if self.value is not None:
            if not self.value:
                raise ValueError("component value vectors cannot be empty")
            if any(not math.isfinite(item) for item in self.value):
                raise ValueError("component value vectors must contain finite numbers")
            if self.presence == PresenceStatus.ABSENT:
                raise ValueError("ABSENT components cannot carry a value vector")
        if self.presence in (PresenceStatus.PRESENT, PresenceStatus.ABSENT) and not self.evidence:
            raise ValueError(f"{self.presence.value} requires affirmative evidence")
        if self.change in (ChangeStatus.CHANGED, ChangeStatus.STABLE) and len(self.comparison_basis) < 2:
            raise ValueError(f"{self.change.value} requires at least two comparable observations")
        if self.change == ChangeStatus.NOT_COMPARABLE and len(self.comparison_basis) >= 2:
            raise ValueError("NOT_COMPARABLE cannot carry two or more comparison points")


@dataclass(frozen=True)
class TypedRelation:
    relation_id: str
    source: Component
    target: Component
    relation_type: str
    epistemic_status: EpistemicStatus
    directed: bool = True
    weight: float | None = None
    weight_semantics: str | None = None
    evidence_ids: tuple[str, ...] = ()
    mediator: Component | None = None
    note: str = ""

    def __post_init__(self) -> None:
        if not self.relation_id.strip() or not self.relation_type.strip():
            raise ValueError("relation_id and relation_type must be non-empty")
        if self.source == self.target:
            raise ValueError("self-relations are outside this extension contract")
        if self.weight is not None:
            if not math.isfinite(self.weight):
                raise ValueError("relation weight must be finite")
            if not self.weight_semantics or not self.weight_semantics.strip():
                raise ValueError("a relation weight requires declared weight semantics")
        elif self.weight_semantics is not None:
            raise ValueError("weight_semantics requires a relation weight")
        if self.mediator in (self.source, self.target):
            raise ValueError("a mediator must differ from relation endpoints")


@dataclass(frozen=True)
class ProvenanceEvent:
    event_id: str
    actor: str
    operation: str
    source_ids: tuple[str, ...]
    note: str
    reversible: bool = True

    def __post_init__(self) -> None:
        if not self.event_id.strip() or not self.actor.strip() or not self.operation.strip():
            raise ValueError("provenance event identifiers, actor and operation must be non-empty")
        if not self.source_ids:
            raise ValueError("provenance events require at least one source_id")


@dataclass(frozen=True)
class PentacoroSnapshot:
    snapshot_id: str
    time_index: int
    observations: Mapping[Component, ComponentObservation]
    relations: tuple[TypedRelation, ...] = ()
    provenance: tuple[ProvenanceEvent, ...] = ()

    def __post_init__(self) -> None:
        if not self.snapshot_id.strip():
            raise ValueError("snapshot_id must be non-empty")
        normalized = dict(self.observations)
        if set(normalized) != set(COMPONENTS):
            missing = sorted(item.value for item in set(COMPONENTS) - set(normalized))
            extra = sorted(str(item) for item in set(normalized) - set(COMPONENTS))
            raise ValueError(f"a snapshot requires exactly P, Eaf, Act, V and S; missing={missing}, extra={extra}")
        for component, observation in normalized.items():
            if observation.component != component:
                raise ValueError(f"observation key {component.value} does not match payload component")
        relation_ids = [relation.relation_id for relation in self.relations]
        if len(relation_ids) != len(set(relation_ids)):
            raise ValueError("relation identifiers must be unique within a snapshot")
        object.__setattr__(self, "observations", MappingProxyType(normalized))

    def digest(self) -> str:
        return _digest(self)


@dataclass(frozen=True)
class TemporalDelta:
    before_id: str
    after_id: str
    changed_components: tuple[Component, ...]
    added_relation_ids: tuple[str, ...]
    removed_relation_ids: tuple[str, ...]
    retained_relation_ids: tuple[str, ...]


@dataclass(frozen=True)
class CandidateRelationSpec:
    pair: tuple[Component, Component]
    direction: str
    relation_type: str
    epistemic_status: EpistemicStatus
    mediator: Component | None
    falsifier: str


@dataclass(frozen=True)
class ProjectionSpec:
    projection_id: str
    matrix: tuple[tuple[float, ...], tuple[float, ...]]
    source_metric: str | None = None
    purpose: str = "visualization"

    def __post_init__(self) -> None:
        if not self.projection_id.strip():
            raise ValueError("projection_id must be non-empty")
        if len(self.matrix) != 2 or not self.matrix[0] or len(self.matrix[0]) != len(self.matrix[1]):
            raise ValueError("a 2D projection requires a rectangular 2 x n matrix")
        if any(not math.isfinite(value) for row in self.matrix for value in row):
            raise ValueError("projection coefficients must be finite")
        if self.source_metric not in (None, "euclidean"):
            raise ValueError("source_metric must be None or 'euclidean'")
        if self.purpose != "visualization":
            raise ValueError("this candidate extension authorizes visualization projections only")


@dataclass(frozen=True)
class ProjectionReport:
    projection_id: str
    points_2d: Mapping[Component, tuple[float, float]]
    collision_groups: tuple[tuple[Component, ...], ...]
    max_relative_distance_distortion: float | None
    source_metric: str | None
    is_visualization_only: bool = True
    warnings: tuple[str, ...] = (
        "A 2D projection is not a complete representation.",
        "Geometric distance is not semantic distance.",
    )

    def __post_init__(self) -> None:
        object.__setattr__(self, "points_2d", MappingProxyType(dict(self.points_2d)))


@dataclass(frozen=True)
class RC1GeometryReport:
    extension_id: str
    rc1_release: str
    snapshot: PentacoroSnapshot
    simplicial_counts: Mapping[int, int]
    relation_catalogue: tuple[CandidateRelationSpec, ...]
    warnings: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "simplicial_counts", MappingProxyType(dict(self.simplicial_counts)))


def _require_unit_interval(value: float, label: str) -> None:
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError(f"{label} must be finite and in [0,1]")


def _primitive(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value):
        return {item.name: _primitive(getattr(value, item.name)) for item in fields(value)}
    if isinstance(value, Mapping):
        return {str(_primitive(key)): _primitive(item) for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))}
    if isinstance(value, (tuple, list)):
        return [_primitive(item) for item in value]
    return value


def _digest(value: Any) -> str:
    payload = json.dumps(_primitive(value), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def simplex_inventory() -> Mapping[int, tuple[tuple[Component, ...], ...]]:
    """Return every non-empty subset; no subset receives MOC semantics."""

    return MappingProxyType(
        {size: tuple(combinations(COMPONENTS, size)) for size in range(1, len(COMPONENTS) + 1)}
    )


def simplicial_counts() -> Mapping[int, int]:
    """Return dimensions 0..4 -> 5,10,10,5,1."""

    inventory = simplex_inventory()
    return MappingProxyType({size - 1: len(items) for size, items in inventory.items()})


def vertex_complements() -> Mapping[Component, tuple[Component, ...]]:
    return MappingProxyType(
        {component: tuple(other for other in COMPONENTS if other != component) for component in COMPONENTS}
    )


def candidate_relation_catalogue() -> tuple[CandidateRelationSpec, ...]:
    """Ten pairwise hypotheses from the current review; never auto-applied."""

    rows = (
        (Component.P, Component.EAF, "P_TO_EAF", "interpretation_may_organize_affect", EpistemicStatus.SOURCE_SUPPORTED, None, "P may be present without observable Eaf."),
        (Component.P, Component.ACT, "BIDIRECTIONAL", "interpretation_response_feedback", EpistemicStatus.SOURCE_SUPPORTED, None, "Reverse influence requires temporal evidence."),
        (Component.P, Component.V, "V_TO_P", "criterion_orients_interpretation", EpistemicStatus.HYPOTHESIS, None, "The corpus does not cleanly separate V from certainty or preference."),
        (Component.P, Component.S, "BIDIRECTIONAL", "meaning_condition_feedback", EpistemicStatus.CANDIDATE, None, "S must not be assumed neutral as a MOC axiom."),
        (Component.EAF, Component.ACT, "EAF_TO_ACT", "affect_modulates_response", EpistemicStatus.CANDIDATE, None, "Act may occur without visible affect or against it."),
        (Component.EAF, Component.V, "BIDIRECTIONAL", "affect_value_signal", EpistemicStatus.HYPOTHESIS, None, "Pleasant affect can accompany a problematic pattern."),
        (Component.EAF, Component.S, "MEDIATED", "situated_affect", EpistemicStatus.CANDIDATE, Component.P, "Do not infer affect from situation alone."),
        (Component.ACT, Component.V, "V_TO_ACT", "criterion_prioritizes_response", EpistemicStatus.CANDIDATE, None, "Preference and emotion are insufficient to infer V."),
        (Component.ACT, Component.S, "BIDIRECTIONAL", "response_affordance_feedback", EpistemicStatus.CANDIDATE, None, "External change does not prove experiential change."),
        (Component.V, Component.S, "BIDIRECTIONAL", "relevance_consequence_feedback", EpistemicStatus.HYPOTHESIS, None, "Requires temporal episodes rather than one sentence."),
    )
    return tuple(
        CandidateRelationSpec(
            pair=(left, right),
            direction=direction,
            relation_type=relation_type,
            epistemic_status=status,
            mediator=mediator,
            falsifier=falsifier,
        )
        for left, right, direction, relation_type, status, mediator, falsifier in rows
    )


def compare_snapshots(before: PentacoroSnapshot, after: PentacoroSnapshot) -> TemporalDelta:
    changed = tuple(
        component
        for component in COMPONENTS
        if before.observations[component] != after.observations[component]
    )
    before_ids = {relation.relation_id for relation in before.relations}
    after_ids = {relation.relation_id for relation in after.relations}
    return TemporalDelta(
        before_id=before.snapshot_id,
        after_id=after.snapshot_id,
        changed_components=changed,
        added_relation_ids=tuple(sorted(after_ids - before_ids)),
        removed_relation_ids=tuple(sorted(before_ids - after_ids)),
        retained_relation_ids=tuple(sorted(before_ids & after_ids)),
    )


def project_snapshot(snapshot: PentacoroSnapshot, spec: ProjectionSpec, *, tolerance: float = 1e-9) -> ProjectionReport:
    if tolerance <= 0 or not math.isfinite(tolerance):
        raise ValueError("projection tolerance must be positive and finite")
    input_dimension = len(spec.matrix[0])
    vectors: dict[Component, tuple[float, ...]] = {}
    for component in COMPONENTS:
        observation = snapshot.observations[component]
        if observation.value is None:
            raise ValueError(f"component {component.value} has no declared vector")
        if len(observation.value) != input_dimension:
            raise ValueError(
                f"component {component.value} has dimension {len(observation.value)}; projection expects {input_dimension}"
            )
        vectors[component] = observation.value

    points = {
        component: (
            sum(coefficient * value for coefficient, value in zip(spec.matrix[0], vector)),
            sum(coefficient * value for coefficient, value in zip(spec.matrix[1], vector)),
        )
        for component, vector in vectors.items()
    }
    groups: list[tuple[Component, ...]] = []
    unused = set(COMPONENTS)
    while unused:
        anchor = min(unused, key=lambda item: COMPONENTS.index(item))
        group = tuple(
            component
            for component in COMPONENTS
            if component in unused and _euclidean(points[anchor], points[component]) <= tolerance
        )
        for component in group:
            unused.remove(component)
        if len(group) > 1:
            groups.append(group)

    distortion: float | None = None
    if spec.source_metric == "euclidean":
        distortions: list[float] = []
        for left, right in combinations(COMPONENTS, 2):
            source_distance = _euclidean(vectors[left], vectors[right])
            projected_distance = _euclidean(points[left], points[right])
            if source_distance <= tolerance:
                if projected_distance > tolerance:
                    distortions.append(math.inf)
                continue
            distortions.append(abs(projected_distance - source_distance) / source_distance)
        distortion = max(distortions, default=0.0)

    return ProjectionReport(
        projection_id=spec.projection_id,
        points_2d=points,
        collision_groups=tuple(groups),
        max_relative_distance_distortion=distortion,
        source_metric=spec.source_metric,
    )


def _euclidean(left: Sequence[float], right: Sequence[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def _normalize_mapping(row_mapping: Mapping[str, Component | str]) -> dict[str, Component]:
    normalized: dict[str, Component] = {}
    for row, component in row_mapping.items():
        if not isinstance(row, str) or not row.strip():
            raise ValueError("RC1 row names in the mapping must be non-empty strings")
        try:
            normalized[row] = component if isinstance(component, Component) else Component(component)
        except ValueError as exc:
            raise ValueError(f"unknown Pentacoro component in mapping: {component!r}") from exc
    if set(normalized.values()) != set(COMPONENTS) or len(normalized) != len(COMPONENTS):
        raise ValueError("row_mapping must be a five-to-five bijection onto P, Eaf, Act, V and S")
    return normalized


def adapt_rc1_matrix(
    matrix_q: Any,
    *,
    row_mapping: Mapping[str, Component | str],
    snapshot_id: str,
    time_index: int,
    source_id: str,
) -> PentacoroSnapshot:
    """Adapt an RC1 MatrixQ only through an explicit caller-supplied mapping."""

    mapping = _normalize_mapping(row_mapping)
    rows = getattr(matrix_q, "rows", None)
    if not isinstance(rows, Mapping):
        raise ValueError("matrix_q must expose a mapping named rows")
    if set(rows) != set(mapping):
        raise ValueError("row_mapping keys must exactly match the RC1 matrix rows")

    observations: dict[Component, ComponentObservation] = {}
    for row_name, component in mapping.items():
        row = rows[row_name]
        coordinates = tuple(float(item) for item in getattr(row, "coordinates"))
        confidence = float(getattr(row, "confidence"))
        _require_unit_interval(confidence, f"confidence for RC1 row {row_name}")
        provenance = getattr(row, "provenance", "unknown")
        provenance_value = getattr(provenance, "value", str(provenance))
        attribution = Attribution.SUBJECT if provenance_value == "explicit_self_report" else Attribution.HYPOTHESIS
        evidence = Evidence(
            evidence_id=f"{snapshot_id}:{row_name}",
            source_id=source_id,
            span=f"RC1 matrix row {row_name}; Pentacoro mapping supplied by caller",
            attribution=attribution,
            confidence=confidence,
            source_provenance=provenance_value,
        )
        observations[component] = ComponentObservation(
            component=component,
            presence=PresenceStatus.PRESENT,
            change=ChangeStatus.NOT_COMPARABLE,
            value=coordinates,
            evidence=(evidence,),
            uncertainty_note="The row-to-component mapping is declared externally and is not inferred by RC1.",
        )

    event = ProvenanceEvent(
        event_id=f"{snapshot_id}:adapt",
        actor="rc1-geometry-sidecar",
        operation="adapt_rc1_matrix_with_declared_mapping",
        source_ids=(source_id,),
        note="Non-mutating adaptation. The mapping records caller authority; it does not grant semantic approval.",
    )
    return PentacoroSnapshot(
        snapshot_id=snapshot_id,
        time_index=time_index,
        observations=observations,
        relations=(),
        provenance=(event,),
    )


def analyze_rc1_envelope(
    envelope: Any,
    *,
    row_mapping: Mapping[str, Component | str],
    source_id: str,
) -> RC1GeometryReport:
    matrix_q = getattr(envelope, "matrix_q", None)
    if matrix_q is None:
        raise ValueError("the RC1 envelope has no matrix_q")
    candidate_id = str(getattr(envelope, "candidate_id", "unknown-candidate"))
    snapshot = adapt_rc1_matrix(
        matrix_q,
        row_mapping=row_mapping,
        snapshot_id=f"geometry:{candidate_id}",
        time_index=0,
        source_id=source_id,
    )
    return RC1GeometryReport(
        extension_id=EXTENSION_ID,
        rc1_release=RC1_RELEASE,
        snapshot=snapshot,
        simplicial_counts=simplicial_counts(),
        relation_catalogue=candidate_relation_catalogue(),
        warnings=(
            "RC1 was not mutated.",
            "The candidate relation catalogue was not instantiated as observed relations.",
            "The 5-10-10-5-1 sequence is combinatorial inventory, not MOC evidence.",
            "Conduct is not a sixth Pentacoro component.",
            "No metric, centroid, symmetry or projection has semantic authority.",
        ),
    )


def validate_no_sixth_component(names: Iterable[str]) -> None:
    normalized = {name.strip().casefold() for name in names}
    allowed = {component.value.casefold() for component in COMPONENTS}
    extra = normalized - allowed
    if extra:
        raise ValueError(f"unsupported Pentacoro components: {sorted(extra)}")

