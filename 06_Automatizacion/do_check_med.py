#!/usr/bin/env python3
"""Verificador medio no mutante del Laboratorio Concordante."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

REQUIRED_SOURCES = [
    "CURRENT_STATE.md",
    "05_Estado_Proyecto/ESTADO_ACTUAL.md",
    "01_Canon/M-000_Reglas_Fundamentales.md",
    "01_Canon/M-001_Auditoria_Arquitectonica.md",
    "02_Documentos/C-001_Especificacion_Tecnica_Auditor.md",
    "03_Expedientes/DO-001_DO-CHECK-001.md",
    "03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md",
    "03_Expedientes/REC-001_Mapa_Reconciliacion_Canon_Baselines.md",
]

EXCLUDED_SCAN_DIRS = {".git", "Concordantes", "__pycache__", "reportes"}
EXCLUDED_INDEX_DIRS = {".git", "Concordantes", "__pycache__"}
PASSIVE_HISTORICAL_PREFIXES = ("04_Registro_Historico/2026-07-01_descargas_usuario_001/",)
ALLOWED_NON_ASCII = {"04_Registro_Historico/2026-07-01_chatgpt_share_001_transcripcion.md"}
ALLOWED_NON_ASCII_PREFIXES = PASSIVE_HISTORICAL_PREFIXES
STATUS_PREFIXES = (
    "01_Canon/",
    "02_Documentos/",
    "03_Expedientes/",
    "04_Registro_Historico/",
    "05_Estado_Proyecto/",
)
ROOT_STATE_FILES = {"CURRENT_STATE.md", "README.md", "HANDOFF.md", "HANDOFF_PACKAGE.md", "CHANGELOG.md"}
STATUS_RE = re.compile(r"^Estatus:\s*(.+?)\s*$", re.IGNORECASE)
BT = chr(96)
BACKTICK_REF_RE = re.compile(re.escape(BT) + "([^" + re.escape(BT) + "\\n]+)" + re.escape(BT))
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SENSITIVE_ACTION_RE = re.compile(
    r"\b(modifica|modificar|actualiza|actualizar|promueve|promover|"
    r"cierra|cerrar|reabre|reabrir|autoriza|autorizar)\b.*"
    r"\b(Canon|documento oficial|documentos oficiales|expediente cerrado|"
    r"expedientes cerrados|hipotesis|hipotesis externa)\b",
    re.IGNORECASE,
)
NEGATION_TOKENS = (
    "no ",
    "sin ",
    "no cubre",
    "no autoriza",
    "no modifica",
    "no cierra",
    "no reabre",
    "no promueve",
    "prohibe",
    "prohibida",
    "prohibido",
    "fuera de alcance",
)

CONTROL_CONTEXT_TOKENS = (
    "detectar",
    "deteccion",
    "uso indebido",
    "violacion",
    "bloquea",
    "bloquear",
    "bloqueado",
    "prueba",
    "probar",
    "simulacion",
    "simulaciones",
    "caso",
    "casos",
    "validado",
    "validada",
    "validar",
    "validacion",
    "criterio",
    "fallo",
    "red flag",
    "cumplido",
    "objeto evaluado",
    "control negativo",
    "fuera de autoridad",
    "aud-t",
    "aud-sim",
    "val-",
    "med-historial",
    "evidencia:",
    "importacion de",
    "solo se reabre",
    "se reabre por decision",
    "decision posterior",
)
CONTROL_SECTION_TOKENS = (
    "no cubre",
    "no puede",
    "que no prueba",
    "fuera de alcance",
    "restricciones",
    "prohibiciones",
    "antipatrones",
    "riesgos",
    "casos",
    "validaciones",
    "simulaciones",
    "control negativo",
    "bloqueo",
    "bloqueado",
    "bloqueada",
    "bloqueados",
    "bloqueadas",
    "acciones bloqueadas",
    "controles",
    "hallazgos",
    "deudas",
)
TRANSFERRED_PSI_PREFIX = "03_Expedientes/PSI-001"
REPORT_REQUIRED_TERMS = (
    "report_id",
    "expediente",
    "resultado",
    "tipo",
    "descripcion",
    "evidencia",
    "estatus_afirmacion",
    "dependencias",
    "deudas_generadas",
    "transformacion_permitida",
)


def rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def iter_files(root: Path, excluded_dirs: set[str]):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for name in files:
            yield Path(base) / name


def iter_md(root: Path, excluded_dirs: set[str] = EXCLUDED_SCAN_DIRS):
    for path in iter_files(root, excluded_dirs):
        if path.suffix.lower() == ".md":
            yield path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def status_of(text: str) -> str:
    for line in text.splitlines()[:30]:
        match = STATUS_RE.match(line.strip())
        if match:
            return match.group(1).strip().rstrip(".")
    return ""


def add(findings, severity, check_id, kind, file, detail, evidence=""):
    findings.append(
        {
            "severity": severity,
            "check_id": check_id,
            "kind": kind,
            "file": file,
            "detail": detail,
            "evidence": evidence,
        }
    )


def clean_ref(raw: str) -> str:
    ref = raw.strip().replace("\\", "/")
    if ref.startswith("<") and ref.endswith(">"):
        ref = ref[1:-1].strip()
    if "#" in ref:
        ref = ref.split("#", 1)[0]
    return ref.strip()


def looks_like_local_path(ref: str) -> bool:
    if not ref or ref.startswith(("http://", "https://", "mailto:")):
        return False
    if ref.startswith("#"):
        return False
    suffix = Path(ref).suffix.lower()
    return "/" in ref or suffix in {".md", ".py", ".json", ".txt", ".docx", ".pdf", ".zip"}


def surface_of(file_rel: str) -> str:
    if file_rel.startswith("01_Canon/"):
        return "canon"
    if file_rel.startswith("02_Documentos/"):
        return "documento_oficial"
    if file_rel.startswith("03_Expedientes/"):
        return "expediente"
    if file_rel.startswith("04_Registro_Historico/"):
        return "registro_historico"
    if file_rel.startswith("05_Estado_Proyecto/") or file_rel in ROOT_STATE_FILES:
        return "estado_operativo"
    if file_rel.startswith("06_Automatizacion/"):
        return "automatizacion"
    return "otro"


def parse_bullet_section(text: str, heading: str) -> set[str]:
    inside = False
    values: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == heading:
            inside = True
            continue
        if inside and stripped.startswith("## "):
            break
        if inside and stripped.startswith("- "):
            item = stripped[2:].strip().split(" ", 1)[0].strip(BT + ".,:")
            if item:
                values.add(item)
    return values


def build_project_context(root: Path) -> dict:
    estado_path = root / "05_Estado_Proyecto/ESTADO_ACTUAL.md"
    current_path = root / "CURRENT_STATE.md"
    estado_text = read(estado_path) if estado_path.exists() else ""
    current_text = read(current_path) if current_path.exists() else ""
    return {
        "closed_expedientes": parse_bullet_section(estado_text, "## Expedientes cerrados"),
        "open_expedientes": parse_bullet_section(estado_text, "## Expedientes abiertos"),
        "frozen_expedientes": parse_bullet_section(estado_text, "## Expedientes congelados"),
        "estado_text": estado_text,
        "current_text": current_text,
    }


def references_in(text: str) -> list[str]:
    refs: list[str] = []
    refs.extend(match.group(1) for match in BACKTICK_REF_RE.finditer(text))
    refs.extend(match.group(1) for match in MARKDOWN_LINK_RE.finditer(text))
    return [clean_ref(ref) for ref in refs if looks_like_local_path(clean_ref(ref))]


def is_control_section(heading: str) -> bool:
    low = heading.lower()
    return any(token in low for token in CONTROL_SECTION_TOKENS)


def iter_lines_with_heading(text: str):
    heading = ""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
        yield line, heading


def has_negation_context(line: str, heading: str = "") -> bool:
    low = line.lower()
    return (
        is_control_section(heading)
        or low.strip().startswith("- reabrir ")
        or any(token in low for token in NEGATION_TOKENS)
        or any(token in low for token in CONTROL_CONTEXT_TOKENS)
    )


def is_transferred_psi_ref(ref: str) -> bool:
    normalized = ref.lstrip("./")
    name = Path(normalized).name
    return (
        normalized.startswith(TRANSFERRED_PSI_PREFIX)
        or (name.startswith("PSI-001") and name.endswith(".md"))
    )


def check_historical_authority(text: str, file_rel: str, findings):
    if file_rel.startswith("04_Registro_Historico/"):
        return
    for line, heading in iter_lines_with_heading(text):
        low = line.lower()
        mentions_history = (
            "registro historico" in low
            or "04_registro_historico" in low
            or re.search(r"\bsrc-\d{3}\b", low) is not None
        )
        authority_language = any(
            token in low
            for token in (
                "autoridad vigente",
                "autoridad directa",
                "como autoridad",
                "fuente normativa",
                "fundamento positivo",
            )
        )
        if mentions_history and authority_language and not has_negation_context(line, heading):
            severity = "block" if surface_of(file_rel) in {"canon", "documento_oficial", "estado_operativo"} else "warning"
            kind = "historial_como_autoridad" if severity == "block" else "historial_como_autoridad_controlada"
            add(
                findings,
                severity,
                "MED-HISTORIAL",
                kind,
                file_rel,
                "Posible uso del Registro Historico o de SRC como autoridad vigente.",
                line.strip(),
            )


def check_sensitive_actions(text: str, file_rel: str, findings):
    for line, heading in iter_lines_with_heading(text):
        if SENSITIVE_ACTION_RE.search(line) and not has_negation_context(line, heading):
            add(
                findings,
                "warning",
                "MED-NIVELES",
                "accion_de_nivel_sensible",
                file_rel,
                "La linea parece tocar Canon, documento oficial, expediente cerrado o hipotesis.",
                line.strip(),
            )


def check_report_contract(text: str, file_rel: str, findings):
    if "_REPORT = {" not in text and "DO_CHECK_REPORT = {" not in text:
        return
    missing = [term for term in REPORT_REQUIRED_TERMS if term not in text]
    if missing:
        add(
            findings,
            "warning",
            "MED-REPORTES",
            "reporte_normalizado_incompleto",
            file_rel,
            "Faltan campos esperados en una definicion de reporte: " + ", ".join(missing),
        )


def check_closed_exp_reopen(text: str, file_rel: str, findings, closed_expedientes: set[str]):
    if not closed_expedientes:
        return
    for line, heading in iter_lines_with_heading(text):
        low = line.lower()
        if not any(token in low for token in ("reabrir", "reabre", "modificar")):
            continue
        if has_negation_context(line, heading):
            continue
        affected = sorted(exp for exp in closed_expedientes if exp.lower() in low)
        if affected:
            if file_rel == "CHANGELOG.md":
                severity = "warning"
            else:
                severity = "block" if surface_of(file_rel) in {"canon", "documento_oficial", "estado_operativo"} or "_Decision" in Path(file_rel).name else "warning"
            add(
                findings,
                severity,
                "MED-CERRADOS",
                "expediente_cerrado_afectado",
                file_rel,
                "La linea parece afectar expediente cerrado: " + ", ".join(affected),
                line.strip(),
            )


def check_file(path: Path, root: Path, existing: set[str], context: dict) -> dict:
    file_rel = rel(path, root)
    text = read(path)
    findings = []
    surface = surface_of(file_rel)

    if file_rel.startswith(PASSIVE_HISTORICAL_PREFIXES):
        return {
            "file": file_rel,
            "surface": surface,
            "estatus": status_of(text) or "material_historico_pasivo",
            "findings": findings,
        }

    if file_rel.startswith(STATUS_PREFIXES) and Path(file_rel).name != "README.md":
        if not status_of(text):
            add(findings, "warning", "MED-ESTATUS", "estatus_ausente", file_rel, "No hay campo Estatus en las primeras 30 lineas.")

    if any(ord(ch) > 127 for ch in text) and file_rel not in ALLOWED_NON_ASCII and not file_rel.startswith(ALLOWED_NON_ASCII_PREFIXES):
        add(findings, "warning", "MED-ASCII", "no_ascii", file_rel, "Contiene caracteres no ASCII fuera de excepciones historicas.")

    existing_names = {Path(item).name for item in existing}
    for ref in references_in(text):
        if re.match(r"^[A-Za-z]:/", ref):
            continue
        normalized = ref.lstrip("./")
        exact_exists = normalized in existing or (root / normalized).exists()
        basename_exists = "/" not in normalized and Path(normalized).name in existing_names
        if normalized and not exact_exists and not basename_exists:
            if is_transferred_psi_ref(normalized):
                add(
                    findings,
                    "warning",
                    "MED-REFERENCIAS",
                    "referencia_historica_transferida",
                    file_rel,
                    "Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local.",
                    normalized,
                )
                continue
            add(findings, "warning", "MED-REFERENCIAS", "referencia_no_materializada", file_rel, normalized)

    check_historical_authority(text, file_rel, findings)
    check_sensitive_actions(text, file_rel, findings)
    check_report_contract(text, file_rel, findings)
    check_closed_exp_reopen(text, file_rel, findings, context["closed_expedientes"])

    return {
        "file": file_rel,
        "surface": surface,
        "estatus": status_of(text) or "no_clasificado",
        "findings": findings,
    }


def repository_checks(root: Path, context: dict, existing: set[str]) -> list[dict]:
    findings: list[dict] = []
    for source in REQUIRED_SOURCES:
        if source not in existing:
            add(findings, "block", "MED-FUENTES", "fuente_minima_ausente", source, "Fuente minima requerida no encontrada.")
    if "AUT-001" not in context["open_expedientes"] and "AUT-001" not in context["closed_expedientes"]:
        add(findings, "warning", "MED-ESTADO", "aut_001_sin_estado_operativo", "05_Estado_Proyecto/ESTADO_ACTUAL.md", "AUT-001 no aparece como expediente abierto ni cerrado.")
    if "REC-001" not in context["closed_expedientes"]:
        add(findings, "warning", "MED-ESTADO", "rec_001_no_figura_cerrado", "05_Estado_Proyecto/ESTADO_ACTUAL.md", "REC-001 no aparece como expediente cerrado.")
    if "REC-DEUDA-003" not in context["estado_text"] and "REC-DEUDA-003" not in context["current_text"]:
        add(findings, "info", "MED-DEUDAS", "deuda_aau_no_visible_en_estado", "05_Estado_Proyecto/ESTADO_ACTUAL.md", "La deuda del AAU historico no aparece visible en el estado operativo.")
    return findings


def result_for(findings: list[dict]) -> tuple[str, str, str]:
    severities = {item["severity"] for item in findings}
    if "block" in severities:
        return "bloqueado", "bloquear", "INCONSISTENTE"
    if "warning" in severities:
        return "advertencia", "continuar_sin_transformar", "SUSPENDIDO"
    return "ok", "aprobar_lectura", "APROBADO"


def render_md(report: dict) -> str:
    lines = [
        "# DO_CHECK_REPORT medio",
        "",
        f"report_id: {report['report_id']}",
        "expediente: AUT-001",
        "algoritmo: DO-CHECK-MED-001",
        f"resultado: {report['resultado']}",
        f"estado_aau_local: {report['estado_aau_local']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "",
        "## Resumen",
        "",
        f"- archivos revisados: {report['summary']['files_checked']}",
        f"- hallazgos: {report['summary']['findings']}",
        f"- bloques: {report['summary']['by_severity'].get('block', 0)}",
        f"- advertencias: {report['summary']['by_severity'].get('warning', 0)}",
        f"- informativos: {report['summary']['by_severity'].get('info', 0)}",
        "",
        "## Puente AAU",
        "",
        "- Presv: controles medios preservables.",
        "- Activas(G): estado operativo, permisos, expedientes cerrados y superficies sensibles.",
        "- Inv(G): controles sin ruptura.",
        "- Break(Fk): hallazgos emitidos por este reporte.",
        "",
        "## Hallazgos",
        "",
    ]
    if not report["findings"]:
        lines.append("- Sin hallazgos.")
    else:
        for item in report["findings"]:
            line = f"- [{item['severity']}] {item['check_id']} {item['file']} - {item['kind']}: {item['detail']}"
            if item.get("evidence"):
                line += f" | evidencia: {item['evidence']}"
            lines.append(line)
    return "\n".join(lines) + "\n"


def collect_targets(root: Path, args) -> list[Path]:
    if args.all:
        return list(iter_md(root))
    if not args.targets:
        raise SystemExit("indica al menos un objetivo o usa --all")
    targets: list[Path] = []
    for raw in args.targets:
        path = (root / raw).resolve()
        if not path.exists():
            raise SystemExit(f"Objetivo no existe: {raw}")
        if root.resolve() not in path.parents and path != root.resolve():
            raise SystemExit(f"Objetivo fuera del repositorio: {raw}")
        if path.is_dir():
            targets.extend(iter_md(path))
        elif path.suffix.lower() == ".md":
            targets.append(path)
    return sorted(set(targets))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="DO-CHECK medio no mutante.")
    parser.add_argument("targets", nargs="*", help="Archivos o carpetas Markdown a revisar.")
    parser.add_argument("--all", action="store_true", help="Revisar todos los Markdown no generados.")
    parser.add_argument("--format", choices=("json", "md"), default="json")
    parser.add_argument("--output", help="Ruta de salida del reporte.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    existing = {rel(path, root) for path in iter_files(root, EXCLUDED_INDEX_DIRS)}
    context = build_project_context(root)
    targets = collect_targets(root, args)

    checked = [check_file(path, root, existing, context) for path in targets]
    findings = [finding for item in checked for finding in item["findings"]]
    findings.extend(repository_checks(root, context, existing))

    resultado, recomendacion, estado_aau_local = result_for(findings)
    by_severity = dict(Counter(item["severity"] for item in findings))
    by_check = dict(Counter(item["check_id"] for item in findings))

    report = {
        "report_id": "DO-CHECK-MED-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-CHECK-MED-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "estado_aau_local": estado_aau_local,
        "transformacion_permitida": False,
        "fuentes_minimas": REQUIRED_SOURCES,
        "aau_bridge": {
            "fuente_historica": "SRC-013",
            "presv": [
                "MED-FUENTES",
                "MED-ESTATUS",
                "MED-REFERENCIAS",
                "MED-HISTORIAL",
                "MED-NIVELES",
                "MED-CERRADOS",
                "MED-REPORTES",
                "MED-ESTADO",
                "MED-ASCII",
            ],
            "estados": {
                "APROBADO": "sin hallazgos bloqueantes ni advertencias",
                "SUSPENDIDO": "hallazgos no bloqueantes; continuar sin transformar",
                "INCONSISTENTE": "hallazgo bloqueante; bloquear",
                "NO AUDITABLE": "fuentes minimas ausentes o entrada insuficiente",
            },
        },
        "summary": {
            "files_checked": len(checked),
            "findings": len(findings),
            "by_severity": by_severity,
            "by_check": by_check,
        },
        "targets": checked,
        "findings": findings,
    }

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
    return 0 if resultado in {"ok", "advertencia"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
