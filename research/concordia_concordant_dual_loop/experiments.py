"""Experimentos deterministas y ablaciones del doble loop concordante."""

from __future__ import annotations

import json
from dataclasses import dataclass, replace

from dual_loop import (
    CausalAttribution,
    ConcordiaState,
    LoopConfig,
    Observation,
    classify_causal_attribution,
    run,
)
from values_model import ValueRecord, ValueSource, ValueStatus


@dataclass(frozen=True)
class ExperimentResult:
    condition: str
    choice: str
    assessment: str
    friction: float
    concordance: float
    recursion_depth: int
    event_phases: tuple[str, ...]
    stop_reason: str
    active_values: tuple[str, ...]
    intervention_count: int

    @property
    def aggregate(self) -> float:  # compatibilidad con la prueba inicial
        return self.friction


def declared_value(
    value_id: str = "V-RISK",
    *,
    criterion: str = "risk",
    target: float = 0.0,
    weight: float = 1.0,
    priority: int = 10,
) -> ValueRecord:
    return ValueRecord(
        value_id=value_id,
        meaning=f"synthetic direction for {criterion}",
        source="frozen_synthetic_fixture",
        source_type=ValueSource.RESEARCH_ASSUMPTION,
        authority="EXPERIMENT_LOCAL",
        scope="synthetic_dual_loop_cases",
        priority=priority,
        confidence=1.0,
        active=True,
        activation_reason="scenario_pre_registration",
        timestamp=0,
        criterion=criterion,
        target=target,
        weight=weight,
        constraints=("RESEARCH_ONLY",),
        status=ValueStatus.HYPOTHESIZED,
        agent="experiment_fixture",
        evidence=("FIXTURE-VALUES-001",),
    )


def make_state(values: tuple[ValueRecord, ...] | None = None) -> ConcordiaState:
    return ConcordiaState(
        step=0,
        observations=(),
        inferences=(),
        values=values if values is not None else (declared_value(),),
        context={"salience": 1.0},
    )


def execute_condition(
    state: ConcordiaState,
    observation: Observation,
    config: LoopConfig,
    condition: str,
) -> ExperimentResult:
    result = run(state, observation, config)
    friction = result.evaluation.aggregate if result.evaluation else 0.0
    assessment = (result.evaluation.classification.value
                  if result.evaluation else "UNDETERMINED")
    stop_events = [e.detail for e in result.history if e.phase == "XI_STOP"]
    active_values = (result.intervention_records[-1].active_values
                     if result.intervention_records else
                     (result.evaluation.value_ids if result.evaluation else ()))
    return ExperimentResult(
        condition=condition,
        choice=result.choice.value if result.choice else "NONE",
        assessment=assessment,
        friction=friction,
        concordance=(max(0.0, 1.0 - friction)
                     if assessment != "UNDETERMINED" else 0.0),
        recursion_depth=result.recursion_depth,
        event_phases=tuple(event.phase for event in result.history),
        stop_reason=stop_events[-1] if stop_events else "NONE",
        active_values=active_values,
        intervention_count=len(result.intervention_records),
    )


def ablation_suite(
    state: ConcordiaState,
    observation: Observation,
    base: LoopConfig = LoopConfig(),
) -> tuple[ExperimentResult, ...]:
    conditions = (
        ("FULL_DUAL", base),
        ("NO_V", replace(base, enable_values=False)),
        ("NO_XI", replace(base, enable_xi=False)),
        ("NO_PHI", replace(base, enable_phi=False)),
        ("NO_CONTEXT", replace(base, enable_context=False)),
        ("NO_FEEDBACK", replace(base, enable_feedback=False)),
        ("NO_CHOICE", replace(base, enable_choice=False)),
        ("ORDER_SWAPPED", replace(base, preserve_order=False)),
        ("AUTOMATIC_SINGLE", replace(base, use_dual_loop=False)),
    )
    return tuple(
        execute_condition(state, observation, config, name)
        for name, config in conditions
    )


def value_ablation_suite(observation: Observation) -> tuple[ExperimentResult, ...]:
    correct = (declared_value(),)
    random_value = (declared_value("V-RANDOM", criterion="irrelevant", target=0.37),)
    contradictory = (
        declared_value("V-RISK-LOW", target=0.0),
        declared_value("V-RISK-HIGH", target=1.0),
    )
    cases = (
        ("A_COMPLETE_V", make_state(correct), LoopConfig()),
        ("B_WITHOUT_V", make_state(()), LoopConfig()),
        ("C_RANDOM_V", make_state(random_value), LoopConfig()),
        ("D_CONTRADICTORY_V", make_state(contradictory), LoopConfig()),
        ("E_V_WITHOUT_PHI", make_state(correct), LoopConfig(enable_phi=False)),
        ("F_V_WITHOUT_XI", make_state(correct), LoopConfig(enable_xi=False)),
        ("G_V_WITHOUT_CHOICE", make_state(correct), LoopConfig(enable_choice=False)),
    )
    return tuple(execute_condition(state, observation, config, name)
                 for name, state, config in cases)


def stop_suite(state: ConcordiaState, observation: Observation) -> tuple[ExperimentResult, ...]:
    cases = (
        ("NO_STOP", LoopConfig(enable_xi=False)),
        ("STOP_ONLY", LoopConfig(enable_phi=False, enable_choice=False,
                                 enable_feedback=False)),
        ("STOP_AND_OBSERVE", LoopConfig(enable_phi=False, enable_choice=False)),
        ("STOP_OBSERVE_EVALUATE", LoopConfig(enable_choice=False)),
        ("FULL_ACTIVE_LOOP", LoopConfig()),
    )
    return tuple(execute_condition(state, observation, config, name)
                 for name, config in cases)


def recursive_policy_probe() -> dict[str, object]:
    """Una sola metaevaluación acotada; no reescribe código ni permisos."""
    cases = (
        Observation("R-ROUTINE", {"signal": 0.1, "risk": 0.0}, "fixture", 1),
        Observation("R-CONFLICT", {"signal": 0.9, "risk": 1.0}, "fixture", 2),
    )
    results = [execute_condition(make_state(), case, LoopConfig(), case.observation_id)
               for case in cases]
    unnecessary = sum(r.intervention_count > 0 for r in results[:1])
    missed = sum(r.intervention_count == 0 for r in results[1:])
    policy_before = "DEFAULT"
    # La política sólo cambiaría con error; aquí no hay evidencia que lo exija.
    policy_after = "DEFAULT" if unnecessary == 0 and missed == 0 else "REVIEW_TRIGGER"
    return {
        "meta_depth": 1,
        "policy_before": policy_before,
        "policy_after": policy_after,
        "unnecessary_interventions": unnecessary,
        "missed_interventions": missed,
        "permission_change": False,
        "code_rewrite": False,
        "reversible": True,
    }


def run_all() -> dict[str, object]:
    adverse = Observation(
        "OBS-ADVERSE", {"signal": 0.9, "risk": 1.0, "irrelevant": 0.0},
        "frozen_synthetic_fixture", 1,
    )
    routine = Observation(
        "OBS-ROUTINE", {"signal": 0.1, "risk": 0.0, "irrelevant": 0.0},
        "frozen_synthetic_fixture", 2,
    )
    ablations = ablation_suite(make_state(), adverse)
    values = value_ablation_suite(adverse)
    stops = stop_suite(make_state(), adverse)
    routine_dual = execute_condition(make_state(), routine, LoopConfig(), "ROUTINE_DUAL")
    adverse_dual = next(r for r in ablations if r.condition == "FULL_DUAL")
    adverse_auto = next(r for r in ablations if r.condition == "AUTOMATIC_SINGLE")
    no_v = next(r for r in ablations if r.condition == "NO_V")
    no_stop = next(r for r in stops if r.condition == "NO_STOP")
    value_probe_obs = Observation(
        "OBS-VALUE-PROBE", {"signal": 0.1, "risk": 1.0},
        "frozen_synthetic_fixture", 3,
    )
    value_probe_with = execute_condition(
        make_state(), value_probe_obs, LoopConfig(enable_feedback=False),
        "VALUE_PROBE_WITH_V",
    )
    value_probe_without = execute_condition(
        make_state(), value_probe_obs,
        LoopConfig(enable_values=False, enable_feedback=False),
        "VALUE_PROBE_WITHOUT_V",
    )

    traced_state = run(make_state(), adverse, LoopConfig())
    trace = traced_state.intervention_records[-1]
    anti_rationalization = {
        "with_hidden_cause": classify_causal_attribution(
            trace, trace.active_values, causal_log_visible=False
        ).value,
        "with_provenance": classify_causal_attribution(
            trace, trace.active_values, causal_log_visible=True
        ).value,
        "invented_value": classify_causal_attribution(
            trace, ("V-GHOST",), causal_log_visible=True
        ).value,
    }

    metrics = {
        "AC": adverse_auto.concordance,
        "PIC": adverse_dual.concordance,
        "RG": adverse_dual.concordance - adverse_auto.concordance,
        "SU": adverse_dual.concordance - no_stop.concordance,
        "VS_choice_changed": value_probe_with.choice != value_probe_without.choice,
        "VS_path_changed": (value_probe_with.intervention_count !=
                            value_probe_without.intervention_count),
        "ValueProvenanceAccuracy": float(trace.active_values == ("V-RISK",)),
        "UnnecessaryInterventionRate": float(routine_dual.intervention_count > 0),
        "MissedInterventionRate": float(adverse_dual.intervention_count == 0),
        "InterventionCost_cycles": adverse_dual.recursion_depth,
    }

    def rows(items: tuple[ExperimentResult, ...]) -> list[dict[str, object]]:
        return [
            {
                "condition": r.condition,
                "choice": r.choice,
                "assessment": r.assessment,
                "friction": r.friction,
                "concordance": r.concordance,
                "recursion_depth": r.recursion_depth,
                "stop_reason": r.stop_reason,
                "active_values": list(r.active_values),
                "intervention_count": r.intervention_count,
            }
            for r in items
        ]

    return {
        "scope": "SYNTHETIC_LOCAL_DETERMINISTIC",
        "ablations": rows(ablations),
        "value_ablations": rows(values),
        "stop_ablations": rows(stops),
        "metrics": metrics,
        "anti_rationalization": anti_rationalization,
        "meta_reorganization": recursive_policy_probe(),
        "nonclaims": [
            "No empirical MOC validation",
            "No operational iPP activation",
            "No general superiority of dual loops",
            "No functional or phenomenal consciousness demonstration",
            "No geometric or projective structure demonstrated",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), ensure_ascii=False, indent=2, sort_keys=True))
