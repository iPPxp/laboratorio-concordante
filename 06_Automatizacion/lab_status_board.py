#!/usr/bin/env python3
"""Tablero no mutante de estado del Laboratorio Concordante."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "CURRENT_STATE.md",
    "05_Estado_Proyecto/ESTADO_ACTUAL.md",
    "HANDOFF.md",
    "README.md",
]

AUTOMATION_FILES = [
    "06_Automatizacion/do_check_min.py",
    "06_Automatizacion/do_check_med.py",
    "06_Automatizacion/lab_status_board.py",
    "06_Automatizacion/lab_continuity_report.py",
    "06_Automatizacion/lab_risk_classifier.py",
    "06_Automatizacion/lab_executive_summary.py",
    "06_Automatizacion/lab_run.py",
    "06_Automatizacion/r001_table_checks.py",
    "06_Automatizacion/ao_ext_confluence.py",
    "06_Automatizacion/ao_doc04_wide_tests.py",
    "06_Automatizacion/moc_eval.py",
]

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def first_bullet_after(text: str, heading: str) -> str:
    lines = text.splitlines()
    inside = False
    for line in lines:
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
    lines = text.splitlines()
    inside = False
    values: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == heading:
            inside = True
            continue
        if inside and stripped.startswith("## "):
            break
        if inside and stripped.startswith("- "):
            values.append(stripped[2:].strip())
    return values


def scalar_after(text: str, label: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == label:
            for nxt in lines[i + 1 : i + 5]:
                stripped = nxt.strip()
                if stripped.startswith("- "):
                    return stripped[2:].strip()
                if stripped and not stripped.startswith("#"):
                    return stripped.strip()
    return ""


def build_report(root: Path) -> dict:
    missing = [name for name in REQUIRED_FILES if not (root / name).exists()]
    current = read(root / "CURRENT_STATE.md") if (root / "CURRENT_STATE.md").exists() else ""
    estado = read(root / "05_Estado_Proyecto/ESTADO_ACTUAL.md") if (root / "05_Estado_Proyecto/ESTADO_ACTUAL.md").exists() else ""

    findings = []
    for name in missing:
        findings.append({"severity": "block", "kind": "fuente_ausente", "file": name, "detail": "Fuente minima no encontrada."})

    automation_status = []
    for name in AUTOMATION_FILES:
        exists = (root / name).exists()
        automation_status.append({"file": name, "exists": exists})
        if not exists:
            findings.append({"severity": "warning", "kind": "automatizacion_ausente", "file": name, "detail": "Herramienta esperada no encontrada."})

    last_operational = first_bullet_after(current, "Ultima decision operativa:")
    next_objective = first_bullet_after(current, "Proximo objetivo:")
    active = first_bullet_after(current, "Expediente activo inmediato:")

    open_exps = bullets_after(estado, "## Expedientes abiertos")
    closed_exps = bullets_after(estado, "## Expedientes cerrados")
    frozen_exps = bullets_after(estado, "## Expedientes congelados")

    if not next_objective:
        findings.append({"severity": "warning", "kind": "objetivo_no_detectado", "file": "CURRENT_STATE.md", "detail": "No se detecto proximo objetivo."})
    if not open_exps:
        findings.append({"severity": "warning", "kind": "expedientes_abiertos_no_detectados", "file": "05_Estado_Proyecto/ESTADO_ACTUAL.md", "detail": "No se detectaron expedientes abiertos."})

    severities = {item["severity"] for item in findings}
    if "block" in severities:
        resultado = "bloqueado"
        recomendacion = "bloquear"
    elif "warning" in severities:
        resultado = "advertencia"
        recomendacion = "continuar_sin_transformar"
    else:
        resultado = "ok"
        recomendacion = "aprobar_lectura"

    return {
        "report_id": "DO-STATE-BOARD-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-STATE-BOARD-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "summary": {
            "missing_required_files": len(missing),
            "open_expedientes": len(open_exps),
            "closed_expedientes": len(closed_exps),
            "frozen_expedientes": len(frozen_exps),
            "findings": len(findings),
        },
        "state": {
            "ultimo_expediente_cerrado": scalar_after(current, "Ultimo expediente cerrado:"),
            "ultimo_expediente_tecnico_cerrado": scalar_after(current, "Ultimo expediente tecnico cerrado:"),
            "ultima_decision_operativa": last_operational,
            "proximo_objetivo": next_objective,
            "expediente_activo_inmediato": active,
            "expedientes_abiertos": open_exps,
            "expedientes_cerrados": closed_exps,
            "expedientes_congelados": frozen_exps,
            "automatizacion": automation_status,
        },
        "findings": findings,
    }


def render_md(report: dict) -> str:
    state = report["state"]
    lines = [
        "# LAB_STATUS_BOARD",
        "",
        f"report_id: {report['report_id']}",
        "expediente: AUT-001",
        "algoritmo: DO-STATE-BOARD-001",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "",
        "## Estado sintetico",
        "",
        f"- ultimo expediente cerrado: {state['ultimo_expediente_cerrado'] or 'no_detectado'}",
        f"- ultimo expediente tecnico cerrado: {state['ultimo_expediente_tecnico_cerrado'] or 'no_detectado'}",
        f"- ultima decision operativa: {state['ultima_decision_operativa'] or 'no_detectada'}",
        f"- proximo objetivo: {state['proximo_objetivo'] or 'no_detectado'}",
        "",
        "## Expediente activo inmediato",
        "",
        state["expediente_activo_inmediato"] or "no_detectado",
        "",
        "## Expedientes abiertos",
        "",
    ]
    lines.extend(f"- {item}" for item in state["expedientes_abiertos"] or ["no_detectado"])
    lines.extend(["", "## Automatizacion", ""])
    for item in state["automatizacion"]:
        status = "presente" if item["exists"] else "ausente"
        lines.append(f"- {item['file']}: {status}")
    lines.extend(["", "## Hallazgos", ""])
    if report["findings"]:
        for item in report["findings"]:
            lines.append(f"- [{item['severity']}] {item['file']} - {item['kind']}: {item['detail']}")
    else:
        lines.append("- Sin hallazgos.")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Tablero no mutante de estado del Laboratorio.")
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
    return 0 if report["resultado"] in {"ok", "advertencia"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
