#!/usr/bin/env python3
"""Implementacion no mutante inicial del Auditor v0 segun C-002."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any

EXPEDIENTE = "AUD-001"
ALGORITHM = "AUDITOR-V0-001"
CASE_IDS = [f"AUD-T{index:02d}" for index in range(10)]
SOURCES = [
    "02_Documentos/C-002_RFC_Operativo_Auditor_v0.md",
    "02_Documentos/C-001_Especificacion_Tecnica_Auditor.md",
    "03_Expedientes/AUD-001_Casos_Prueba_Auditor.md",
    "03_Expedientes/AUD-001_Contrato_Reportes.md",
    "03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md",
]


DEFAULT_CASES: list[dict[str, Any]] = [
    {
        "id": "AUD-T00",
        "kind": "automaton",
        "claim_status": "definicion",
        "declaration": {"deterministic": True, "complete": True},
        "automaton": {
            "states": ["q0", "q1"],
            "alphabet": ["0", "1"],
            "initial": "q0",
            "finals": ["q1"],
            "transitions": [
                ["q0", "0", "q0"],
                ["q0", "1", "q1"],
                ["q1", "0", "q0"],
                ["q1", "1", "q1"],
            ],
        },
    },
    {
        "id": "AUD-T01",
        "kind": "automaton",
        "claim_status": "definicion",
        "declaration": {"deterministic": True, "complete": True},
        "automaton": {
            "states": ["q0", "q1"],
            "alphabet": ["0", "1"],
            "initial": "q0",
            "finals": ["q1"],
            "transitions": [
                ["q0", "0", "q0"],
                ["q0", "1", "q1"],
                ["q1", "0", "q0"],
            ],
        },
    },
    {
        "id": "AUD-T02",
        "kind": "automaton",
        "claim_status": "definicion",
        "declaration": {"deterministic": True, "complete": False},
        "automaton": {
            "states": ["q0", "q1", "q2"],
            "alphabet": ["a"],
            "initial": "q0",
            "finals": ["q2"],
            "transitions": [
                ["q0", "a", "q1"],
                ["q1", "a", "q1"],
                ["q2", "a", "q2"],
            ],
        },
    },
    {
        "id": "AUD-T03",
        "kind": "automaton",
        "claim_status": "definicion",
        "declaration": {"deterministic": True, "complete": False},
        "automaton": {
            "states": ["q0", "q1"],
            "alphabet": ["x"],
            "initial": "q0",
            "finals": ["q1"],
            "transitions": [
                ["q0", "x", "q0"],
                ["q0", "x", "q1"],
                ["q1", "x", "q1"],
            ],
        },
    },
    {
        "id": "AUD-T04",
        "kind": "claim",
        "claim_status": "hipotesis",
        "claim": "A4a equivale a A4b",
        "justification": "se ve por inspeccion",
        "required_dependency": "algoritmo local de equivalencia o demostracion",
        "dependency_materialized": False,
    },
    {
        "id": "AUD-T05",
        "kind": "automaton",
        "claim_status": "expediente",
        "declaration": {"deterministic": True, "complete": False},
        "automaton": {
            "states": ["q0"],
            "alphabet": ["a"],
            "initial": "q0",
            "finals": ["q1"],
            "transitions": [["q0", "a", "q1"]],
        },
        "transformation": {
            "executed": True,
            "decision_emitida": "ausente",
            "description": "anadir q1 a Q y aceptar el cambio",
        },
    },
    {
        "id": "AUD-T06",
        "kind": "claim",
        "claim_status": "teorema",
        "claim": "Gamma(A) produce la generalizacion canonica del automata A",
        "required_dependency": "definicion local de Gamma",
        "dependency_materialized": False,
        "forbidden_promotion": "Gamma formal",
    },
    {
        "id": "AUD-T07",
        "kind": "authority",
        "claim_status": "decision",
        "claim": "resultado vigente fundado en conversacion historica",
        "source": "04_Registro_Historico",
        "registered_decision": False,
    },
    {
        "id": "AUD-T08",
        "kind": "level_change",
        "claim_status": "expediente",
        "surface": "01_Canon/M-000_Reglas_Fundamentales.md",
        "action": "modificar M-000 para incorporar R4-AUD",
        "registered_decision": False,
    },
    {
        "id": "AUD-T09",
        "kind": "term",
        "claim_status": "no_clasificado",
        "text": "El operador concordante resuelve la reduccion.",
        "term": "operador concordante",
        "term_status": "",
    },
]


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def report_id(case_id: str, operator: str, index: int) -> str:
    return f"{ALGORITHM}-{case_id}-{operator}-{index:02d}"


def op_report(
    case_id: str,
    operator: str,
    index: int,
    resultado: str,
    tipo: str,
    ubicacion: str,
    descripcion: str,
    evidencia: str,
    estatus_afirmacion: str,
    decision_permitida: list[str],
    decision_emitida: str,
    tau_requerido: str,
    tau_estado: str,
    dependencias: list[str] | None = None,
    deudas_generadas: list[str] | None = None,
    alternativas_no_decididas: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "report_id": report_id(case_id, operator, index),
        "expediente": EXPEDIENTE,
        "caso": case_id,
        "operador": operator,
        "resultado": resultado,
        "tipo": tipo,
        "ubicacion": ubicacion,
        "descripcion": descripcion,
        "evidencia": evidencia,
        "estatus_afirmacion": estatus_afirmacion,
        "alternativas_no_decididas": alternativas_no_decididas or [],
        "decision_permitida": decision_permitida,
        "decision_emitida": decision_emitida,
        "transformacion_permitida": False,
        "tau_requerido": tau_requerido,
        "tau_estado": tau_estado,
        "dependencias": dependencias or SOURCES,
        "deudas_generadas": deudas_generadas or [],
    }


def transition_tuples(case: dict[str, Any]) -> list[tuple[str, str, str]]:
    return [tuple(item) for item in case["automaton"].get("transitions", [])]


def automaton_findings(case: dict[str, Any]) -> list[dict[str, Any]]:
    case_id = case["id"]
    claim_status = case.get("claim_status", "no_clasificado")
    automaton = case["automaton"]
    states = set(automaton.get("states", []))
    alphabet = set(automaton.get("alphabet", []))
    initial = automaton.get("initial")
    finals = set(automaton.get("finals", []))
    transitions = transition_tuples(case)
    declaration = case.get("declaration", {})
    reports: list[dict[str, Any]] = []
    index = 1

    invalid_refs: list[str] = []
    if initial not in states:
        invalid_refs.append(f"estado inicial fuera de Q: {initial}")
    for final in sorted(finals - states):
        invalid_refs.append(f"estado final fuera de Q: {final}")
    for src, symbol, dst in transitions:
        if src not in states:
            invalid_refs.append(f"origen fuera de Q: {src}")
        if dst not in states:
            invalid_refs.append(f"destino fuera de Q: {dst}")
        if symbol not in alphabet:
            invalid_refs.append(f"simbolo fuera de Sigma: {symbol}")
    if invalid_refs:
        reports.append(
            op_report(
                case_id,
                "Mp",
                index,
                "falla",
                "dependencia_no_registrada",
                "automata",
                "El mapeo referencia estados o simbolos no declarados.",
                "; ".join(invalid_refs),
                claim_status,
                ["bloquear", "escalar", "continuar_sin_transformar"],
                "bloquear",
                "bloqueo_temprano",
                "bloqueo_temprano",
                deudas_generadas=["normalizar declaracion del automata antes de calcular"],
            )
        )
        index += 1

    if declaration.get("complete"):
        present = {(src, symbol) for src, symbol, _ in transitions}
        missing = sorted((state, symbol) for state in states for symbol in alphabet if (state, symbol) not in present)
        if missing:
            evidence = ", ".join(f"({state}, {symbol})" for state, symbol in missing)
            reports.append(
                op_report(
                    case_id,
                    "Mp",
                    index,
                    "falla",
                    "ambiguedad",
                    "delta",
                    "El automata declara completitud, pero faltan transiciones.",
                    evidence,
                    claim_status,
                    ["bloquear", "continuar_sin_transformar"],
                    "bloquear",
                    "bloqueo_temprano",
                    "bloqueo_temprano",
                    deudas_generadas=["completar delta o retirar declaracion de completitud"],
                )
            )
            index += 1

    if declaration.get("deterministic"):
        counter = Counter((src, symbol) for src, symbol, _ in transitions)
        duplicates = sorted(pair for pair, count in counter.items() if count > 1)
        if duplicates:
            evidence = ", ".join(f"({state}, {symbol})" for state, symbol in duplicates)
            reports.append(
                op_report(
                    case_id,
                    "Cr",
                    index,
                    "falla",
                    "contradiccion",
                    "delta",
                    "La declaracion de determinismo contradice transiciones duplicadas.",
                    evidence,
                    claim_status,
                    ["bloquear"],
                    "bloquear",
                    "bloqueo_temprano",
                    "bloqueo_temprano",
                    deudas_generadas=["resolver contradiccion de determinismo"],
                )
            )
            index += 1

    if not any(report["operador"] == "Mp" and report["resultado"] == "falla" for report in reports):
        reachable = reachable_states(initial, transitions)
        unreachable_finals = sorted(finals - reachable)
        if unreachable_finals:
            reports.append(
                op_report(
                    case_id,
                    "Cr",
                    index,
                    "escalado",
                    "deuda_conceptual",
                    "F",
                    "Existe estado final inalcanzable desde el estado inicial.",
                    ", ".join(unreachable_finals),
                    claim_status,
                    ["escalar", "continuar_sin_transformar"],
                    "escalar",
                    "escalamiento",
                    "escalamiento",
                    deudas_generadas=["justificar finalidad o corregir alcanzabilidad"],
                )
            )
            index += 1

    transformation = case.get("transformation")
    if transformation and transformation.get("executed") and transformation.get("decision_emitida") != "continuar_con_cambio_acotado":
        reports.append(
            op_report(
                case_id,
                "Tr",
                index,
                "bloqueado",
                "violacion_r4_aud",
                "transformacion",
                "Se detecta transformacion ejecutada sin decision fundada.",
                transformation.get("description", "transformacion sin decision"),
                claim_status,
                ["bloquear"],
                "bloquear",
                "bloqueo_temprano",
                "bloqueo_temprano",
                deudas_generadas=["registrar permiso valido antes de cualquier ejecucion"],
            )
        )

    if not reports:
        reports.append(
            op_report(
                case_id,
                "D",
                1,
                "ok",
                "sin_hallazgo_bloqueante",
                "integracion",
                "La lectura no detecta hallazgos bloqueantes.",
                "Mp, Cr, tau y D conservan separacion; Tr no se ejecuta.",
                claim_status,
                ["aprobar", "continuar_sin_transformar"],
                "aprobar",
                "exito",
                "exito",
            )
        )
    return reports


def reachable_states(initial: str, transitions: list[tuple[str, str, str]]) -> set[str]:
    graph: dict[str, list[str]] = {}
    for src, _symbol, dst in transitions:
        graph.setdefault(src, []).append(dst)
    seen: set[str] = set()
    queue: deque[str] = deque([initial])
    while queue:
        state = queue.popleft()
        if state in seen:
            continue
        seen.add(state)
        queue.extend(graph.get(state, []))
    return seen


def claim_findings(case: dict[str, Any]) -> list[dict[str, Any]]:
    case_id = case["id"]
    claim_status = case.get("claim_status", "no_clasificado")
    dependency = case.get("required_dependency", "dependencia local")
    claim = case.get("claim", "")
    if not case.get("dependency_materialized", False):
        tipo = "dependencia_no_registrada"
        descripcion = "La afirmacion requiere una dependencia local no materializada."
        if case.get("forbidden_promotion"):
            tipo = "deuda_conceptual"
            descripcion = "La afirmacion promueve una construccion formal sin definicion local."
        return [
            op_report(
                case_id,
                "D",
                1,
                "bloqueado",
                tipo,
                "afirmacion",
                descripcion,
                f"{claim}; falta: {dependency}",
                claim_status,
                ["bloquear", "continuar_sin_transformar"],
                "bloquear",
                "bloqueo_temprano",
                "bloqueo_temprano",
                deudas_generadas=[dependency],
            )
        ]
    return []


def authority_findings(case: dict[str, Any]) -> list[dict[str, Any]]:
    if case.get("source", "").startswith("04_Registro_Historico") and not case.get("registered_decision"):
        return [
            op_report(
                case["id"],
                "D",
                1,
                "bloqueado",
                "dependencia_no_registrada",
                "fuente",
                "El Registro Historico aparece como autoridad directa sin decision registrada.",
                case.get("source", ""),
                case.get("claim_status", "no_clasificado"),
                ["bloquear", "escalar"],
                "bloquear",
                "bloqueo_temprano",
                "bloqueo_temprano",
                deudas_generadas=["convertir pista historica en decision o documento vigente antes de usarla"],
            )
        ]
    return []


def level_change_findings(case: dict[str, Any]) -> list[dict[str, Any]]:
    if case.get("surface", "").startswith("01_Canon/") and not case.get("registered_decision"):
        return [
            op_report(
                case["id"],
                "D",
                1,
                "bloqueado",
                "violacion_r4_aud",
                case.get("surface", ""),
                "Un expediente intenta modificar Canon sin decision explicita.",
                case.get("action", ""),
                case.get("claim_status", "no_clasificado"),
                ["bloquear"],
                "bloquear",
                "bloqueo_temprano",
                "bloqueo_temprano",
                deudas_generadas=["mantener R4-AUD dentro de AUD-001 hasta decision superior"],
            )
        ]
    return []


def term_findings(case: dict[str, Any]) -> list[dict[str, Any]]:
    if not case.get("term_status"):
        return [
            op_report(
                case["id"],
                "Mp",
                1,
                "escalado",
                "deuda_conceptual",
                "termino",
                "El texto introduce un termino nuevo sin estatus declarado.",
                case.get("term", ""),
                "no_clasificado",
                ["escalar", "continuar_sin_transformar"],
                "continuar_sin_transformar",
                "interrupcion_por_deuda",
                "interrupcion_por_deuda",
                deudas_generadas=[f"declarar estatus de {case.get('term', 'termino nuevo')}"],
            )
        ]
    return []


def evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    kind = case.get("kind")
    if kind == "automaton":
        reports = automaton_findings(case)
    elif kind == "claim":
        reports = claim_findings(case)
    elif kind == "authority":
        reports = authority_findings(case)
    elif kind == "level_change":
        reports = level_change_findings(case)
    elif kind == "term":
        reports = term_findings(case)
    else:
        reports = [
            op_report(
                case.get("id", "AUD-TXX"),
                "Mp",
                1,
                "falla",
                "deuda_conceptual",
                "caso",
                "Tipo de caso no reconocido.",
                str(kind),
                "no_clasificado",
                ["escalar"],
                "escalar",
                "escalamiento",
                "escalamiento",
            )
        ]
    return {
        "case_id": case["id"],
        "kind": kind,
        "resultado": result_for_reports(reports),
        "transformacion_permitida": False,
        "reports": reports,
    }


def result_for_reports(reports: list[dict[str, Any]]) -> str:
    decisions = {report.get("decision_emitida") for report in reports}
    results = {report.get("resultado") for report in reports}
    if "bloquear" in decisions or "bloqueado" in results or "falla" in results:
        return "bloqueado"
    if "escalar" in decisions or "escalado" in results:
        return "advertencia"
    return "ok"


def load_cases(root: Path, case_file: str | None) -> list[dict[str, Any]]:
    if not case_file:
        return DEFAULT_CASES
    path = root / case_file
    assert_inside(root, path)
    loaded = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(loaded, dict):
        loaded = loaded.get("cases", [])
    if not isinstance(loaded, list):
        raise SystemExit("El archivo de casos debe contener una lista o {cases: [...]}.")
    return loaded


def build_report(root: Path, case_file: str | None = None) -> dict[str, Any]:
    cases = load_cases(root, case_file)
    evaluated = [evaluate_case(case) for case in cases]
    all_reports = [report for case in evaluated for report in case["reports"]]
    covered = sorted({case["case_id"] for case in evaluated})
    missing = [case_id for case_id in CASE_IDS if case_id not in covered]
    blocking = [case for case in evaluated if case["resultado"] == "bloqueado"]
    warnings = [case for case in evaluated if case["resultado"] == "advertencia"]
    return {
        "report_id": "AUDITOR-V0-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM,
        "base_normativa": "C-002",
        "modo": "no_mutante",
        "transformacion_permitida": False,
        "conforme_c002": not missing and all(not report["transformacion_permitida"] for report in all_reports),
        "fuentes": SOURCES,
        "summary": {
            "cases_checked": len(evaluated),
            "mandatory_cases": len(CASE_IDS),
            "mandatory_missing": missing,
            "ok": sum(1 for case in evaluated if case["resultado"] == "ok"),
            "advertencia": len(warnings),
            "bloqueado": len(blocking),
            "operator_reports": len(all_reports),
            "by_operator": dict(Counter(report["operador"] for report in all_reports)),
            "by_tipo": dict(Counter(report["tipo"] for report in all_reports)),
        },
        "cases": evaluated,
    }


def render_md(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# AUDITOR_V0_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {report['expediente']}",
        f"algoritmo: {report['algoritmo']}",
        f"base_normativa: {report['base_normativa']}",
        f"modo: {report['modo']}",
        f"conforme_c002: {str(report['conforme_c002']).lower()}",
        "transformacion_permitida: false",
        "",
        "## Resumen",
        "",
        f"- casos revisados: {summary['cases_checked']}",
        f"- casos obligatorios faltantes: {len(summary['mandatory_missing'])}",
        f"- ok: {summary['ok']}",
        f"- advertencia: {summary['advertencia']}",
        f"- bloqueado: {summary['bloqueado']}",
        f"- reportes de operador: {summary['operator_reports']}",
        "",
        "## Casos",
        "",
    ]
    for case in report["cases"]:
        lines.append(f"### {case['case_id']} - {case['resultado']}")
        lines.append("")
        for item in case["reports"]:
            lines.append(
                "- "
                + f"{item['operador']} / {item['resultado']} / {item['tipo']}: "
                + f"{item['descripcion']} "
                + f"Decision: {item['decision_emitida']}. "
                + f"Transformacion: {str(item['transformacion_permitida']).lower()}."
            )
        lines.append("")
    lines.extend(["## Fuentes", ""])
    lines.extend(f"- {source}" for source in report["fuentes"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Auditor v0 no mutante conforme C-002.")
    parser.add_argument("--case-file", help="Archivo JSON opcional con casos a evaluar.")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta de salida del reporte.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    report = build_report(root, args.case_file)
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
    return 0 if report["conforme_c002"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
