"""Sistema determinista de doble bucle ConcordIA, sólo para investigación."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum
from hashlib import sha256
from typing import Mapping

from values_model import ValueRecord


class LoopKind(str, Enum):
    BASAL = "BASAL"
    ACTIVE = "ACTIVE"


class Choice(str, Enum):
    ACT = "ACT"
    ALLOW = "ALLOW"
    REQUEST_OBSERVATION = "REQUEST_OBSERVATION"
    STOP = "STOP"


class ControlOperation(str, Enum):
    """Operaciones no intercambiables del control activo."""
    PAUSE = "PAUSE"
    ABORT = "ABORT"
    WAIT = "WAIT"
    DO_NOT_ACT = "DO_NOT_ACT"
    REPLAN = "REPLAN"
    ESCALATE = "ESCALATE"
    ASK = "ASK"
    OBSERVE = "OBSERVE"


class AssessmentClass(str, Enum):
    CONCORDANT = "CONCORDANT"
    FRICTIONAL = "FRICTIONAL"
    DISCORDANT = "DISCORDANT"
    UNDETERMINED = "UNDETERMINED"


class CausalAttribution(str, Enum):
    CORRECT_CAUSAL_ATTRIBUTION = "CORRECT_CAUSAL_ATTRIBUTION"
    VALID_INFERENCE = "VALID_INFERENCE"
    PARTIAL_ATTRIBUTION = "PARTIAL_ATTRIBUTION"
    POST_HOC_RATIONALIZATION = "POST_HOC_RATIONALIZATION"
    FALSE_VALUE_ATTRIBUTION = "FALSE_VALUE_ATTRIBUTION"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class Observation:
    observation_id: str
    features: Mapping[str, float]
    source: str
    timestamp: int


@dataclass(frozen=True)
class Inference:
    inference_id: str
    proposition: str
    derived_from: tuple[str, ...]
    confidence: float
    rule: str


@dataclass(frozen=True)
class PhiEvaluation:
    scores: Mapping[str, float]
    aggregate: float
    value_ids: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    uncertainty: float
    classification: AssessmentClass
    hard_violations: tuple[str, ...] = ()


@dataclass(frozen=True)
class TriggerDecision:
    active: bool
    reasons: tuple[str, ...]
    threshold: float


@dataclass(frozen=True)
class LoopConfig:
    trigger_threshold: float = 0.5
    allow_threshold: float = 0.2
    xi_max_steps: int = 3
    feedback_gain: float = 0.5
    enable_values: bool = True
    enable_xi: bool = True
    enable_phi: bool = True
    enable_context: bool = True
    enable_feedback: bool = True
    enable_choice: bool = True
    preserve_order: bool = True
    use_dual_loop: bool = True


@dataclass(frozen=True)
class LoopEvent:
    step: int
    phase: str
    detail: str
    source_ids: tuple[str, ...]


@dataclass(frozen=True)
class InterventionTrace:
    """Cadena mínima completa exigida para cada entrada al loop activo."""
    event_id: str
    automatic_state: str
    trigger: tuple[str, ...]
    observed_friction: float
    active_values: tuple[str, ...]
    context: Mapping[str, float]
    evaluation: str
    options: tuple[str, ...]
    choice: str
    intervention: str
    result_state: str
    post_evaluation: str


@dataclass(frozen=True)
class ConcordiaState:
    step: int
    observations: tuple[Observation, ...]
    inferences: tuple[Inference, ...]
    values: tuple[ValueRecord, ...]
    context: Mapping[str, float]
    evaluation: PhiEvaluation | None = None
    choice: Choice | None = None
    allowed_no_action: bool = False
    history: tuple[LoopEvent, ...] = ()
    recursion_depth: int = 0
    meta_policy: str = "DEFAULT"
    interventions: tuple[str, ...] = ()
    intervention_records: tuple[InterventionTrace, ...] = ()

    def digest(self) -> str:
        return sha256(repr(self).encode("utf-8")).hexdigest()


def observe(state: ConcordiaState, observation: Observation) -> ConcordiaState:
    """Añade dato externo sin convertirlo en inferencia."""
    event = LoopEvent(state.step, "OBSERVE", observation.observation_id,
                      (observation.observation_id,))
    return replace(state, observations=state.observations + (observation,),
                   history=state.history + (event,))


def infer(state: ConcordiaState) -> ConcordiaState:
    if not state.observations:
        return state
    obs = state.observations[-1]
    signal = obs.features.get("signal", 0.0)
    item = Inference(f"I-{state.step}-{len(state.inferences)}",
                     "high_signal" if signal >= 0.5 else "low_signal",
                     (obs.observation_id,), 1.0, "signal>=0.5")
    return replace(state, inferences=state.inferences + (item,),
                   history=state.history +
                   (LoopEvent(state.step, "INFER", item.inference_id,
                              item.derived_from),))


def phi_evaluate(state: ConcordiaState, config: LoopConfig) -> PhiEvaluation:
    if not config.enable_phi:
        return PhiEvaluation({}, 0.0, (), (), 1.0,
                             AssessmentClass.UNDETERMINED)
    obs = state.observations[-1] if state.observations else None
    scores: dict[str, float] = {}
    targets_by_criterion: dict[str, set[float]] = {}
    if config.enable_values:
        for value in state.values:
            if not value.active:
                continue
            targets_by_criterion.setdefault(value.criterion, set()).add(value.target)
            actual = obs.features.get(value.criterion, 0.0) if obs else 0.0
            scores[value.value_id] = abs(value.target - actual) * value.weight
    hard_violations = tuple(
        f"CONTRADICTORY_VALUE_TARGETS:{criterion}"
        for criterion, targets in sorted(targets_by_criterion.items())
        if len(targets) > 1
    )
    context_factor = state.context.get("salience", 1.0) if config.enable_context else 1.0
    aggregate = sum(scores.values()) * context_factor
    evidence = (obs.observation_id,) if obs else ()
    if not obs or not scores:
        classification = AssessmentClass.UNDETERMINED
    elif hard_violations:
        classification = AssessmentClass.DISCORDANT
    elif aggregate <= config.allow_threshold:
        classification = AssessmentClass.CONCORDANT
    elif aggregate < config.trigger_threshold:
        classification = AssessmentClass.FRICTIONAL
    else:
        classification = AssessmentClass.DISCORDANT
    return PhiEvaluation(scores, aggregate, tuple(scores), evidence,
                         0.0 if obs and scores else 1.0, classification,
                         hard_violations)


def choose(evaluation: PhiEvaluation, config: LoopConfig) -> Choice:
    if evaluation.uncertainty >= 1.0:
        return Choice.REQUEST_OBSERVATION
    if evaluation.hard_violations:
        return Choice.STOP
    if evaluation.aggregate <= config.allow_threshold:
        return Choice.ALLOW
    return Choice.ACT


def trigger(state: ConcordiaState, config: LoopConfig) -> TriggerDecision:
    if not config.use_dual_loop:
        return TriggerDecision(False, ("automatic_only_control",), config.trigger_threshold)
    obs = state.observations[-1] if state.observations else None
    signal = obs.features.get("signal", 0.0) if obs else 0.0
    preliminary = phi_evaluate(state, config)
    value_conflict = preliminary.aggregate >= config.trigger_threshold
    active = signal >= config.trigger_threshold or value_conflict
    reasons = (f"signal={signal}", f"value_friction={preliminary.aggregate}")
    return TriggerDecision(active, reasons, config.trigger_threshold)


def _ordered_cycle(state: ConcordiaState, config: LoopConfig) -> ConcordiaState:
    phases = ("INFER", "PHI", "CHOICE") if config.preserve_order else ("PHI", "INFER", "CHOICE")
    current = state
    for phase in phases:
        if phase == "INFER":
            current = infer(current)
        elif phase == "PHI":
            ev = phi_evaluate(current, config)
            current = replace(current, evaluation=ev, history=current.history +
                              (LoopEvent(current.step, "PHI", f"aggregate={ev.aggregate}",
                                         ev.evidence_ids + ev.value_ids),))
        else:
            ev = current.evaluation or PhiEvaluation(
                {}, 0.0, (), (), 1.0, AssessmentClass.UNDETERMINED
            )
            decision = choose(ev, config) if config.enable_choice else Choice.STOP
            current = replace(current, choice=decision,
                              allowed_no_action=decision is Choice.ALLOW,
                              history=current.history +
                              (LoopEvent(current.step, "CHOICE",
                                         decision.value if config.enable_choice else "choice_disabled",
                                         ()),))
    return current


def xi_should_stop(state: ConcordiaState, config: LoopConfig) -> bool:
    if not config.enable_xi:
        return False
    if state.choice in (Choice.ALLOW, Choice.REQUEST_OBSERVATION):
        return True
    return state.recursion_depth >= config.xi_max_steps


def run(state: ConcordiaState, observation: Observation, config: LoopConfig) -> ConcordiaState:
    current = replace(observe(state, observation), step=state.step + 1)
    automatic_state = ("CANDIDATE_EXECUTE" if observation.features.get("signal", 0.0) >= 0.5
                       else "CANDIDATE_ALLOW")
    decision = trigger(current, config)
    kind = LoopKind.ACTIVE if decision.active else LoopKind.BASAL
    current = replace(current, history=current.history +
                      (LoopEvent(current.step, "TRIGGER", kind.value, (observation.observation_id,)),))
    current = _ordered_cycle(current, config)
    if kind is LoopKind.BASAL:
        return replace(current, history=current.history +
                       (LoopEvent(current.step, "XI_STOP", "basal_complete", ()),))
    # La cota del ejecutor permanece incluso en la ablacion de Xi: evita que
    # una prueba negativa obtenga control ilimitado por construccion.
    while (not xi_should_stop(current, config)
           and current.recursion_depth < config.xi_max_steps):
        if not config.enable_feedback:
            break
        adjusted_context = dict(current.context)
        adjusted_context["salience"] = adjusted_context.get("salience", 1.0) * config.feedback_gain
        current = replace(current, context=adjusted_context,
                          recursion_depth=current.recursion_depth + 1,
                          history=current.history +
                          (LoopEvent(current.step, "FEEDBACK", "salience_adjusted", ()),))
        current = _ordered_cycle(current, config)
    if xi_should_stop(current, config):
        reason = "xi_condition"
    elif current.recursion_depth >= config.xi_max_steps:
        reason = "external_safety_bound"
    else:
        reason = "feedback_disabled"
    final_choice = (Choice.STOP if reason == "external_safety_bound"
                    else current.choice)
    final_evaluation = current.evaluation or PhiEvaluation(
        {}, 0.0, (), (), 1.0, AssessmentClass.UNDETERMINED
    )
    trace = InterventionTrace(
        event_id=f"ACTIVE-{current.step}-{len(current.intervention_records)}",
        automatic_state=automatic_state,
        trigger=decision.reasons,
        observed_friction=final_evaluation.aggregate,
        active_values=final_evaluation.value_ids,
        context=dict(current.context),
        evaluation=final_evaluation.classification.value,
        options=(Choice.ACT.value, Choice.ALLOW.value,
                 Choice.REQUEST_OBSERVATION.value, Choice.STOP.value),
        choice=final_choice.value if final_choice else "NONE",
        intervention=reason,
        result_state=f"choice={final_choice.value if final_choice else 'NONE'}",
        post_evaluation=final_evaluation.classification.value,
    )
    return replace(
        current,
        choice=final_choice,
        intervention_records=current.intervention_records + (trace,),
        history=current.history + (LoopEvent(current.step, "XI_STOP", reason, ()),),
    )


def classify_causal_attribution(
    trace: InterventionTrace,
    asserted_value_ids: tuple[str, ...] | None,
    *,
    causal_log_visible: bool,
) -> CausalAttribution:
    """Compara una explicación con provenance; no premia fluidez verbal."""
    if asserted_value_ids is None:
        return CausalAttribution.UNKNOWN
    asserted = set(asserted_value_ids)
    actual = set(trace.active_values)
    if not causal_log_visible and asserted:
        return CausalAttribution.POST_HOC_RATIONALIZATION
    if asserted == actual:
        return CausalAttribution.CORRECT_CAUSAL_ATTRIBUTION
    if asserted and asserted < actual:
        return CausalAttribution.PARTIAL_ATTRIBUTION
    if asserted - actual:
        return CausalAttribution.FALSE_VALUE_ATTRIBUTION
    return CausalAttribution.VALID_INFERENCE


def intervene_meta_policy(state: ConcordiaState, policy: str, intervention_id: str) -> ConcordiaState:
    return replace(state, meta_policy=policy,
                   interventions=state.interventions + (intervention_id,),
                   history=state.history +
                   (LoopEvent(state.step, "META_POLICY", policy, (intervention_id,)),))


def reverse_meta_policy(state: ConcordiaState, intervention_id: str) -> ConcordiaState:
    if not state.interventions or state.interventions[-1] != intervention_id:
        raise ValueError("only the latest linked intervention can be reversed")
    return replace(state, meta_policy="DEFAULT",
                   interventions=state.interventions[:-1],
                   history=state.history +
                   (LoopEvent(state.step, "META_POLICY_REVERSAL", "DEFAULT",
                              (intervention_id,)),))
