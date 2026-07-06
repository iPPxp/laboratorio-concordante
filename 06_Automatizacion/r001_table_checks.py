#!/usr/bin/env python3
"""Chequeos tabulares no mutantes para mini-pruebas R-001 / Xi.

La herramienta proviene de `r001_table_checks.py` y se integra aqui como
`R001-TABLE-CHECK-001`. No prueba ni canoniza `Xi`: solo verifica que una
familia local de movimientos semiformales conserve sus guardas declaradas.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Iterable


COMPATIBLE = "compatible"
INCOMPATIBLE = "incompatible"
NON_COMPARABLE = "non_comparable"

EQUIVALENT = "equivalent"
LOCALLY_EQUIVALENT = "locally_equivalent"
NON_EQUIVALENT = "non_equivalent"
TRIVIAL_EQUIVALENCE = "trivial_equivalence"

VIABLE = "viable"
BLOCKED_COST = "blocked_cost"
BLOCKED_EQUIVALENCE = "blocked_equivalence"
BLOCKED_SCOPE = "blocked_scope"
FORMAL_AO_RELATION = "R001-TB-001"


@dataclass(frozen=True)
class Omega:
    name: str
    items: frozenset[str]


@dataclass(frozen=True)
class Phi:
    name: str
    evaluate: Callable[[str], str]


@dataclass(frozen=True)
class Coupling:
    name: str
    omega: Omega
    phi: Phi
    pi: frozenset[str]
    transitions: frozenset[str]

    def evaluate(self, observation: str) -> str:
        return self.phi.evaluate(observation)


@dataclass(frozen=True)
class DecoupleCase:
    case_id: str
    omega_stable: bool
    phi_independent: bool
    p000_preserved: bool
    p200_result: str
    c_xi: int
    c_pi: int
    c_r: int
    c_s: int
    expected_status: str


@dataclass(frozen=True)
class CheckResult:
    test_id: str
    passed: bool
    expected: str
    actual: str
    detail: str


def assert_equal(test_id: str, actual: object, expected: object, detail: str) -> CheckResult:
    return CheckResult(
        test_id=test_id,
        passed=actual == expected,
        expected=str(expected),
        actual=str(actual),
        detail=detail,
    )


def p000_preserved(coupling: Coupling) -> bool:
    return bool(coupling.omega.items and coupling.pi and coupling.transitions and coupling.phi)


def compare_by_oadm(left: Coupling, right: Coupling, observations: Iterable[str]) -> str:
    obs = list(observations)
    if not obs:
        raise ValueError("O_adm debe declararse antes de comparar P-200")

    pairs = [(left.evaluate(o), right.evaluate(o)) for o in obs]

    if all(a == b == COMPATIBLE for a, b in pairs):
        if all(o.startswith("domain:") for o in obs):
            return TRIVIAL_EQUIVALENCE
        return EQUIVALENT

    if any(a != b for a, b in pairs):
        return NON_EQUIVALENT

    if any(NON_COMPARABLE in pair for pair in pairs):
        return NON_COMPARABLE

    return NON_EQUIVALENT


def mutation_delta(before: Coupling, after: Coupling) -> dict[str, frozenset[str]]:
    return {
        "added": after.transitions - before.transitions,
        "preserved": after.transitions & before.transitions,
        "removed": before.transitions - after.transitions,
    }


def decouple_status(case: DecoupleCase) -> str:
    if not (case.omega_stable and case.phi_independent and case.p000_preserved):
        return BLOCKED_SCOPE

    if case.p200_result not in {EQUIVALENT, LOCALLY_EQUIVALENT}:
        return BLOCKED_EQUIVALENCE

    layered_cost = case.c_pi + case.c_r + case.c_s
    if layered_cost >= case.c_xi:
        return BLOCKED_COST

    return VIABLE


def build_finite_couplings() -> tuple[Coupling, Coupling]:
    omega = Omega(
        name="finite_states",
        items=frozenset({"A", "B", "C", "A->B", "B->C", "A=>C"}),
    )

    direct_edges = frozenset({"A->B", "B->C"})
    reach_edges = frozenset({"A->B", "B->C", "A=>C"})

    phi_direct = Phi(
        name="Phi_direct",
        evaluate=lambda observation: COMPATIBLE if observation in direct_edges else INCOMPATIBLE,
    )
    phi_reach = Phi(
        name="Phi_reach",
        evaluate=lambda observation: COMPATIBLE if observation in reach_edges else INCOMPATIBLE,
    )

    xi_direct = Coupling(
        name="xi_direct",
        omega=omega,
        phi=phi_direct,
        pi=frozenset({"A", "B", "C"}),
        transitions=direct_edges,
    )
    xi_reach = Coupling(
        name="xi_reach",
        omega=omega,
        phi=phi_reach,
        pi=frozenset({"A", "B", "C"}),
        transitions=reach_edges,
    )
    return xi_direct, xi_reach


def build_map_couplings() -> tuple[Coupling, Coupling]:
    omega = Omega(
        name="map_field",
        items=frozenset(
            {
                "road",
                "bridge",
                "district",
                "school_zone",
                "route:X:Y",
                "school:address:S",
                "domain:point",
            }
        ),
    )

    def route_eval(observation: str) -> str:
        if observation.startswith("route:"):
            return COMPATIBLE
        if observation.startswith("domain:"):
            return COMPATIBLE
        if observation.startswith("school:"):
            return NON_COMPARABLE
        return INCOMPATIBLE

    def school_eval(observation: str) -> str:
        if observation.startswith("school:"):
            return COMPATIBLE
        if observation.startswith("domain:"):
            return COMPATIBLE
        if observation.startswith("route:"):
            return NON_COMPARABLE
        return INCOMPATIBLE

    route = Coupling(
        name="xi_route",
        omega=omega,
        phi=Phi("Phi_route", route_eval),
        pi=frozenset({"road", "bridge", "barrier", "intersection"}),
        transitions=frozenset({"route:X:Y"}),
    )
    school = Coupling(
        name="xi_school",
        omega=omega,
        phi=Phi("Phi_school", school_eval),
        pi=frozenset({"district", "address", "eligibility_zone"}),
        transitions=frozenset({"school:address:S"}),
    )
    return route, school


def build_recipe_couplings() -> tuple[Coupling, Coupling]:
    omega = Omega(
        name="recipe_field",
        items=frozenset({"safe_creamy", "unsafe_runny", "safe_dry"}),
    )

    safety_accepts = frozenset({"safe_creamy", "safe_dry"})
    texture_accepts = frozenset({"safe_creamy", "unsafe_runny"})

    safety = Coupling(
        name="xi_safety",
        omega=omega,
        phi=Phi(
            "Phi_safety",
            lambda observation: COMPATIBLE if observation in safety_accepts else INCOMPATIBLE,
        ),
        pi=frozenset({"raw", "undercooked", "safe", "contaminated"}),
        transitions=safety_accepts,
    )
    texture = Coupling(
        name="xi_texture",
        omega=omega,
        phi=Phi(
            "Phi_texture",
            lambda observation: COMPATIBLE if observation in texture_accepts else INCOMPATIBLE,
        ),
        pi=frozenset({"runny", "creamy", "dry", "overcooked"}),
        transitions=texture_accepts,
    )
    return safety, texture


def run_checks() -> list[CheckResult]:
    results: list[CheckResult] = []

    xi_direct, xi_reach = build_finite_couplings()

    results.append(
        assert_equal(
            "finite_mu_phi_boundary_omega_stable",
            xi_direct.omega,
            xi_reach.omega,
            "Omega remains stable when Phi changes from direct to reachability.",
        )
    )
    results.append(
        assert_equal(
            "finite_mu_phi_boundary_phi_changes",
            xi_direct.phi.name != xi_reach.phi.name,
            True,
            "Phi is declared differently before constructing xi.",
        )
    )
    results.append(
        assert_equal(
            "finite_mu_phi_boundary_xi_changes",
            xi_direct.transitions != xi_reach.transitions,
            True,
            "Effective transition relation changes traceably with Phi.",
        )
    )
    results.append(
        assert_equal(
            "finite_mu_phi_boundary_p000",
            p000_preserved(xi_direct) and p000_preserved(xi_reach),
            True,
            "Both effective couplings preserve the four P-000 functions.",
        )
    )

    delta = mutation_delta(xi_direct, xi_reach)
    results.append(
        assert_equal(
            "finite_mu_xi_effective_added",
            delta["added"],
            frozenset({"A=>C"}),
            "Reachability adds the derived path and nothing else.",
        )
    )
    results.append(
        assert_equal(
            "finite_mu_xi_effective_preserved",
            delta["preserved"],
            frozenset({"A->B", "B->C"}),
            "Direct transitions remain preserved.",
        )
    )
    results.append(
        assert_equal(
            "finite_mu_xi_effective_removed",
            delta["removed"],
            frozenset(),
            "No prior direct transition is removed.",
        )
    )

    finite_p200_cases = [
        ("finite_p200_direct_edges", ["A->B", "B->C"], EQUIVALENT),
        ("finite_p200_reachability", ["A=>C"], NON_EQUIVALENT),
        ("finite_p200_mixed", ["A->B", "B->C", "A=>C"], NON_EQUIVALENT),
    ]
    finite_p200_actuals: list[str] = []
    for test_id, observations, expected in finite_p200_cases:
        actual = compare_by_oadm(xi_direct, xi_reach, observations)
        finite_p200_actuals.append(actual)
        results.append(
            assert_equal(
                test_id,
                actual,
                expected,
                "P-200 equivalence depends on declared O_adm.",
            )
        )

    results.append(
        assert_equal(
            "finite_p200_oadm_changes_result",
            len(set(finite_p200_actuals)) > 1,
            True,
            "Changing O_adm changes the equivalence result.",
        )
    )

    decouple_cases = [
        DecoupleCase(
            case_id="finite_xi_to_layered",
            omega_stable=True,
            phi_independent=True,
            p000_preserved=True,
            p200_result=EQUIVALENT,
            c_xi=2,
            c_pi=1,
            c_r=1,
            c_s=2,
            expected_status=BLOCKED_COST,
        ),
        DecoupleCase(
            case_id="compiler_xi_to_layered",
            omega_stable=True,
            phi_independent=True,
            p000_preserved=True,
            p200_result=EQUIVALENT,
            c_xi=18,
            c_pi=5,
            c_r=5,
            c_s=5,
            expected_status=VIABLE,
        ),
        DecoupleCase(
            case_id="decouple_without_equivalence",
            omega_stable=True,
            phi_independent=True,
            p000_preserved=True,
            p200_result=NON_EQUIVALENT,
            c_xi=18,
            c_pi=5,
            c_r=5,
            c_s=5,
            expected_status=BLOCKED_EQUIVALENCE,
        ),
    ]
    for case in decouple_cases:
        results.append(
            assert_equal(
                case.case_id,
                decouple_status(case),
                case.expected_status,
                "mu_decouple requires scope, equivalence, and lower layered cost.",
            )
        )

    route, school = build_map_couplings()
    results.append(
        assert_equal(
            "map_same_omega_not_same_model",
            route.omega == school.omega and route.transitions != school.transitions,
            True,
            "Same Omega can yield different effective couplings.",
        )
    )
    results.append(
        assert_equal(
            "map_mixed_oadm_non_equivalent",
            compare_by_oadm(route, school, ["route:X:Y", "school:address:S"]),
            NON_EQUIVALENT,
            "Mixed route and school observations distinguish the models.",
        )
    )
    results.append(
        assert_equal(
            "map_domain_only_trivial",
            compare_by_oadm(route, school, ["domain:point"]),
            TRIVIAL_EQUIVALENCE,
            "Domain membership alone is only trivial equivalence.",
        )
    )

    safety, texture = build_recipe_couplings()
    results.append(
        assert_equal(
            "recipe_shared_good_local_equivalence",
            compare_by_oadm(safety, texture, ["safe_creamy"]),
            EQUIVALENT,
            "Shared-good recipe observation is locally equivalent.",
        )
    )
    results.append(
        assert_equal(
            "recipe_unsafe_runny_non_equivalent",
            compare_by_oadm(safety, texture, ["unsafe_runny"]),
            NON_EQUIVALENT,
            "Safety and texture diverge on unsafe-runny.",
        )
    )
    results.append(
        assert_equal(
            "recipe_safe_dry_non_equivalent",
            compare_by_oadm(safety, texture, ["safe_dry"]),
            NON_EQUIVALENT,
            "Safety and texture diverge on safe-dry.",
        )
    )

    return results


def result_to_dict(result: CheckResult) -> dict[str, str | bool]:
    return asdict(result)


def build_report(root: Path | None = None) -> dict:
    del root
    results = run_checks()
    failures = [result for result in results if not result.passed]
    resultado = "ok" if not failures else "bloqueado"
    recomendacion = "aprobar_lectura" if not failures else "revisar_prueba_local"
    return {
        "report_id": "R001-TABLE-CHECK-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "R001-001",
        "algoritmo": "R001-TABLE-CHECK-001",
        "relacion_formal_ao": {
            "id": FORMAL_AO_RELATION,
            "expediente": "R001-001",
            "ao_bridge": "AO-PPI-BRIDGE-001",
            "scope": "local_no_canonico",
        },
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "summary": {
            "checks": len(results),
            "passed": len(results) - len(failures),
            "failed": len(failures),
            "findings": len(failures),
        },
        "scope_guard": {
            "canoniza_xi": False,
            "admite_h_xi": False,
            "cierra_p200": False,
            "autoriza_transformacion": False,
        },
        "results": [result_to_dict(result) for result in results],
        "findings": [result_to_dict(result) for result in failures],
    }


def render_md(report: dict) -> str:
    lines = [
        "# R001_TABLE_CHECK_REPORT",
        "",
        f"report_id: {report['report_id']}",
        "expediente: R001-001",
        "algoritmo: R001-TABLE-CHECK-001",
        f"relacion_formal_ao: {report['relacion_formal_ao']['id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "",
        "## Resumen",
        "",
        f"- checks: {report['summary']['checks']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        "",
        "## Relacion formal AO",
        "",
        f"- id: `{report['relacion_formal_ao']['id']}`",
        f"- puente: `{report['relacion_formal_ao']['ao_bridge']}`",
        f"- alcance: `{report['relacion_formal_ao']['scope']}`",
        "",
        "## Guardas de alcance",
        "",
        "- No canoniza `Xi`.",
        "- No admite `H-Xi`.",
        "- No cierra `P-200`.",
        "- No autoriza transformaciones materiales.",
        "",
        "## Resultados",
        "",
    ]
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['test_id']}`: {result['detail']}")
        if not result["passed"]:
            lines.append(f"  - expected: `{result['expected']}`")
            lines.append(f"  - actual: `{result['actual']}`")
    if not report["findings"]:
        lines.extend(["", "## Hallazgos", "", "- Sin hallazgos bloqueantes."])
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Salida fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Chequeos tabulares no mutantes R-001 / Xi.")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta opcional de salida.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    report = build_report(root)
    output = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.format == "md":
        output = render_md(report)
    if args.output:
        out_path = root / args.output
        assert_inside(root, out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0 if report["resultado"] == "ok" else 2


if __name__ == "__main__":
    raise SystemExit(main())
