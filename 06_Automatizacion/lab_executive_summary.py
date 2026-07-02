#!/usr/bin/env python3
"""Resumen ejecutivo automatico no mutante del Laboratorio."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

RUN_REPORT = "06_Automatizacion/reportes/lab_run_report.json"
RISK_REPORT = "06_Automatizacion/reportes/lab_risk_report.json"
BOARD_REPORT = "06_Automatizacion/reportes/lab_status_board.json"
CONTINUITY_REPORT = "06_Automatizacion/reportes/lab_continuity_report.json"
CURRENT_STATE = "CURRENT_STATE.md"
PROJECT_STATE = "05_Estado_Proyecto/ESTADO_ACTUAL.md"
AUT_CLOSE_DECISION = "03_Expedientes/AUT-001_Decision_Cierre_Operativo_Completo.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def first_bullet_after(text: str, heading: str) -> str:
    inside = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == heading:
            inside = True
            continue
        if inside and stripped.startswith("## "):
            break
        if inside and stripped.startswith("- "):
            return stripped[2:].strip()
    return ""


def bullets_after(text: str, heading: str) -> list[str]:
    inside = False
    values: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == heading:
            inside = True
            continue
        if inside and stripped.startswith("## "):
            break
        if inside and stripped.startswith("- "):
            values.append(stripped[2:].strip())
    return values


def section_text_after(text: str, heading: str) -> str:
    lines = text.splitlines()
    inside = False
    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == heading:
            inside = True
            continue
        if inside and stripped.startswith("## "):
            break
        if inside and stripped:
            out.append(stripped)
    return " ".join(out).strip()


def safe_load_json(root: Path, rel_path: str, fallback: dict[str, Any] | None = None) -> dict[str, Any]:
    path = root / rel_path
    if not path.exists():
        return fallback or {"missing": True, "path": rel_path}
    return read_json(path)


def risk_top_items(risk_report: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    findings = risk_report.get("findings", [])
    active = [item for item in findings if item.get("category") == "riesgo_activo"]
    order = {"alta": 0, "media": 1, "baja": 2}
    return sorted(active, key=lambda item: (order.get(item.get("operational_severity", "baja"), 9), item.get("file", "")))[:limit]


def executive_result(run_report: dict[str, Any], risk_report: dict[str, Any], closure_registered: bool = False) -> tuple[str, str, str]:
    findings = risk_report.get("findings", [])
    active = [item for item in findings if item.get("category") == "riesgo_activo"]
    active_high = [item for item in active if item.get("operational_severity") == "alta"]
    controlled = [item for item in findings if item.get("category") == "advertencia_controlada"]
    if active_high:
        return "atencion_requerida", "revisar_riesgos_altos_sin_transformar", "Operativo con riesgos altos activos; no cerrar."
    if active:
        return "advertencia", "priorizar_riesgos_activos", "Operativo con riesgos activos pendientes."
    if closure_registered:
        if run_report.get("resultado") == "ok":
            return "ok", "mantener_cierre_operativo", "Cierre operativo conservado sin riesgos activos clasificados."
        return "advertencia", "mantener_cierre_operativo", "Cierre operativo conservado con deuda documental visible."
    if controlled:
        return "advertencia", "preparar_cierre_tecnico_provisional", "Operativo con advertencias controladas y cierre tecnico provisional preparado."
    if run_report.get("resultado") == "advertencia":
        return "advertencia", "preparar_cierre_tecnico_provisional", "Operativo con advertencias no bloqueantes visibles."
    return "ok", "aprobar_lectura", "Operativo sin riesgos activos clasificados."


def build_report(
    root: Path,
    run_report: dict[str, Any] | None = None,
    risk_report: dict[str, Any] | None = None,
    board_report: dict[str, Any] | None = None,
    continuity_report: dict[str, Any] | None = None,
) -> dict[str, Any]:
    current = read_text(root / CURRENT_STATE) if (root / CURRENT_STATE).exists() else ""
    project = read_text(root / PROJECT_STATE) if (root / PROJECT_STATE).exists() else ""
    run = run_report or safe_load_json(root, RUN_REPORT)
    risk = risk_report or safe_load_json(root, RISK_REPORT)
    board = board_report or safe_load_json(root, BOARD_REPORT)
    continuity = continuity_report or safe_load_json(root, CONTINUITY_REPORT)

    active_line = first_bullet_after(current, "Expediente activo inmediato:") or board.get("state", {}).get("expediente_activo_inmediato", "")
    next_objective = first_bullet_after(current, "Proximo objetivo:") or section_text_after(project, "## Proximo objetivo")
    latest_decision = first_bullet_after(current, "Ultima decision operativa:") or board.get("state", {}).get("ultima_decision_operativa", "")
    open_expedientes = bullets_after(project, "## Expedientes abiertos") or board.get("state", {}).get("expedientes_abiertos", [])

    closure_registered = (root / AUT_CLOSE_DECISION).exists()
    resultado, recomendacion, headline = executive_result(run, risk, closure_registered)
    risk_summary = risk.get("summary", {})
    run_steps = run.get("steps", [])

    next_actions = [
        "Decidir o mantener cierre de AUT-001.",
        "Mantener advertencias controladas visibles en reportes.",
        "Mantener transformacion_permitida en false hasta decision explicita.",
    ]
    if closure_registered:
        next_actions[0] = "Mantener cierre operativo de AUT-001 con deuda documental visible."

    return {
        "report_id": "DO-LAB-SUMMARY-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-LAB-SUMMARY-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "headline": headline,
        "state": {
            "expediente_activo_inmediato": active_line,
            "proximo_objetivo": next_objective,
            "ultima_decision_operativa": latest_decision,
            "expedientes_abiertos": open_expedientes,
        },
        "automation": {
            "run_resultado": run.get("resultado", "no_detectado"),
            "run_recomendacion": run.get("recomendacion", "no_detectada"),
            "steps": run_steps,
            "continuity_resultado": continuity.get("resultado", "no_detectado"),
            "board_resultado": board.get("resultado", "no_detectado"),
        },
        "risk": {
            "resultado": risk.get("resultado", "no_detectado"),
            "recomendacion": risk.get("recomendacion", "no_detectada"),
            "by_category": risk_summary.get("by_category", {}),
            "by_operational_severity": risk_summary.get("by_operational_severity", {}),
            "by_context_class": risk_summary.get("by_context_class", {}),
            "by_treatment_status": risk_summary.get("by_treatment_status", {}),
            "risk_blocks_closure": risk_summary.get("risk_blocks_closure", False),
            "top_active": risk_top_items(risk),
        },
        "sources": {
            "run": run.get("report_id"),
            "risk": risk.get("report_id"),
            "board": board.get("report_id"),
            "continuity": continuity.get("report_id"),
        },
        "next_actions": next_actions,
    }


def render_md(report: dict[str, Any]) -> str:
    state = report["state"]
    risk = report["risk"]
    automation = report["automation"]
    lines = [
        "# LAB_EXECUTIVE_SUMMARY",
        "",
        f"report_id: {report['report_id']}",
        "expediente: AUT-001",
        "algoritmo: DO-LAB-SUMMARY-001",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "",
        "## Lectura ejecutiva",
        "",
        f"- {report['headline']}",
        f"- corrida unificada: {automation['run_resultado']} / {automation['run_recomendacion']}",
        f"- clasificacion de riesgos: {risk['resultado']} / {risk['recomendacion']}",
        "",
        "## Estado operativo",
        "",
        f"- frente activo: {state['expediente_activo_inmediato'] or 'no_detectado'}",
        f"- ultima decision: {state['ultima_decision_operativa'] or 'no_detectada'}",
        f"- proximo objetivo: {state['proximo_objetivo'] or 'no_detectado'}",
        "",
        "## Riesgos clasificados",
        "",
    ]
    for category in ("riesgo_activo", "advertencia_controlada", "deuda_documental", "advertencia_heredada", "observacion"):
        lines.append(f"- {category}: {risk['by_category'].get(category, 0)}")
    lines.extend(["", "## Contexto de riesgos", ""])
    for context_class, count in sorted(risk.get("by_context_class", {}).items()):
        lines.append(f"- {context_class}: {count}")
    lines.extend(["", "## Severidad", ""])
    for severity in ("alta", "media", "baja"):
        lines.append(f"- {severity}: {risk['by_operational_severity'].get(severity, 0)}")
    lines.extend(["", "## Riesgos activos principales", ""])
    top_active = risk.get("top_active", [])
    if not top_active:
        lines.append("- Sin riesgos activos principales.")
    else:
        for item in top_active:
            line = f"- [{item.get('operational_severity', 'no_detectada')}] {item.get('file', 'no_detectado')} - {item.get('kind', 'hallazgo')}: {item.get('detail', '')}"
            if item.get("evidence"):
                line += f" | evidencia: {item['evidence']}"
            lines.append(line)
    lines.extend(["", "## Automatizacion", ""])
    for step in automation.get("steps", []):
        lines.append(f"- {step.get('algorithm', 'no_detectado')}: {step.get('resultado', 'no_detectado')} ({step.get('findings', 0)} hallazgos)")
    lines.extend(["", "## Siguientes acciones", ""])
    lines.extend(f"- {item}" for item in report["next_actions"])
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Resumen ejecutivo automatico no mutante del Laboratorio.")
    parser.add_argument("--format", choices=("json", "md"), default="json")
    parser.add_argument("--output", help="Ruta de salida del reporte.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    report = build_report(root)
    output = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.format == "md":
        output = render_md(report)
    if args.output:
        out_path = (root / args.output).resolve()
        if root.resolve() not in out_path.parents and out_path != root.resolve():
            raise SystemExit(f"Salida fuera del repositorio: {args.output}")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
