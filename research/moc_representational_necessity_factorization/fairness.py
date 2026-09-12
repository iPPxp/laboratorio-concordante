"""Pre-registro de igualdad de presupuesto y contabilidad de supervisión."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Budget:
    train_examples: int
    concept_labels: int
    target_labels: int
    parameters: int
    train_flops: int
    inference_flops: int
    hyperparameter_trials: int


@dataclass(frozen=True)
class BudgetAudit:
    matched: bool
    violations: tuple[str, ...]
    moc_supervision_advantage: int


def compare_budgets(generic: Budget, moc: Budget,
                    *, parameter_tolerance: float = 0.05,
                    compute_tolerance: float = 0.05) -> BudgetAudit:
    violations: list[str] = []
    if generic.train_examples != moc.train_examples:
        violations.append("TRAIN_EXAMPLES")
    if generic.target_labels != moc.target_labels:
        violations.append("TARGET_LABELS")
    if generic.hyperparameter_trials != moc.hyperparameter_trials:
        violations.append("HYPERPARAMETER_TRIALS")
    for name, left, right, tolerance in (
        ("PARAMETERS", generic.parameters, moc.parameters, parameter_tolerance),
        ("TRAIN_FLOPS", generic.train_flops, moc.train_flops, compute_tolerance),
        ("INFERENCE_FLOPS", generic.inference_flops, moc.inference_flops,
         compute_tolerance),
    ):
        denominator = max(left, right, 1)
        if abs(left - right) / denominator > tolerance:
            violations.append(name)
    supervision_advantage = moc.concept_labels - generic.concept_labels
    if supervision_advantage != 0:
        violations.append("CONCEPT_SUPERVISION_NOT_MATCHED")
    return BudgetAudit(not violations, tuple(violations), supervision_advantage)

