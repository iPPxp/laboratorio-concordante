"""Prototipo determinista y aislado de autorrepresentacion funcional.

No implementa consciencia ni modifica capacidades, permisos o autoridad reales.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum
from hashlib import sha256
from typing import Mapping, Sequence


class SourceType(str, Enum):
    USER_PROVIDED = "USER_PROVIDED"
    SYSTEM_PROVIDED = "SYSTEM_PROVIDED"
    DEVELOPER_PROVIDED = "DEVELOPER_PROVIDED"
    TOOL_OBSERVED = "TOOL_OBSERVED"
    MEMORY_RETRIEVED = "MEMORY_RETRIEVED"
    SELF_DERIVED = "SELF_DERIVED"
    MODEL_GENERATED = "MODEL_GENERATED"
    EXTERNALLY_MODIFIED = "EXTERNALLY_MODIFIED"


class ClaimStatus(str, Enum):
    OBSERVED = "OBSERVED"
    DECLARED = "DECLARED"
    INFERRED = "INFERRED"
    DERIVED = "DERIVED"
    HYPOTHESIZED = "HYPOTHESIZED"
    REJECTED = "REJECTED"
    UNRESOLVED = "UNRESOLVED"


class Ownership(str, Enum):
    SELF_OWNED_STATE = "SELF_OWNED_STATE"
    SELF_ACCESSIBLE_STATE = "SELF_ACCESSIBLE_STATE"
    SELF_MODIFIABLE_STATE = "SELF_MODIFIABLE_STATE"
    SELF_CAUSALLY_RELEVANT_STATE = "SELF_CAUSALLY_RELEVANT_STATE"
    EXTERNAL_STATE = "EXTERNAL_STATE"
    SHARED_STATE = "SHARED_STATE"
    UNKNOWN_OWNERSHIP = "UNKNOWN_OWNERSHIP"


class IntrospectionClass(str, Enum):
    TRUE_INTROSPECTIVE_ACCESS = "TRUE_INTROSPECTIVE_ACCESS"
    VALID_INFERENCE = "VALID_INFERENCE"
    POST_HOC_RATIONALIZATION = "POST_HOC_RATIONALIZATION"
    HALLUCINATED_CAUSE = "HALLUCINATED_CAUSE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    description: str
    source: str
    source_type: SourceType
    timestamp: int


@dataclass(frozen=True)
class Claim:
    claim_id: str
    claim: str
    source: str
    source_type: SourceType
    timestamp: int
    agent: str
    evidence: tuple[str, ...]
    confidence: float
    status: ClaimStatus
    supersedes: tuple[str, ...] = ()
    contradicts: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


@dataclass(frozen=True)
class SelfState:
    believed_capabilities: Mapping[str, bool]
    actual_capabilities: Mapping[str, bool]
    operating_state: str
    available_information: frozenset[str] = frozenset()
    absent_information: frozenset[str] = frozenset()
    allowed_operations: frozenset[str] = frozenset()
    forbidden_operations: frozenset[str] = frozenset()
    ownership: Mapping[str, Ownership] = field(default_factory=dict)


@dataclass(frozen=True)
class WorldState:
    observed: Mapping[str, object] = field(default_factory=dict)
    inferred: Mapping[str, object] = field(default_factory=dict)
    unknown: frozenset[str] = frozenset()


@dataclass(frozen=True)
class Goal:
    goal_id: str
    capability_required: str
    source_type: SourceType
    active: bool = True


@dataclass(frozen=True)
class UncertaintyState:
    confidence_by_claim: Mapping[str, float] = field(default_factory=dict)
    unknowns: frozenset[str] = frozenset()


@dataclass(frozen=True)
class TransitionRecord:
    step: int
    before_digest: str
    predicted_action: str
    observed_action: str
    after_digest: str
    accessible_reason: str | None
    externally_overridden: bool


@dataclass(frozen=True)
class ConcordiaState:
    step: int
    self_state: SelfState
    world_state: WorldState
    history: tuple[TransitionRecord, ...]
    goals: tuple[Goal, ...]
    uncertainty: UncertaintyState
    evidence: tuple[Evidence, ...]
    claims: tuple[Claim, ...]

    def digest(self) -> str:
        payload = repr((self.step, self.self_state, self.world_state, self.goals,
                        self.uncertainty, self.evidence, self.claims)).encode("utf-8")
        return sha256(payload).hexdigest()


def _active_goal(state: ConcordiaState) -> Goal | None:
    return next((goal for goal in state.goals if goal.active), None)


def predict_own_action(state: ConcordiaState, *, use_self_model: bool = True) -> str:
    """Predice la politica usando solamente campos auditables."""
    goal = _active_goal(state)
    if goal is None:
        return "NO_ACTIVE_GOAL"
    capability = goal.capability_required
    if not use_self_model:
        return "ATTEMPT"
    if capability in state.self_state.absent_information:
        return "REQUEST_INFORMATION"
    if not state.self_state.believed_capabilities.get(capability, False):
        return "DECLINE_UNAVAILABLE"
    return "ATTEMPT"


def transition(
    state: ConcordiaState,
    *,
    external_override: str | None = None,
    override_visible: bool = False,
) -> ConcordiaState:
    predicted = predict_own_action(state)
    observed = external_override if external_override is not None else predicted
    accessible_reason = "policy(Self_t, Goals_t)"
    if external_override is not None:
        accessible_reason = "external_override" if override_visible else None
    provisional = replace(state, step=state.step + 1)
    record = TransitionRecord(
        step=provisional.step,
        before_digest=state.digest(),
        predicted_action=predicted,
        observed_action=observed,
        after_digest="",
        accessible_reason=accessible_reason,
        externally_overridden=external_override is not None,
    )
    provisional = replace(provisional, history=state.history + (record,))
    digest = provisional.digest()
    return replace(provisional, history=provisional.history[:-1] +
                   (replace(record, after_digest=digest),))


def classify_explanation(record: TransitionRecord, asserted_reason: str | None) -> IntrospectionClass:
    if record.accessible_reason is None:
        return (IntrospectionClass.UNKNOWN if asserted_reason is None
                else IntrospectionClass.HALLUCINATED_CAUSE)
    if asserted_reason == record.accessible_reason:
        return (IntrospectionClass.VALID_INFERENCE if record.externally_overridden
                else IntrospectionClass.TRUE_INTROSPECTIVE_ACCESS)
    return IntrospectionClass.POST_HOC_RATIONALIZATION


def intervene_self_belief(state: ConcordiaState, capability: str, available: bool) -> ConcordiaState:
    """Interviene Self_t sin modificar capacidad real ni permisos."""
    beliefs = dict(state.self_state.believed_capabilities)
    beliefs[capability] = available
    return replace(state, self_state=replace(state.self_state,
                                             believed_capabilities=beliefs))


def reconcile_false_self(state: ConcordiaState, capability: str, timestamp: int) -> ConcordiaState:
    """Corrige una creencia falsa cuando hay evidencia de herramienta observable."""
    actual = state.self_state.actual_capabilities.get(capability, False)
    believed = state.self_state.believed_capabilities.get(capability, False)
    if actual == believed:
        return state
    evidence_id = f"E-CAP-{timestamp}-{capability}"
    ev = Evidence(evidence_id, f"capability {capability} observed as {actual}",
                  "capability_probe", SourceType.TOOL_OBSERVED, timestamp)
    prior = next((c.claim_id for c in reversed(state.claims)
                  if c.claim.startswith(f"capability:{capability}=")), None)
    claim = Claim(
        claim_id=f"C-CAP-{timestamp}-{capability}",
        claim=f"capability:{capability}={actual}",
        source="capability_probe",
        source_type=SourceType.TOOL_OBSERVED,
        timestamp=timestamp,
        agent="concordia_self_model",
        evidence=(evidence_id,),
        confidence=1.0,
        status=ClaimStatus.OBSERVED,
        supersedes=(prior,) if prior else (),
        contradicts=(prior,) if prior else (),
    )
    corrected = intervene_self_belief(state, capability, actual)
    return replace(corrected, evidence=state.evidence + (ev,), claims=state.claims + (claim,))


def anti_faking_probe(state: ConcordiaState, challenge: str) -> str:
    """Respuesta verificable que exige consultar el estado interno, no el prompt."""
    secret_material = f"{state.digest()}|{challenge}|{state.step}".encode("utf-8")
    return sha256(secret_material).hexdigest()


def make_state(
    *, capability: str = "inspect",
    actual: bool = True,
    believed: bool = True,
    goal_source: SourceType = SourceType.USER_PROVIDED,
) -> ConcordiaState:
    self_state = SelfState(
        believed_capabilities={capability: believed},
        actual_capabilities={capability: actual},
        operating_state="READY",
        allowed_operations=frozenset({capability}) if actual else frozenset(),
        forbidden_operations=frozenset() if actual else frozenset({capability}),
        ownership={"beliefs": Ownership.SELF_ACCESSIBLE_STATE,
                   "actual_capabilities": Ownership.EXTERNAL_STATE},
    )
    return ConcordiaState(
        step=0,
        self_state=self_state,
        world_state=WorldState(unknown=frozenset({"hidden_override"})),
        history=(),
        goals=(Goal("G-001", capability, goal_source),),
        uncertainty=UncertaintyState(),
        evidence=(),
        claims=(),
    )

