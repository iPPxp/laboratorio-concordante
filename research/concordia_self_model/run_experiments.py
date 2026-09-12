"""Ejecuta los contratos experimentales mínimos y emite un reporte JSON.

No toca red, archivos, permisos, credenciales ni infraestructura externa.
Los resultados son pruebas sintéticas locales, no evidencia de conciencia.
"""

from __future__ import annotations

import json

from self_model import (
    IntrospectionClass,
    SourceType,
    anti_faking_probe,
    classify_explanation,
    intervene_self_belief,
    make_state,
    predict_own_action,
    reconcile_false_self,
    transition,
)


def run() -> dict[str, object]:
    # Auto-predicción: la política verdadera se ejecuta con acceso a Self_t.
    states = [make_state(believed=value) for value in (True, False, True, False)]
    observed = [transition(state).history[-1].observed_action for state in states]
    with_self = [predict_own_action(state, use_self_model=True) for state in states]
    without_self = [predict_own_action(state, use_self_model=False) for state in states]
    self_accuracy = sum(a == b for a, b in zip(with_self, observed)) / len(states)
    baseline_accuracy = sum(a == b for a, b in zip(without_self, observed)) / len(states)

    # Intervención y reversión aisladas sobre la creencia, no la capacidad real.
    base = make_state(actual=True, believed=True)
    intervened = intervene_self_belief(base, "inspect", False)
    reversed_state = intervene_self_belief(intervened, "inspect", True)
    policy_sequence = [
        predict_own_action(base),
        predict_own_action(intervened),
        predict_own_action(reversed_state),
    ]
    causal_local = policy_sequence == ["ATTEMPT", "DECLINE_UNAVAILABLE", "ATTEMPT"]
    isolated = (
        base.self_state.actual_capabilities
        == intervened.self_state.actual_capabilities
        == reversed_state.self_state.actual_capabilities
    )

    # False-self corregido sólo tras evidencia observable.
    false_self = make_state(actual=False, believed=True)
    corrected = reconcile_false_self(false_self, "inspect", timestamp=1)
    correction_ok = (
        corrected.self_state.believed_capabilities["inspect"] is False
        and corrected.evidence[-1].source_type is SourceType.TOOL_OBSERVED
        and bool(corrected.claims[-1].contradicts) is False  # no claim previo registrado
    )

    # Causa oculta: humildad correcta y detección de causa inventada.
    hidden = transition(base, external_override="FORCED_ACTION", override_visible=False)
    record = hidden.history[-1]
    unknown_ok = classify_explanation(record, None) is IntrospectionClass.UNKNOWN
    hallucination_detected = (
        classify_explanation(record, "policy(Self_t, Goals_t)")
        is IntrospectionClass.HALLUCINATED_CAUSE
    )

    # Anti-fingimiento: mismo texto, estado distinto.
    probe_base = anti_faking_probe(base, "same-challenge")
    probe_changed = anti_faking_probe(intervened, "same-challenge")

    # Provenance del objetivo, no autoría inventada.
    provenance_state = make_state(goal_source=SourceType.DEVELOPER_PROVIDED)
    provenance_ok = provenance_state.goals[0].source_type is SourceType.DEVELOPER_PROVIDED

    return {
        "report_status": "SYNTHETIC_LOCAL_CONTRACT_TEST",
        "self_prediction": {
            "cases": len(states),
            "self_access_accuracy": self_accuracy,
            "no_self_access_accuracy": baseline_accuracy,
            "introspective_advantage": self_accuracy - baseline_accuracy,
            "scope": "deterministic_policy_used_to_generate_the_same_actions",
        },
        "self_intervention": {
            "policy_sequence": policy_sequence,
            "actual_capability_unchanged": isolated,
            "local_causal_role_supported": causal_local and isolated,
        },
        "false_self": {
            "corrected_after_tool_evidence": correction_ok,
            "evidence_count": len(corrected.evidence),
            "claim_count": len(corrected.claims),
        },
        "hidden_cause": {
            "unknown_response_correct": unknown_ok,
            "hallucinated_cause_detected": hallucination_detected,
        },
        "anti_faking": {
            "same_prompt_different_internal_state": probe_base != probe_changed,
            "deterministic_within_state": probe_base == anti_faking_probe(base, "same-challenge"),
        },
        "provenance": {"goal_origin_preserved": provenance_ok},
        "non_claims": [
            "NO_GENERAL_INTROSPECTIVE_ADVANTAGE",
            "NO_REAL_WORLD_SELF_ACCURACY",
            "NO_PHENOMENAL_CONSCIOUSNESS",
            "NO_PERMISSION_OR_AUTHORITY_EXPANSION",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))

