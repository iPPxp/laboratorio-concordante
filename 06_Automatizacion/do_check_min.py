#!/usr/bin/env python3
"""Verificador minimo no mutante del Laboratorio Concordante."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

REQUIRED_SOURCES = [
    "CURRENT_STATE.md",
    "05_Estado_Proyecto/ESTADO_ACTUAL.md",
    "01_Canon/M-000_Reglas_Fundamentales.md",
    "01_Canon/M-001_Auditoria_Arquitectonica.md",
    "03_Expedientes/DO-001_DO-CHECK-001.md",
]

EXCLUDED_DIRS = {".git", "Concordantes", "__pycache__", "reportes"}
ALLOWED_NON_ASCII = {
    "04_Registro_Historico/2026-07-01_chatgpt_share_001_transcripcion.md",
}
ALLOWED_NON_ASCII_PREFIXES = (
    "04_Registro_Historico/2026-07-01_descargas_usuario_001/",
)
PASSIVE_HISTORICAL_PREFIXES = (
    "04_Registro_Historico/2026-07-01_descargas_usuario_001/",
)
TRANSFERRED_PSI_PREFIX = "03_Expedientes/PSI-001"
STATUS_PREFIXES = (
    "01_Canon/",
    "02_Documentos/",
    "03_Expedientes/",
    "04_Registro_Historico/",
    "05_Estado_Proyecto/",
)

STATUS_RE = re.compile(r"^Estatus:\s*(.+?)\s*$", re.IGNORECASE)
MD_REF_RE = re.compile(r"`([^`]+\.md)`")

def rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()

def iter_md(root: Path):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for name in files:
            if name.lower().endswith(".md"):
                yield Path(base) / name

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def status_of(text: str) -> str:
    for line in text.splitlines()[:30]:
        match = STATUS_RE.match(line.strip())
        if match:
            return match.group(1).strip().rstrip(".")
    return ""

def add(findings, severity, kind, file, detail):
    findings.append({"severity": severity, "kind": kind, "file": file, "detail": detail})

def is_transferred_psi_ref(ref: str) -> bool:
    normalized = ref.lstrip("./")
    name = Path(normalized).name
    return (
        normalized.startswith(TRANSFERRED_PSI_PREFIX)
        or (name.startswith("PSI-001") and name.endswith(".md"))
    )

def check_file(path: Path, root: Path, existing: set[str]):
    file_rel = rel(path, root)
    text = read(path)
    findings = []
    if file_rel.startswith(PASSIVE_HISTORICAL_PREFIXES):
        return {"file": file_rel, "estatus": status_of(text) or "material_historico_pasivo", "findings": findings}
    if file_rel.startswith(STATUS_PREFIXES) and Path(file_rel).name != "README.md":
        if not status_of(text):
            add(findings, "warning", "estatus_ausente", file_rel, "No hay campo Estatus en las primeras 30 lineas.")
    if any(ord(ch) > 127 for ch in text) and file_rel not in ALLOWED_NON_ASCII and not file_rel.startswith(ALLOWED_NON_ASCII_PREFIXES):
        add(findings, "warning", "no_ascii", file_rel, "Contiene caracteres no ASCII fuera de excepciones historicas.")
    for match in MD_REF_RE.finditer(text):
        ref = match.group(1).replace("\\", "/").strip()
        if ref.startswith("http"):
            continue
        if "/" in ref and ref not in existing:
            if is_transferred_psi_ref(ref):
                add(
                    findings,
                    "warning",
                    "referencia_historica_transferida",
                    file_rel,
                    f"{ref} (PSI-001 transferido; no restaurar copia local)",
                )
                continue
            add(findings, "warning", "referencia_no_materializada", file_rel, ref)
    if not file_rel.startswith("04_Registro_Historico/"):
        for line in text.splitlines():
            low = line.lower()
            if "registro historico" in low and "autoridad" in low:
                is_control_context = any(token in low for token in (
                    "no ",
                    "sin ",
                    "indebido",
                    "prohib",
                    "nunca",
                    "no puede",
                    "bloque",
                    "detectar",
                    "detecta",
                    "sensible",
                    "prueba",
                    "caso",
                    "simul",
                    "valid",
                    "criterio",
                    "fallo",
                    "violacion",
                    "red flag",
                ))
                if not is_control_context:
                    add(findings, "warning", "historial_como_autoridad_posible", file_rel, line.strip())
    return {"file": file_rel, "estatus": status_of(text) or "no_clasificado", "findings": findings}

def result_for(findings):
    severities = {item["severity"] for item in findings}
    if "block" in severities:
        return "bloqueado", "bloquear"
    if "warning" in severities:
        return "advertencia", "continuar_sin_transformar"
    return "ok", "aprobar_lectura"

def render_md(report) -> str:
    lines = [
        "# DO_CHECK_REPORT minimo", "",
        f"report_id: {report['report_id']}",
        "expediente: AUT-001",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false", "",
        "## Resumen", "",
        f"- archivos revisados: {report['summary']['files_checked']}",
        f"- hallazgos: {report['summary']['findings']}",
        "", "## Hallazgos", ""
    ]
    if not report["findings"]:
        lines.append("- Sin hallazgos.")
    else:
        for item in report["findings"]:
            lines.append(f"- [{item['severity']}] {item['file']} - {item['kind']}: {item['detail']}")
    return "\n".join(lines) + "\n"

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="DO-CHECK minimo no mutante.")
    parser.add_argument("targets", nargs="*", help="Archivos o carpetas a revisar.")
    parser.add_argument("--all", action="store_true", help="Revisar todos los Markdown.")
    parser.add_argument("--format", choices=("json", "md"), default="json")
    parser.add_argument("--output", help="Ruta de salida del reporte.")
    args = parser.parse_args(argv)
    root = Path.cwd()
    existing = {rel(path, root) for path in iter_md(root)}
    missing_sources = [source for source in REQUIRED_SOURCES if not (root / source).exists()]
    targets = []
    if args.all:
        targets = list(iter_md(root))
    else:
        if not args.targets:
            parser.error("indica al menos un objetivo o usa --all")
        for raw in args.targets:
            path = (root / raw).resolve()
            if not path.exists():
                raise SystemExit(f"Objetivo no existe: {raw}")
            if root.resolve() not in path.parents and path != root.resolve():
                raise SystemExit(f"Objetivo fuera del repositorio: {raw}")
            if path.is_dir():
                targets.extend(iter_md(path))
            else:
                targets.append(path)
    checked = [check_file(path, root, existing) for path in sorted(set(targets))]
    findings = [finding for item in checked for finding in item["findings"]]
    for source in missing_sources:
        add(findings, "block", "fuente_minima_ausente", source, "Fuente minima requerida no encontrada.")
    resultado, recomendacion = result_for(findings)
    report = {
        "report_id": "DO-CHECK-MIN-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "fuentes_minimas": REQUIRED_SOURCES,
        "summary": {"files_checked": len(checked), "findings": len(findings)},
        "targets": checked,
        "findings": findings,
    }
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
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
    return 0 if resultado in {"ok", "advertencia"} else 2

if __name__ == "__main__":
    raise SystemExit(main())
