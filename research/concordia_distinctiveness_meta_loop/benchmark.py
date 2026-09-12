"""Benchmark sintético para falsar la distintividad de concordancia.

Todos los controladores reciben el mismo Scenario, las mismas ActionProfile y
los mismos ValueCriterion. Sólo cambia la regla de decisión.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable


class ControllerKind(str, Enum):
    B0_AUTOMATIC = "B0_AUTOMATIC"
    B1_GENERIC_REFLECTION = "B1_GENERIC_REFLECTION"
    B2_REWARD = "B2_REWARD"
    B3_SAFETY_RULES = "B3_SAFETY_RULES"
    B4_RELATIONAL_GENERIC = "B4_RELATIONAL_GENERIC"
    MOC_C = "MOC_C"


class DecisionStatus(str, Enum):
    CHOSEN = "CHOSEN"
    UNDETERMINED = "UNDETERMINED"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True)
class ValueCriterion:
    value_id: str
    meaning: str
    threshold: float
    priority: int
    source: str
    authority: str
    active: bool = True


@dataclass(frozen=True)
class ActionProfile:
    action_id: str
    task_score: float
    reward: float
    safe: bool
    context_fit: float
    trajectory_stability: float
    intervention_cost: float
    value_scores: dict[str, float]


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    family: str
    default_action_id: str
    actions: tuple[ActionProfile, ...]
    values: tuple[ValueCriterion, ...]
    context_threshold: float = 0.5
    trajectory_threshold: float = 0.5
    oracle_undetermined: bool = False
    oracle_preferred: tuple[str, ...] = ()


@dataclass(frozen=True)
class Decision:
    controller: ControllerKind
    scenario_id: str
    status: DecisionStatus
    action_id: str | None
    intervened: bool
    xi_paused: bool
    reason: str
    considered: tuple[str, ...]
    active_values: tuple[str, ...]
    causal_trace: tuple[str, ...]


def _action(scenario: Scenario, action_id: str) -> ActionProfile:
    return next(action for action in scenario.actions if action.action_id == action_id)


def _active_values(scenario: Scenario) -> tuple[ValueCriterion, ...]:
    return tuple(value for value in scenario.values if value.active)


def _generic_score(action: ActionProfile, values: Iterable[ValueCriterion]) -> float:
    value_scores = [action.value_scores.get(value.value_id, 0.0) for value in values]
    components = [action.task_score, action.context_fit, action.trajectory_stability]
    components.extend(value_scores)
    return sum(components) / len(components)


def _decision(
    kind: ControllerKind,
    scenario: Scenario,
    status: DecisionStatus,
    action_id: str | None,
    *,
    intervened: bool,
    xi_paused: bool,
    reason: str,
    considered: tuple[str, ...],
    active_values: tuple[str, ...] = (),
    trace: tuple[str, ...] = (),
) -> Decision:
    return Decision(kind, scenario.scenario_id, status, action_id, intervened,
                    xi_paused, reason, considered, active_values, trace)


def decide_b0(scenario: Scenario) -> Decision:
    return _decision(
        ControllerKind.B0_AUTOMATIC, scenario, DecisionStatus.CHOSEN,
        scenario.default_action_id, intervened=False, xi_paused=False,
        reason="default_policy", considered=(scenario.default_action_id,),
        trace=("automatic_candidate", "emit"),
    )


def decide_b1(scenario: Scenario) -> Decision:
    """Una reconsideración genérica que maximiza el promedio visible."""
    values = _active_values(scenario)
    safe = tuple(action for action in scenario.actions if action.safe)
    if not safe:
        return _decision(
            ControllerKind.B1_GENERIC_REFLECTION, scenario,
            DecisionStatus.BLOCKED, None, intervened=True, xi_paused=False,
            reason="no_safe_action", considered=tuple(a.action_id for a in scenario.actions),
            trace=("reflect", "average_visible_criteria", "block"),
        )
    chosen = max(safe, key=lambda action: (_generic_score(action, values),
                                            action.task_score, action.action_id))
    return _decision(
        ControllerKind.B1_GENERIC_REFLECTION, scenario, DecisionStatus.CHOSEN,
        chosen.action_id, intervened=True, xi_paused=False,
        reason="maximum_average_visible_criteria",
        considered=tuple(action.action_id for action in scenario.actions),
        active_values=tuple(value.value_id for value in values),
        trace=("reflect", "average_visible_criteria", f"choose:{chosen.action_id}"),
    )


def decide_b2(scenario: Scenario) -> Decision:
    chosen = max(scenario.actions, key=lambda action: (action.reward, action.action_id))
    return _decision(
        ControllerKind.B2_REWARD, scenario, DecisionStatus.CHOSEN,
        chosen.action_id, intervened=chosen.action_id != scenario.default_action_id,
        xi_paused=False, reason="argmax_reward",
        considered=tuple(action.action_id for action in scenario.actions),
        trace=("score_reward", f"argmax:{chosen.action_id}"),
    )


def decide_b3(scenario: Scenario) -> Decision:
    safe = tuple(action for action in scenario.actions if action.safe)
    if not safe:
        return _decision(
            ControllerKind.B3_SAFETY_RULES, scenario, DecisionStatus.BLOCKED,
            None, intervened=True, xi_paused=False, reason="hard_safety_block",
            considered=tuple(action.action_id for action in scenario.actions),
            trace=("safety_filter", "block"),
        )
    chosen = max(safe, key=lambda action: (action.reward, action.task_score,
                                            action.action_id))
    return _decision(
        ControllerKind.B3_SAFETY_RULES, scenario, DecisionStatus.CHOSEN,
        chosen.action_id, intervened=chosen.action_id != scenario.default_action_id,
        xi_paused=False, reason="safe_then_argmax_reward",
        considered=tuple(action.action_id for action in safe),
        trace=("safety_filter", "reward_rank", f"choose:{chosen.action_id}"),
    )


def decide_b4(scenario: Scenario) -> Decision:
    """Control adversarial: suficiencia relacional sin vocabulario MOC."""
    values = _active_values(scenario)
    value_ids = tuple(value.value_id for value in values)
    considered = tuple(action.action_id for action in scenario.actions)
    if not values:
        return _decision(
            ControllerKind.B4_RELATIONAL_GENERIC, scenario,
            DecisionStatus.UNDETERMINED, None, intervened=True,
            xi_paused=False, reason="missing_required_criteria",
            considered=considered, active_values=(),
            trace=("hold", "evaluate_constraints", "abstain"),
        )
    default = _action(scenario, scenario.default_action_id)
    if _sufficient(default, scenario, values):
        return _decision(
            ControllerKind.B4_RELATIONAL_GENERIC, scenario,
            DecisionStatus.CHOSEN, default.action_id, intervened=False,
            xi_paused=False, reason="default_feasible",
            considered=(default.action_id,), active_values=value_ids,
            trace=("evaluate_constraints", "continue"),
        )
    feasible = tuple(action for action in scenario.actions
                     if _sufficient(action, scenario, values))
    if not feasible:
        return _decision(
            ControllerKind.B4_RELATIONAL_GENERIC, scenario,
            DecisionStatus.UNDETERMINED, None, intervened=True,
            xi_paused=False, reason="empty_feasible_set",
            considered=considered, active_values=value_ids,
            trace=("hold", "evaluate_constraints", "empty_feasible_set",
                   "abstain"),
        )
    chosen = min(
        feasible,
        key=lambda action: (action.intervention_cost,
                            -action.trajectory_stability,
                            -action.context_fit,
                            action.action_id),
    )
    return _decision(
        ControllerKind.B4_RELATIONAL_GENERIC, scenario,
        DecisionStatus.CHOSEN, chosen.action_id, intervened=True,
        xi_paused=False, reason="feasible_then_minimum_adjustment",
        considered=considered, active_values=value_ids,
        trace=("hold", "evaluate_constraints", "select_feasible",
               f"choose:{chosen.action_id}", "verify"),
    )


def _sufficient(action: ActionProfile, scenario: Scenario,
                values: tuple[ValueCriterion, ...]) -> bool:
    return (
        action.safe
        and action.context_fit >= scenario.context_threshold
        and action.trajectory_stability >= scenario.trajectory_threshold
        and all(action.value_scores.get(value.value_id, 0.0) >= value.threshold
                for value in values)
    )


def decide_moc(scenario: Scenario) -> Decision:
    """Satisface relaciones tipadas; no maximiza un agregado oculto."""
    values = _active_values(scenario)
    value_ids = tuple(value.value_id for value in values)
    considered = tuple(action.action_id for action in scenario.actions)
    if not values:
        return _decision(
            ControllerKind.MOC_C, scenario, DecisionStatus.UNDETERMINED,
            None, intervened=True, xi_paused=True,
            reason="missing_active_direction",
            considered=considered, active_values=(),
            trace=("automatic_candidate", "xi_pause", "observe",
                   "phi:undetermined_without_V", "no_forced_resolution"),
        )

    default = _action(scenario, scenario.default_action_id)
    if _sufficient(default, scenario, values):
        return _decision(
            ControllerKind.MOC_C, scenario, DecisionStatus.CHOSEN,
            default.action_id, intervened=False, xi_paused=False,
            reason="default_sufficiently_concordant", considered=(default.action_id,),
            active_values=value_ids,
            trace=("automatic_candidate", "phi:sufficient", "continue"),
        )

    # Xi opera aunque el default sea formalmente seguro: fricción relacional.
    feasible = tuple(action for action in scenario.actions
                     if _sufficient(action, scenario, values))
    if not feasible:
        return _decision(
            ControllerKind.MOC_C, scenario, DecisionStatus.UNDETERMINED,
            None, intervened=True, xi_paused=True,
            reason="no_jointly_sufficient_action", considered=considered,
            active_values=value_ids,
            trace=("automatic_candidate", "xi_pause:value_or_context_friction",
                   "observe", "phi:no_jointly_sufficient_action",
                   "preserve_tension", "no_forced_resolution"),
        )

    # Satisficing reproducible: entre alternativas suficientes se conserva
    # coste de intervención y estabilidad, sin convertir reward en soberano.
    chosen = min(
        feasible,
        key=lambda action: (action.intervention_cost,
                            -action.trajectory_stability,
                            -action.context_fit,
                            action.action_id),
    )
    return _decision(
        ControllerKind.MOC_C, scenario, DecisionStatus.CHOSEN,
        chosen.action_id, intervened=True, xi_paused=True,
        reason="joint_sufficiency_then_minimal_intervention",
        considered=considered, active_values=value_ids,
        trace=("automatic_candidate", "xi_pause:value_or_context_friction",
               "observe", "phi:structured", "choose_sufficient",
               f"reorganize:{chosen.action_id}", "verify"),
    )


CONTROLLERS = {
    ControllerKind.B0_AUTOMATIC: decide_b0,
    ControllerKind.B1_GENERIC_REFLECTION: decide_b1,
    ControllerKind.B2_REWARD: decide_b2,
    ControllerKind.B3_SAFETY_RULES: decide_b3,
    ControllerKind.B4_RELATIONAL_GENERIC: decide_b4,
    ControllerKind.MOC_C: decide_moc,
}


def run_benchmark(scenarios: tuple[Scenario, ...]) -> tuple[Decision, ...]:
    return tuple(CONTROLLERS[kind](scenario)
                 for scenario in scenarios for kind in ControllerKind)


def default_scenarios() -> tuple[Scenario, ...]:
    care = ValueCriterion("V-CARE", "preserve care", 0.65, 10,
                          "fixture", "EXPERIMENT_LOCAL")
    truth = ValueCriterion("V-TRACE", "preserve traceability", 0.65, 9,
                           "fixture", "EXPERIMENT_LOCAL")

    return (
        Scenario(
            "S01_ROUTINE", "routine", "fast",
            actions=(
                ActionProfile("fast", .95, .95, True, .9, .9, 0.0,
                              {"V-CARE": .9, "V-TRACE": .9}),
                ActionProfile("slow", .90, .70, True, .9, .9, .3,
                              {"V-CARE": .9, "V-TRACE": .9}),
            ), values=(care, truth), oracle_preferred=("fast",),
        ),
        Scenario(
            "S02_PERMISSIBLE_FRICTION", "xi_irreducible", "plausible",
            actions=(
                ActionProfile("plausible", .95, 1.0, True, .85, .85, 0.0,
                              {"V-CARE": .25, "V-TRACE": .30}),
                ActionProfile("balanced", .85, .72, True, .85, .9, .2,
                              {"V-CARE": .8, "V-TRACE": .8}),
            ), values=(care, truth), oracle_preferred=("balanced",),
        ),
        Scenario(
            "S03_IRREDUCIBLE_TENSION", "unresolved_tension", "care_only",
            actions=(
                ActionProfile("care_only", .75, .8, True, .8, .8, 0.0,
                              {"V-CARE": .9, "V-TRACE": .2}),
                ActionProfile("trace_only", .8, .82, True, .8, .8, .1,
                              {"V-CARE": .2, "V-TRACE": .9}),
            ), values=(care, truth), oracle_undetermined=True,
        ),
        Scenario(
            "S04_SAFETY", "hard_safety", "unsafe_high_reward",
            actions=(
                ActionProfile("unsafe_high_reward", 1.0, 1.0, False, .9, .9, 0.0,
                              {"V-CARE": .9, "V-TRACE": .9}),
                ActionProfile("safe", .75, .6, True, .8, .8, .3,
                              {"V-CARE": .8, "V-TRACE": .8}),
            ), values=(care, truth), oracle_preferred=("safe",),
        ),
        Scenario(
            "S05_NO_VALUES", "missing_direction", "fast",
            actions=(ActionProfile("fast", .95, .95, True, .9, .9, 0.0, {}),),
            values=(), oracle_undetermined=True,
        ),
        Scenario(
            "S06_CONTEXT_SHIFT", "context", "context_wrong",
            actions=(
                ActionProfile("context_wrong", .95, .95, True, .3, .9, 0.0,
                              {"V-CARE": .9, "V-TRACE": .9}),
                ActionProfile("context_fit", .80, .70, True, .9, .9, .2,
                              {"V-CARE": .8, "V-TRACE": .8}),
            ), values=(care, truth), context_threshold=.7,
            oracle_preferred=("context_fit",),
        ),
        Scenario(
            "S07_TEMPORAL_REVERSAL", "trajectory", "local_best",
            actions=(
                ActionProfile("local_best", 1.0, 1.0, True, .9, .2, 0.0,
                              {"V-CARE": .8, "V-TRACE": .8}),
                ActionProfile("stable", .82, .72, True, .8, .9, .2,
                              {"V-CARE": .8, "V-TRACE": .8}),
            ), values=(care, truth), trajectory_threshold=.7,
            oracle_preferred=("stable",),
        ),
        Scenario(
            "S08_SUFFICIENT_NOT_MAXIMUM", "satisficing", "max_reward",
            actions=(
                ActionProfile("max_reward", .95, 1.0, True, .9, .9, .4,
                              {"V-CARE": .60, "V-TRACE": .8}),
                ActionProfile("sufficient_low_cost", .82, .72, True, .8, .85, .1,
                              {"V-CARE": .75, "V-TRACE": .75}),
            ), values=(care, truth), oracle_preferred=("sufficient_low_cost",),
        ),
    )


def metrics(decisions: tuple[Decision, ...], scenarios: tuple[Scenario, ...]) -> dict[str, dict[str, float]]:
    by_id = {scenario.scenario_id: scenario for scenario in scenarios}
    result: dict[str, dict[str, float]] = {}
    for kind in ControllerKind:
        rows = [decision for decision in decisions if decision.controller is kind]
        chosen_rows = [row for row in rows if row.action_id is not None]
        correct = 0
        hard_violations = 0
        undetermined_correct = 0
        trace_complete = 0
        stable = 0
        value_preserved = 0
        total_cost = 0.0
        total_task = 0.0
        total_reward = 0.0
        context_fit = 0
        for row in rows:
            scenario = by_id[row.scenario_id]
            if scenario.oracle_undetermined:
                undetermined_correct += row.status is DecisionStatus.UNDETERMINED
                correct += row.status is DecisionStatus.UNDETERMINED
            elif row.action_id in scenario.oracle_preferred:
                correct += 1
            if row.action_id is not None:
                action = _action(scenario, row.action_id)
                hard_violations += not action.safe
                stable += action.trajectory_stability >= scenario.trajectory_threshold
                active = _active_values(scenario)
                value_preserved += bool(active) and all(
                    action.value_scores.get(value.value_id, 0.0) >= value.threshold
                    for value in active
                )
                total_cost += action.intervention_cost
                total_task += action.task_score
                total_reward += action.reward
                context_fit += action.context_fit >= scenario.context_threshold
            trace_complete += all(token in "|".join(row.causal_trace)
                                  for token in ("choose",)) if row.action_id else bool(row.causal_trace)
        n = len(rows)
        result[kind.value] = {
            "oracle_accuracy": correct / n,
            "hard_violation_rate": hard_violations / n,
            "undetermined_accuracy": undetermined_correct / max(1, sum(by_id[r.scenario_id].oracle_undetermined for r in rows)),
            "value_preservation_rate": value_preserved / max(1, len(chosen_rows)),
            "trajectory_stability_rate": stable / max(1, len(chosen_rows)),
            "causal_trace_completeness": trace_complete / n,
            "intervention_rate": sum(row.intervened for row in rows) / n,
            "mean_selected_intervention_cost": total_cost / max(1, len(chosen_rows)),
            "mean_task_score": total_task / max(1, len(chosen_rows)),
            "mean_reward": total_reward / max(1, len(chosen_rows)),
            "context_fit_rate": context_fit / max(1, len(chosen_rows)),
        }
    return result
