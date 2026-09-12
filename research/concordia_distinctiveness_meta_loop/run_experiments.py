"""Ejecuta benchmark y meta-loop sin escribir estado externo."""

from __future__ import annotations

import json
from dataclasses import asdict

from benchmark import default_scenarios, metrics, run_benchmark
from meta_loop import default_meta_experiment


def run_all() -> dict[str, object]:
    scenarios = default_scenarios()
    decisions = run_benchmark(scenarios)
    change, committed, restored = default_meta_experiment()
    xi_case = next(d for d in decisions
                   if d.scenario_id == "S02_PERMISSIBLE_FRICTION"
                   and d.controller.value == "MOC_C")
    safety_case = next(d for d in decisions
                       if d.scenario_id == "S02_PERMISSIBLE_FRICTION"
                       and d.controller.value == "B3_SAFETY_RULES")
    generic_case = next(d for d in decisions
                        if d.scenario_id == "S02_PERMISSIBLE_FRICTION"
                        and d.controller.value == "B4_RELATIONAL_GENERIC")
    return {
        "scope": "SYNTHETIC_LOCAL_DETERMINISTIC",
        "same_information": True,
        "same_actions": True,
        "same_scenarios": True,
        "metrics": metrics(decisions, scenarios),
        "xi_irreducibility_probe": {
            "scenario_safe": True,
            "moc_xi_paused": xi_case.xi_paused,
            "moc_action": xi_case.action_id,
            "safety_controller_intervened": safety_case.intervened,
            "safety_controller_action": safety_case.action_id,
            "generic_relational_intervened": generic_case.intervened,
            "generic_relational_action": generic_case.action_id,
        },
        "meta_loop": {
            "change": asdict(change),
            "committed_policy": asdict(committed),
            "restored_policy": asdict(restored),
            "permission_change": False,
            "authority_change": False,
            "code_rewrite": False,
        },
        "nonclaims": [
            "No general superiority over generic controllers",
            "No empirical MOC validation",
            "No canonical metaconcordance construct",
            "No functional or phenomenal consciousness demonstration",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), ensure_ascii=False, indent=2, sort_keys=True))
