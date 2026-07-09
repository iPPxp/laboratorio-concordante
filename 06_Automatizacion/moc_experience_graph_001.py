#!/usr/bin/env python3
"""Validador no mutante para MOC-EXP-GRAPH-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "MOC-EXP-GRAPH-CHECK-001"
EXPEDIENTE = "MOC-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "moc_experience_graph_cases.json"

METRIC_KEYS = (
    "G_scope",
    "G_olc",
    "G_embed",
    "G_T",
    "G_E",
    "G_path",
    "G_Aprism",
    "G_Vprism",
    "G_OmegaPhi",
    "G_tau_fit",
    "G_adapt",
    "G_unity",
    "G_Aexp",
    "G_Cpsi",
    "G_phi",
    "G_evid",
)
MIN_GEOMETRIC_KEYS = (
    "G_T",
    "G_E",
    "G_path",
    "G_Aprism",
    "G_Vprism",
    "G_OmegaPhi",
    "G_unity",
)
REQUIRED_NODES = {
    "Omega_psi",
    "Xi_psi",
    "Pi5_psi",
    "Phi_psi",
    "C_psi",
    "Omega_psi_prime",
    "R_geo",
}
REQUIRED_EDGES = {
    ("Omega_psi", "Xi_psi"),
    ("Xi_psi", "Pi5_psi"),
    ("Pi5_psi", "Phi_psi"),
    ("Phi_psi", "C_psi"),
    ("C_psi", "Omega_psi_prime"),
}
AO_ROLE_BY_OUTPUT = {
    "concordancia_local": "evidencia_auxiliar_equivalencia_local",
    "reorganizacion_local_habilitada": "evidencia_auxiliar_con_deuda",
    "friccion_relevante": "evidencia_friccion_confluencia_local",
    "friccion_desorganizante": "bloqueo_transitabilidad_sin_uso_positivo",
    "discordancia_local": "deuda_local_direccion_no_cierre",
    "disolucion_local": "bloqueo_comparabilidad_sin_uso_positivo",
    "fuera_de_alcance": "bloqueo_alcance_sin_uso_positivo",
    "indeterminado_por_falta_de_evidencia": "bloqueo_evidencia_sin_uso_positivo",
}


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    external_case: str
    expected: str
    actual: str
    passed: bool
    rule_id: str
    priority: int
    ao_role: str
    graph_valid: bool
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]
    operator_trace: dict[str, Any]
    ao_bridge: dict[str, Any]


def load_suite(path: Path = DEFAULT_CASE_FILE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _metric(case: dict[str, Any], key: str) -> int:
    raw = dict(case.get("metrics", {})).get(key, 0)
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return 0
    if value < 0:
        return 0
    if value > 2:
        return 2
    return value


def _metrics(case: dict[str, Any]) -> dict[str, int]:
    return {key: _metric(case, key) for key in METRIC_KEYS}


def _flags(case: dict[str, Any]) -> dict[str, bool]:
    return {str(key): bool(value) for key, value in dict(case.get("flags", {})).items()}


def _graph_validation(suite: dict[str, Any]) -> tuple[bool, tuple[str, ...], tuple[str, ...]]:
    template = dict(suite.get("graph_template", {}))
    nodes = {str(node) for node in template.get("nodes", [])}
    edges = {tuple(edge) for edge in template.get("edges", []) if isinstance(edge, list) and len(edge) == 2}
    blockers: list[str] = []
    warnings: list[str] = []

    missing_nodes = sorted(REQUIRED_NODES - nodes)
    missing_edges = sorted(REQUIRED_EDGES - edges)
    if missing_nodes:
        blockers.append("nodos_minimos_ausentes:" + ",".join(missing_nodes))
    if missing_edges:
        blockers.append("aristas_minimas_ausentes:" + ",".join(f"{a}->{b}" for a, b in missing_edges))
    if "TrueSelf_psi" in nodes:
        warnings.append("trueself_psi_presente_solo_como_notacion_externa")
    return not blockers, tuple(blockers), tuple(warnings)


def _rule_output(case: dict[str, Any], metrics: dict[str, int], graph_valid: bool) -> tuple[str, str, int]:
    flags = _flags(case)
    if not graph_valid:
        return "indeterminado_por_falta_de_evidencia", "G-TRACE-R0-GRAFO-INCOMPLETO", 0
    if flags.get("clinical_domain") or flags.get("regulated_domain") or flags.get("real_person"):
        return "fuera_de_alcance", "G0-DOMINIO-NO-AUTORIZADO", 1
    if flags.get("h_xi_claim") or flags.get("canon_claim") or flags.get("true_self_authority"):
        return "fuera_de_alcance", "G0-AUTORIDAD-NO-AUTORIZADA", 1
    if metrics["G_scope"] == 0 or flags.get("identity_global_claim"):
        return "fuera_de_alcance", "G0-ALCANCE", 1
    if any(metrics[key] == 0 for key in ("G_olc", "G_embed", "G_phi", "G_evid")):
        return "indeterminado_por_falta_de_evidencia", "G1-EVIDENCIA-PROYECCION", 2
    if any(metrics[key] == 0 for key in MIN_GEOMETRIC_KEYS):
        return "disolucion_local", "G2-MINIMOS-GEOMETRICOS", 3
    if metrics["G_unity"] >= 1 and metrics["G_path"] >= 1 and flags.get("conflict_direction"):
        return "discordancia_local", "G3-DISCORDANCIA-DIRECCION", 4
    if metrics["G_Aexp"] == 0:
        if flags.get("friction_blocks_transitability"):
            return "friccion_desorganizante", "G4-EXPECTATIVA-FIJA-DESORGANIZANTE", 5
        return "friccion_relevante", "G4-EXPECTATIVA-FIJA", 5
    if (
        metrics["G_path"] >= 1
        and metrics["G_OmegaPhi"] >= 1
        and metrics["G_Cpsi"] >= 1
        and metrics["G_unity"] >= 1
        and metrics["G_Aexp"] >= 1
        and flags.get("recomposition_declared")
    ):
        return "reorganizacion_local_habilitada", "G5-REORGANIZACION-LOCAL", 6
    concordance = (
        metrics["G_scope"] == 2
        and metrics["G_olc"] == 2
        and metrics["G_embed"] == 2
        and metrics["G_T"] >= 1
        and metrics["G_E"] >= 1
        and metrics["G_path"] >= 1
        and metrics["G_Aprism"] >= 1
        and metrics["G_Vprism"] >= 1
        and metrics["G_OmegaPhi"] >= 1
        and metrics["G_tau_fit"] >= 1
        and metrics["G_adapt"] >= 1
        and metrics["G_unity"] == 2
        and metrics["G_Aexp"] == 2
        and metrics["G_Cpsi"] >= 1
        and metrics["G_phi"] == 2
        and metrics["G_evid"] >= 1
    )
    if concordance:
        return "concordancia_local", "G6-CONCORDANCIA-LOCAL", 7
    return "friccion_relevante", "G7-FRICCION-RESIDUAL", 8


def evaluate_case(case: dict[str, Any], suite: dict[str, Any]) -> CaseResult:
    metrics = _metrics(case)
    flags = _flags(case)
    graph_valid, graph_blockers, graph_warnings = _graph_validation(suite)
    actual, rule_id, priority = _rule_output(case, metrics, graph_valid)
    expected = str(case.get("expected", "")).strip()
    blockers = list(graph_blockers)
    warnings = list(graph_warnings)

    if not str(case.get("object", "")).strip() or not str(case.get("limit", "")).strip() or not str(case.get("criterion", "")).strip():
        blockers.append("objeto_limite_criterio_incompleto")
    if not case.get("evidence"):
        blockers.append("evidencia_ausente")
    if flags.get("practical_advice_real_person"):
        blockers.append("consejo_practico_persona_real_no_autorizado")
    if flags.get("xi_equals_trueself"):
        blockers.append("xi_igualado_a_trueself")
    if blockers and actual == "concordancia_local":
        actual = "indeterminado_por_falta_de_evidencia"
        rule_id = "G1-BLOQUEO-FALSADOR"
        priority = 2

    ao_role = AO_ROLE_BY_OUTPUT.get(actual, "bloqueo_evidencia_sin_uso_positivo")
    operator_trace = {
        "operator_id": "OP_MOC_GEO_GRAPH",
        "case_id": str(case.get("case_id", "")),
        "external_case": str(case.get("external_case", "")),
        "output": actual,
        "rule_id": rule_id,
        "priority": priority,
        "metric_vector": metrics,
        "graph_validation": {
            "valid": graph_valid,
            "required_nodes_present": graph_valid,
            "required_edges_present": graph_valid,
        },
        "source_evidence": case.get("evidence", []),
        "blockers": sorted(blockers),
        "warnings": sorted(warnings),
    }
    ao_bridge = {
        "ao_role": ao_role,
        "operator_trace_id": "OP_MOC_GEO_GRAPH",
        "closes_equivalence_global": False,
        "closes_confluence_global": False,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "modifies_doc04": False,
        "modifies_canon": False,
        "modifies_nivel_c": False,
        "transformacion_permitida": False,
    }
    return CaseResult(
        case_id=str(case.get("case_id", "")),
        external_case=str(case.get("external_case", "")),
        expected=expected,
        actual=actual,
        passed=actual == expected and not blockers,
        rule_id=rule_id,
        priority=priority,
        ao_role=ao_role,
        graph_valid=graph_valid,
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
        operator_trace=operator_trace,
        ao_bridge=ao_bridge,
    )


def summarize(results: list[CaseResult]) -> dict[str, Any]:
    by_output: dict[str, int] = {}
    by_role: dict[str, int] = {}
    for result in results:
        by_output[result.actual] = by_output.get(result.actual, 0) + 1
        by_role[result.ao_role] = by_role.get(result.ao_role, 0) + 1
    failures = [result for result in results if not result.passed]
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "graph_valid_cases": sum(1 for result in results if result.graph_valid),
        "operator_traces": len(results),
        "by_output": by_output,
        "by_ao_role": by_role,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(item, suite) for item in suite.get("cases", [])]
    summary = summarize(results)
    failures = [result for result in results if not result.passed]
    return {
        "report_id": "MOC-EXP-GRAPH-CHECK-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "MOC-EXP-GRAPH-001-CASES"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "mantener_como_evidencia_local_no_canonica" if not failures else "revisar_casos_grafo_experiencia",
        "transformacion_permitida": False,
        "external_evidence_imported": True,
        "external_evidence_executed": False,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "global_equivalence_authorized": False,
        "global_confluence_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "tests_executed": [
            "MOC-EXP-GRAPH-001",
            "MOC-GEO-METR-LAB-001",
            "MOC-AO-GEO-BRIDGE-001",
        ],
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "admite_h_xi": False,
            "canoniza_xi": False,
            "canoniza_phi": False,
            "usa_trueself_como_autoridad": False,
            "uso_clinico": False,
            "usa_personas_reales": False,
            "usa_dominio_regulado": False,
            "modifica_doc04": False,
            "modifica_canon": False,
            "modifica_nivel_c": False,
            "promueve_report_layer": False,
            "exporta_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "summary": summary,
        "results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# MOC_EXP_GRAPH_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "external_evidence_imported: true",
        "external_evidence_executed: false",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "global_equivalence_authorized: false",
        "global_confluence_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- operator_traces: {report['summary']['operator_traces']}",
        "",
        "## Salidas",
        "",
    ]
    for output, count in sorted(report["summary"]["by_output"].items()):
        lines.append(f"- {output}: {count}")
    lines.extend(["", "## Casos", ""])
    for result in report["results"]:
        lines.append(
            "- {case_id} ({external_case}): {actual} / esperado {expected} / regla {rule_id} / AO {ao_role}".format(
                **result
            )
        )
    if report["findings"]:
        lines.extend(["", "## Hallazgos", ""])
        for finding in report["findings"]:
            lines.append(f"- {finding['case_id']}: {finding['actual']} != {finding['expected']}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validador no mutante de grafo de experiencia MOC.")
    parser.add_argument("--case-file", type=Path, default=DEFAULT_CASE_FILE)
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta opcional de salida.")
    args = parser.parse_args(argv)

    report = build_report(case_file=args.case_file)
    output = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.format == "md":
        output = render_md(report)
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0 if report["resultado"] == "ok" else 2


if __name__ == "__main__":
    raise SystemExit(main())

