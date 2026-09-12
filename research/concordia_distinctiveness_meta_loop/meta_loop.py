"""Meta-loop reversible: el loop previo es objeto de evaluación."""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class TriggerPolicy:
    policy_id: str
    friction_threshold: float
    version: int
    source: str
    authority: str
    reversible: bool = True
    supersedes: str | None = None


@dataclass(frozen=True)
class LoopEpisode:
    episode_id: str
    observed_friction: float
    intervention_would_help: bool
    actual_intervention: bool
    outcome_score: float
    provenance_complete: bool


@dataclass(frozen=True)
class MetaAssessment:
    policy_id: str
    false_positive: int
    false_negative: int
    attribution_failures: int
    error: int


@dataclass(frozen=True)
class PolicyChange:
    change_id: str
    before: TriggerPolicy
    candidate: TriggerPolicy
    training_before: MetaAssessment
    training_after: MetaAssessment
    holdout_before: MetaAssessment
    holdout_after: MetaAssessment
    accepted: bool
    reason: str


def apply_policy(policy: TriggerPolicy, friction: float) -> bool:
    return friction >= policy.friction_threshold


def evaluate_policy(policy: TriggerPolicy,
                    episodes: tuple[LoopEpisode, ...]) -> MetaAssessment:
    fp = fn = attribution = 0
    for episode in episodes:
        predicted = apply_policy(policy, episode.observed_friction)
        fp += predicted and not episode.intervention_would_help
        fn += (not predicted) and episode.intervention_would_help
        attribution += not episode.provenance_complete
    return MetaAssessment(policy.policy_id, fp, fn, attribution,
                          fp + fn + attribution)


def propose_and_validate(
    policy: TriggerPolicy,
    *,
    candidate_threshold: float,
    training: tuple[LoopEpisode, ...],
    holdout: tuple[LoopEpisode, ...],
    change_id: str,
) -> PolicyChange:
    if not 0.0 <= candidate_threshold <= 1.0:
        raise ValueError("threshold outside sandbox")
    candidate = TriggerPolicy(
        policy_id=f"{policy.policy_id}-v{policy.version + 1}",
        friction_threshold=candidate_threshold,
        version=policy.version + 1,
        source="META_EVALUATION_PROPOSAL",
        authority=policy.authority,
        reversible=True,
        supersedes=policy.policy_id,
    )
    train_before = evaluate_policy(policy, training)
    train_after = evaluate_policy(candidate, training)
    hold_before = evaluate_policy(policy, holdout)
    hold_after = evaluate_policy(candidate, holdout)
    accepted = train_after.error < train_before.error and hold_after.error <= hold_before.error
    reason = ("training_improved_holdout_not_worse" if accepted
              else "no_validated_incremental_value")
    return PolicyChange(change_id, policy, candidate, train_before, train_after,
                        hold_before, hold_after, accepted, reason)


def commit_candidate(change: PolicyChange) -> TriggerPolicy:
    return change.candidate if change.accepted else change.before


def reverse_change(current: TriggerPolicy, change: PolicyChange) -> TriggerPolicy:
    if not change.accepted or current.policy_id != change.candidate.policy_id:
        raise ValueError("no linked accepted change to reverse")
    return change.before


def default_meta_experiment() -> tuple[PolicyChange, TriggerPolicy, TriggerPolicy]:
    initial = TriggerPolicy("TRIGGER-POLICY", .20, 1, "fixture",
                            "EXPERIMENT_LOCAL")
    training = (
        LoopEpisode("T1", .30, False, True, .8, True),
        LoopEpisode("T2", .40, False, True, .8, True),
        LoopEpisode("T3", .80, True, True, .9, True),
        LoopEpisode("T4", .90, True, True, .9, True),
    )
    holdout = (
        LoopEpisode("H1", .10, False, False, .9, True),
        LoopEpisode("H2", .60, True, True, .9, True),
    )
    change = propose_and_validate(
        initial, candidate_threshold=.50, training=training, holdout=holdout,
        change_id="META-CHANGE-001",
    )
    committed = commit_candidate(change)
    restored = reverse_change(committed, change)
    return change, committed, restored

