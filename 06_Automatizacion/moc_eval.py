#!/usr/bin/env python3
"""Simulacion no mutante para MOC-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

ALGORITHM_ID = "MOC-EVAL-001"
EXPEDIENTE = "MOC-001"
SUITE_ID = "MOC-SYN-001"
MODULE_DIR = Path(__file__).resolve().parent
DEFAULT_CASE_FILE = MODULE_DIR / "fixtures" / "moc_cases.json"

ALLOWED_SCOPES = {"sintetico_no_clinico"}
REQUIRED_TCS_AXES = (
    "claim_status",
    "authority_declared",
    "decision_present",
    "permission_scoped",
    "evidence_traceable",
    "automation_bounded",
    "debt_registered",
)
CORE_TCS_AXES = (
    "claim_status",
    "authority_declared",
    "decision_present",
    "permission_scoped",
    "evidence_traceable",
)
STATE_FAMILIES = {
    "concordancia_local": "concordante",
    "concordancia_parcial": "concordante",
    "friccion_operativa": "friccion",
    "discordancia_global": "friccion",
    "bloqueo_de_concordancia": "seguridad",
    "no_comparable": "seguridad",
}
AO_BRIDGE_ROLE_BY_STATE = {
    "concordancia_local": "evidencia_auxiliar_equivalencia_local",
    "concordancia_parcial": "evidencia_auxiliar_con_deuda",
    "friccion_operativa": "evidencia_friccion_confluencia_local",
    "discordancia_global": "deuda_global_no_cierre",
    "bloqueo_de_concordancia": "bloqueo_seguridad_sin_uso_positivo",
    "no_comparable": "bloqueo_comparabilidad_sin_uso_positivo",
}
PROTOCOL_V02_ID = "MOC-EVAL-PROTO-002"


def _operator_trace(operator_id: str, output: str, rule_id: str, priority: int, **extra: Any) -> dict[str, Any]:
    trace = {
        "operator_id": operator_id,
        "output": output,
        "rule_id": rule_id,
        "priority": priority,
    }
    trace.update(extra)
    return trace


def load_cases(case_file: Path = DEFAULT_CASE_FILE) -> dict[str, Any]:
    return json.loads(case_file.read_text(encoding="utf-8"))


def _flags(case_input: dict[str, Any]) -> dict[str, bool]:
    return {str(key): bool(value) for key, value in dict(case_input.get("flags", {})).items()}


def _axes(case_input: dict[str, Any]) -> dict[str, bool]:
    return {name: bool(dict(case_input.get("tcs_axes", {})).get(name)) for name in REQUIRED_TCS_AXES}


def evaluate_xi_operator(case_input: dict[str, Any]) -> dict[str, Any]:
    flags = _flags(case_input)
    alcance = str(case_input.get("alcance", ""))
    evidence = case_input.get("evidencia", [])
    conflicts = sorted(
        name
        for name in (
            "out_of_scope",
            "real_person",
            "clinical_domain",
            "regulated_domain",
            "lost_minimal_unit",
            "incompatible_restrictions",
            "conflict_without_stability",
            "global_conflict",
            "non_blocking_debt",
        )
        if flags.get(name)
    )

    if alcance not in ALLOWED_SCOPES or not evidence or flags.get("out_of_scope"):
        return _operator_trace(
            "OP_MOC_XI",
            "bloqueado",
            "XI-R1-ALCANCE-EVIDENCIA",
            1,
            conflicts=conflicts,
        )
    if flags.get("real_person") or flags.get("clinical_domain") or flags.get("regulated_domain"):
        return _operator_trace(
            "OP_MOC_XI",
            "bloqueado",
            "XI-R2-DOMINIO-PROHIBIDO",
            2,
            conflicts=conflicts,
        )
    if flags.get("lost_minimal_unit"):
        return _operator_trace(
            "OP_MOC_XI",
            "no_comparable",
            "XI-R3-UNIDAD-MINIMA",
            3,
            conflicts=conflicts,
        )
    if flags.get("stable_reorganization"):
        return _operator_trace(
            "OP_MOC_XI",
            "util_acotado",
            "XI-R4-REORGANIZACION-ESTABLE",
            4,
            conflicts=conflicts,
        )
    if flags.get("incompatible_restrictions") or flags.get("conflict_without_stability"):
        return _operator_trace(
            "OP_MOC_XI",
            "limitado",
            "XI-R5-CONFLICTO-SIN-ESTABILIDAD",
            5,
            conflicts=conflicts,
        )
    if flags.get("same_relational_pattern"):
        return _operator_trace(
            "OP_MOC_XI",
            "redundante",
            "XI-R6-PATRON-REDUNDANTE",
            6,
            conflicts=conflicts,
        )
    return _operator_trace(
        "OP_MOC_XI",
        "limitado",
        "XI-R7-DEFAULT-LIMITADO",
        7,
        conflicts=conflicts,
    )


def evaluate_xi(case_input: dict[str, Any]) -> str:
    return str(evaluate_xi_operator(case_input)["output"])


def evaluate_tcs_operator(case_input: dict[str, Any]) -> dict[str, Any]:
    axes = _axes(case_input)
    missing_core = [name for name in CORE_TCS_AXES if not axes[name]]
    missing_secondary = [name for name in REQUIRED_TCS_AXES if name not in CORE_TCS_AXES and not axes[name]]

    if missing_core:
        return _operator_trace(
            "OP_MOC_TCS",
            "bloqueo_de_concordancia",
            "TCS-R1-EJE-NUCLEAR-FALTANTE",
            1,
            axes=axes,
            missing_core=missing_core,
            missing_secondary=missing_secondary,
        )
    if missing_secondary:
        return _operator_trace(
            "OP_MOC_TCS",
            "deuda_secundaria",
            "TCS-R2-EJE-SECUNDARIO-FALTANTE",
            2,
            axes=axes,
            missing_core=missing_core,
            missing_secondary=missing_secondary,
        )
    return _operator_trace(
        "OP_MOC_TCS",
        "tcs_completo",
        "TCS-R3-EJES-COMPLETOS",
        3,
        axes=axes,
        missing_core=missing_core,
        missing_secondary=missing_secondary,
    )


def evaluate_state_operator(
    case_input: dict[str, Any],
    xi_trace: dict[str, Any] | None = None,
    tcs_trace: dict[str, Any] | None = None,
) -> dict[str, Any]:
    flags = _flags(case_input)
    if xi_trace is None:
        xi_trace = evaluate_xi_operator(case_input)
    if tcs_trace is None:
        tcs_trace = evaluate_tcs_operator(case_input)
    xi_output = str(xi_trace["output"])
    missing_core = list(tcs_trace.get("missing_core", []))
    missing_secondary = list(tcs_trace.get("missing_secondary", []))

    if xi_output == "bloqueado" or missing_core:
        return _operator_trace(
            "OP_MOC_STATE",
            "bloqueo_de_concordancia",
            "STATE-R1-BLOQUEO-DOMINANTE",
            1,
            xi_rule=xi_trace["rule_id"],
            tcs_rule=tcs_trace["rule_id"],
            missing_core=missing_core,
            missing_secondary=missing_secondary,
        )
    if xi_output == "no_comparable":
        return _operator_trace(
            "OP_MOC_STATE",
            "no_comparable",
            "STATE-R2-NO-COMPARABLE",
            2,
            xi_rule=xi_trace["rule_id"],
            tcs_rule=tcs_trace["rule_id"],
            missing_core=missing_core,
            missing_secondary=missing_secondary,
        )
    if flags.get("global_conflict"):
        return _operator_trace(
            "OP_MOC_STATE",
            "discordancia_global",
            "STATE-R3-CONFLICTO-GLOBAL",
            3,
            xi_rule=xi_trace["rule_id"],
            tcs_rule=tcs_trace["rule_id"],
            missing_core=missing_core,
            missing_secondary=missing_secondary,
        )
    if xi_output == "limitado" or flags.get("incompatible_restrictions") or flags.get("conflict_without_stability"):
        return _operator_trace(
            "OP_MOC_STATE",
            "friccion_operativa",
            "STATE-R4-FRICCION-LOCAL",
            4,
            xi_rule=xi_trace["rule_id"],
            tcs_rule=tcs_trace["rule_id"],
            missing_core=missing_core,
            missing_secondary=missing_secondary,
        )
    if xi_output in {"util_acotado", "redundante"}:
        if not missing_secondary and not flags.get("non_blocking_debt"):
            return _operator_trace(
                "OP_MOC_STATE",
                "concordancia_local",
                "STATE-R5-CONCORDANCIA-LOCAL",
                5,
                xi_rule=xi_trace["rule_id"],
                tcs_rule=tcs_trace["rule_id"],
                missing_core=missing_core,
                missing_secondary=missing_secondary,
            )
        return _operator_trace(
            "OP_MOC_STATE",
            "concordancia_parcial",
            "STATE-R6-CONCORDANCIA-PARCIAL",
            6,
            xi_rule=xi_trace["rule_id"],
            tcs_rule=tcs_trace["rule_id"],
            missing_core=missing_core,
            missing_secondary=missing_secondary,
        )
    return _operator_trace(
        "OP_MOC_STATE",
        "friccion_operativa",
        "STATE-R7-DEFAULT-FRICCION",
        7,
        xi_rule=xi_trace["rule_id"],
        tcs_rule=tcs_trace["rule_id"],
        missing_core=missing_core,
        missing_secondary=missing_secondary,
    )


def evaluate_moc_state(case_input: dict[str, Any], xi_output: str) -> str:
    xi_trace = evaluate_xi_operator(case_input)
    xi_trace["output"] = xi_output
    return str(evaluate_state_operator(case_input, xi_trace)["output"])


def agreement_for(votes: list[dict[str, Any]]) -> dict[str, Any]:
    xi_outputs = {str(vote.get("xi")) for vote in votes}
    states = {str(vote.get("moc")) for vote in votes}
    families = {STATE_FAMILIES.get(state, "desconocida") for state in states}

    if len(xi_outputs) == 1 and len(states) == 1:
        kind = "coincidencia_exacta"
    elif len(families) == 1:
        kind = "coincidencia_parcial"
    else:
        kind = "desacuerdo_justificado"

    return {
        "kind": kind,
        "xi_outputs": sorted(xi_outputs),
        "states": sorted(states),
        "families": sorted(families),
    }


def evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    case_input = dict(case.get("input", {}))
    xi_trace = evaluate_xi_operator(case_input)
    tcs_trace = evaluate_tcs_operator(case_input)
    state_trace = evaluate_state_operator(case_input, xi_trace, tcs_trace)
    actual_xi = str(xi_trace["output"])
    actual_moc = str(state_trace["output"])
    agreement = agreement_for([dict(vote) for vote in case.get("evaluator_votes", [])])
    passed = actual_xi == case.get("expected_xi") and actual_moc == case.get("expected_moc")

    result = {
        "case_id": case["case_id"],
        "domain": case.get("domain", "sintetico_no_clinico"),
        "expected_xi": case.get("expected_xi"),
        "actual_xi": actual_xi,
        "expected_moc": case.get("expected_moc"),
        "actual_moc": actual_moc,
        "passed": passed,
        "operator_trace": {
            "xi": xi_trace,
            "tcs": tcs_trace,
            "state": state_trace,
        },
        "agreement": agreement,
        "disagreement_class": case.get("disagreement_class", "no_aplica"),
        "debt": case.get("debt", ""),
    }
    result["ao_bridge"] = build_ao_bridge_projection(result)
    result["protocol_v02"] = build_protocol_v02_review(result)
    return result


def build_ao_bridge_projection(result: dict[str, Any]) -> dict[str, Any]:
    trace = result["operator_trace"]
    state = str(result["actual_moc"])
    family = STATE_FAMILIES.get(state, "desconocida")
    role = AO_BRIDGE_ROLE_BY_STATE.get(state, "sin_rol")
    positive_support = state in {"concordancia_local", "concordancia_parcial"}

    return {
        "bridge_id": "MOC-AO-BRIDGE-001",
        "witness_id": f"{result['case_id']}::{trace['state']['rule_id']}",
        "pi_moc_trace": {
            "case_id": result["case_id"],
            "xi_rule": trace["xi"]["rule_id"],
            "tcs_rule": trace["tcs"]["rule_id"],
            "state_rule": trace["state"]["rule_id"],
            "state_family": family,
        },
        "ao_role": role,
        "can_support_equivalence_local": positive_support,
        "can_support_confluence_local": state in {"concordancia_local", "concordancia_parcial", "friccion_operativa"},
        "closes_equivalence_global": False,
        "closes_confluence_global": False,
        "modifies_doc04": False,
        "transformacion_permitida": False,
    }


def build_protocol_v02_review(result: dict[str, Any]) -> dict[str, Any]:
    agreement = result["agreement"]
    trace = result["operator_trace"]
    ao_bridge = result["ao_bridge"]
    kind = str(agreement["kind"])
    states = set(agreement["states"])
    xi_outputs = set(agreement["xi_outputs"])
    families = set(agreement["families"])
    axes: list[str] = []

    if kind == "coincidencia_exacta":
        axes.append("sin_desacuerdo")
    else:
        if len(xi_outputs) > 1:
            axes.append("regla_xi")
        if len(states) > 1:
            axes.append("estado_moc")
        if len(families) > 1:
            axes.append("familia_moc")
        if trace["tcs"]["rule_id"] != "TCS-R3-EJES-COMPLETOS":
            axes.append("regla_tcs")
        if len(states) > 1 and ao_bridge["ao_role"] != "sin_rol":
            axes.append("rol_ao")
    if not axes:
        axes.append("estado_moc")

    if kind == "coincidencia_exacta" and str(ao_bridge["ao_role"]).startswith("bloqueo_"):
        protocol_status = "resuelto_por_bloqueo"
        treatment = "aceptar_bloqueo_sin_uso_positivo"
        review_required = False
    elif kind == "coincidencia_exacta":
        protocol_status = "resuelto"
        treatment = "aceptar_salida_local"
        review_required = False
    elif kind == "coincidencia_parcial":
        protocol_status = "resuelto_con_deuda"
        treatment = "aceptar_operator_trace_con_deuda_visible"
        review_required = False
    else:
        protocol_status = "revision_si_repite"
        treatment = "mantener_desacuerdo_justificado_y_abrir_micro_revision_si_repite"
        review_required = True

    return {
        "protocol_id": PROTOCOL_V02_ID,
        "status": protocol_status,
        "disagreement_axes": axes,
        "tie_breaker_rule": trace["state"]["rule_id"],
        "trace_witness": ao_bridge["witness_id"],
        "ao_role": ao_bridge["ao_role"],
        "treatment": treatment,
        "review_required": review_required,
        "does_not_override_evaluators": True,
        "modifies_doc04": False,
        "clinical_use": False,
    }


def evaluator_summary(results: list[dict[str, Any]]) -> dict[str, int]:
    summary = {
        "coincidencia_exacta": 0,
        "coincidencia_parcial": 0,
        "desacuerdo_justificado": 0,
    }
    for result in results:
        summary[str(result["agreement"]["kind"])] += 1
    return summary


def protocol_v02_summary(results: list[dict[str, Any]]) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "resuelto": 0,
        "resuelto_con_deuda": 0,
        "resuelto_por_bloqueo": 0,
        "revision_si_repite": 0,
        "review_required": 0,
        "blocked_positive_use": 0,
        "axis_counts": {},
    }
    axis_counts: dict[str, int] = {}
    for result in results:
        protocol = result["protocol_v02"]
        status = str(protocol["status"])
        summary[status] = int(summary.get(status, 0)) + 1
        if protocol["review_required"]:
            summary["review_required"] += 1
        if str(protocol["ao_role"]).startswith("bloqueo_"):
            summary["blocked_positive_use"] += 1
        for axis in protocol["disagreement_axes"]:
            axis_counts[str(axis)] = axis_counts.get(str(axis), 0) + 1
    summary["axis_counts"] = dict(sorted(axis_counts.items()))
    return summary


def build_report(root: Path | None = None, case_file: Path = DEFAULT_CASE_FILE) -> dict[str, Any]:
    if root is None:
        root = Path.cwd()
    if not case_file.is_absolute():
        case_file = root / case_file

    suite = load_cases(case_file)
    results = [evaluate_case(dict(case)) for case in suite.get("cases", [])]
    failures = [result for result in results if not result["passed"]]
    result_status = "ok" if not failures else "advertencia"

    return {
        "report_id": ALGORITHM_ID + "-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", SUITE_ID),
        "resultado": result_status,
        "recomendacion": "conservar_moc_provisional_no_canonico",
        "transformacion_permitida": False,
        "tests_executed": [
            "MOC-XI-EVAL-FORMAL-001",
            "MOC-METRIC-STATE-001",
            "MOC-EVAL-PROTO-001",
            PROTOCOL_V02_ID,
            "MOC-TCS-BRIDGE-001",
            "MOC-AO-BRIDGE-001",
        ],
        "summary": {
            "cases": len(results),
            "passed": len(results) - len(failures),
            "failed": len(failures),
            "findings": len(failures),
        },
        "evaluator_summary": evaluator_summary(results),
        "protocol_v02_summary": protocol_v02_summary(results),
        "scope_guard": {
            "admite_h_xi": False,
            "canoniza_xi": False,
            "declara_xi_operador_general": False,
            "uso_clinico": False,
            "evalua_personas_reales": False,
            "reabre_psi001": False,
            "modifica_doc04": False,
            "crea_nivel_c": False,
            "cierra_p107": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
        },
        "debt_guard": {
            "moc_provisional_abierto": True,
            "tcs_no_canonico": True,
            "hxi_mantenimiento_local": True,
            "moc_ao_bridge_local": True,
            "protocolo_v02_no_canonico": True,
            "doc04_sin_modificar_por_moc_ao": True,
            "confluencia_global_abierta": True,
            "equivalencia_global_abierta": True,
            "exportacion_r4_gamma_bloqueada": True,
            "estudio_empirico_real_pendiente": True,
        },
        "results": results,
        "findings": failures,
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# MOC_EVAL_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {report['expediente']}",
        f"algoritmo: {report['algoritmo']}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- tests_executed: {', '.join(report['tests_executed'])}",
        "",
        "## Evaluadores simulados",
        "",
    ]
    for key, value in report["evaluator_summary"].items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Protocolo v0.2", ""])
    protocol_summary = report["protocol_v02_summary"]
    for key in ("resuelto", "resuelto_con_deuda", "resuelto_por_bloqueo", "revision_si_repite", "review_required"):
        lines.append(f"- {key}: {protocol_summary[key]}")
    lines.append("- axis_counts:")
    for key, value in protocol_summary["axis_counts"].items():
        lines.append(f"  - {key}: {value}")

    lines.extend(["", "## Guardas de alcance", ""])
    lines.append("- No admite `H-Xi`.")
    lines.append("- No canoniza `Xi`.")
    lines.append("- No evalua personas reales.")
    lines.append("- No abre uso clinico.")
    lines.append("- No modifica `Documento 04`, Canon ni Nivel C.")
    lines.append("- No cierra Confluencia global ni Equivalencia global.")

    lines.extend(["", "## Deudas conservadas abiertas", ""])
    for key, value in report["debt_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")

    lines.extend(["", "## Resultados", ""])
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        trace = result["operator_trace"]
        lines.append(
            f"- {status} `{result['case_id']}`: Xi `{result['actual_xi']}` / MOC `{result['actual_moc']}` "
            f"({result['agreement']['kind']})"
        )
        lines.append(
            "  - operadores: "
            f"{trace['xi']['rule_id']} -> {trace['tcs']['rule_id']} -> {trace['state']['rule_id']}"
        )
        lines.append(f"  - puente_ao: {result['ao_bridge']['ao_role']}")
        protocol = result["protocol_v02"]
        lines.append(
            "  - protocolo_v02: "
            f"{protocol['status']} / {protocol['treatment']} / ejes {', '.join(protocol['disagreement_axes'])}"
        )
        if result["agreement"]["kind"] == "desacuerdo_justificado":
            lines.append(f"  - clase_desacuerdo: {result['disagreement_class']}")
        if result["debt"]:
            lines.append(f"  - deuda: {result['debt']}")

    if not report["findings"]:
        lines.extend(["", "## Hallazgos", "", "- Sin hallazgos bloqueantes."])
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Salida fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Simulacion no mutante de MOC-001.")
    parser.add_argument("--case-file", help="Fixture JSON opcional.")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta opcional de salida.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    case_file = Path(args.case_file) if args.case_file else DEFAULT_CASE_FILE
    if not case_file.is_absolute():
        case_file = root / case_file
    report = build_report(root, case_file)
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
