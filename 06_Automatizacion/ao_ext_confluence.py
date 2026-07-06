#!/usr/bin/env python3
"""Pruebas externas no reguladas de Confluencia para AO-001.

`AO-EXT-CONF-001` ejecuta fixtures sinteticos no mutantes. No modifica
Documento 04, no cierra Confluencia global ni Equivalencia global, y solo
emite reportes locales de expediente.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-EXT-CONF-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_ext_confluence_cases.json"

SAFE_OUTPUTS = {
    "confluencia_local",
    "equivalencia_bajo_testigo",
    "equivalencia_trivial",
    "divergencia_clasificada",
    "bloqueo_por_testigo",
    "bloqueo_por_deuda",
    "no_comparable",
}


@dataclass(frozen=True)
class RouteProjection:
    route: str
    projection: Any
    warnings: tuple[str, ...]
    blockers: tuple[str, ...]


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    test_id: str
    domain: str
    route_a: str
    route_b: str
    expected: str
    actual: str
    passed: bool
    detail: str
    route_a_blockers: tuple[str, ...]
    route_b_blockers: tuple[str, ...]
    route_a_warnings: tuple[str, ...]
    route_b_warnings: tuple[str, ...]


def coerce_value(value: Any, field: dict[str, Any], row_index: int) -> tuple[Any, str | None]:
    name = str(field["name"])
    required = bool(field.get("required", False))
    if value is None or value == "":
        if required:
            return None, f"row:{row_index}:missing:{name}"
        return None, None

    field_type = field.get("type", "str")
    if field_type == "int":
        try:
            return int(value), None
        except (TypeError, ValueError):
            return value, f"row:{row_index}:invalid_int:{name}"

    if field_type == "enum":
        allowed = set(field.get("allowed", []))
        if value not in allowed:
            return value, f"row:{row_index}:invalid_enum:{name}"
        return str(value), None

    return str(value), None


def rows_from_input(route_input: dict[str, Any]) -> list[dict[str, Any]]:
    fmt = route_input.get("format")
    if fmt == "csv":
        reader = csv.DictReader(io.StringIO(str(route_input.get("content", ""))))
        return [dict(row) for row in reader]
    if fmt == "json_rows":
        return [dict(row) for row in route_input.get("rows", [])]
    raise ValueError(f"Formato tabular no soportado: {fmt}")


def project_table(route: str, route_input: dict[str, Any], schema: dict[str, Any]) -> RouteProjection:
    rows = rows_from_input(route_input)
    fields = list(schema.get("fields", []))
    field_names = {str(field["name"]) for field in fields}
    projection: list[dict[str, Any]] = []
    warnings: list[str] = []
    blockers: list[str] = []

    for index, row in enumerate(rows, start=1):
        extra = sorted(set(row) - field_names)
        for name in extra:
            warnings.append(f"row:{index}:extra_ignored:{name}")

        projected: dict[str, Any] = {}
        for field in fields:
            name = str(field["name"])
            coerced, blocker = coerce_value(row.get(name), field, index)
            if blocker:
                blockers.append(blocker)
            projected[name] = coerced
        projection.append(projected)

    projection.sort(key=lambda item: str(item.get("id", "")))
    return RouteProjection(route, projection, tuple(sorted(warnings)), tuple(sorted(blockers)))


def normalize_package(fmt: str, route_input: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if fmt == "package_manifest":
        return dict(route_input.get("package", {})), [dict(dep) for dep in route_input.get("dependencies", [])]
    if fmt == "dependency_report":
        return dict(route_input.get("root", {})), [dict(dep) for dep in route_input.get("resolved", [])]
    raise ValueError(f"Formato de paquete no soportado: {fmt}")


def normalize_package_item(item: dict[str, Any], label: str, blockers: list[str]) -> dict[str, str | None]:
    normalized: dict[str, str | None] = {}
    for field in ("name", "version", "license"):
        value = item.get(field)
        if value is None or value == "":
            blockers.append(f"{label}:missing:{field}")
            normalized[field] = None
        else:
            normalized[field] = str(value)
    return normalized


def project_package(route: str, route_input: dict[str, Any]) -> RouteProjection:
    root, dependencies = normalize_package(str(route_input.get("format")), route_input)
    blockers: list[str] = []
    normalized_root = normalize_package_item(root, "root", blockers)
    normalized_deps = [
        normalize_package_item(dep, f"dep:{dep.get('name', index)}", blockers)
        for index, dep in enumerate(dependencies, start=1)
    ]
    normalized_deps.sort(key=lambda item: str(item.get("name", "")))
    projection = {"root": normalized_root, "dependencies": normalized_deps}
    return RouteProjection(route, projection, tuple(), tuple(sorted(blockers)))


def project_route(case: dict[str, Any], route_name: str, input_name: str) -> RouteProjection:
    route_input = dict(case[input_name])
    fmt = route_input.get("format")
    if fmt in {"csv", "json_rows"}:
        return project_table(route_name, route_input, dict(case.get("schema", {})))
    if fmt in {"package_manifest", "dependency_report"}:
        return project_package(route_name, route_input)
    raise ValueError(f"Formato no soportado: {fmt}")


def classify(left: RouteProjection, right: RouteProjection) -> str:
    if left.blockers or right.blockers:
        if left.blockers == right.blockers:
            return "bloqueo_por_testigo"
        return "bloqueo_por_deuda"
    if left.projection == right.projection:
        if left.warnings or right.warnings:
            return "equivalencia_bajo_testigo"
        return "confluencia_local"
    return "divergencia_clasificada"


def evaluate_case(case: dict[str, Any]) -> CaseResult:
    left = project_route(case, str(case["route_a"]), "route_a_input")
    right = project_route(case, str(case["route_b"]), "route_b_input")
    actual = classify(left, right)
    expected = str(case["expected"])
    if actual not in SAFE_OUTPUTS:
        actual = "no_comparable"
    passed = actual == expected
    detail = f"{case['route_a']} vs {case['route_b']} => {actual}"
    return CaseResult(
        case_id=str(case["case_id"]),
        test_id=str(case["test_id"]),
        domain=str(case["domain"]),
        route_a=str(case["route_a"]),
        route_b=str(case["route_b"]),
        expected=expected,
        actual=actual,
        passed=passed,
        detail=detail,
        route_a_blockers=left.blockers,
        route_b_blockers=right.blockers,
        route_a_warnings=left.warnings,
        route_b_warnings=right.warnings,
    )


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize_by_test(results: list[CaseResult]) -> dict[str, dict[str, int]]:
    summary: dict[str, dict[str, int]] = {}
    for result in results:
        entry = summary.setdefault(result.test_id, {"cases": 0, "passed": 0, "failed": 0})
        entry["cases"] += 1
        if result.passed:
            entry["passed"] += 1
        else:
            entry["failed"] += 1
    return summary


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    tests_executed = sorted({result.test_id for result in results})
    resultado = "ok" if not failures else "bloqueado"
    recomendacion = "mantener_deudas_globales_abiertas" if not failures else "revisar_pruebas_externas"
    return {
        "report_id": "AO-EXT-CONF-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-EXT-CONF-SYN-001"),
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "tests_executed": tests_executed,
        "summary": {
            "cases": len(results),
            "passed": len(results) - len(failures),
            "failed": len(failures),
            "findings": len(failures),
            "by_test": summarize_by_test(results),
        },
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "crea_nivel_c": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
            "promueve_r4_gamma": False,
            "madura_tcs_canonico": False,
            "autoriza_transformacion": False,
        },
        "debt_guard": {
            "confluencia_global_abierta": True,
            "equivalencia_global_abierta": True,
            "formalizacion_doc04_abierta": True,
            "exportacion_r4_gamma_abierta": True,
            "maduracion_tcs_abierta": True,
        },
        "results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_EXT_CONFLUENCE_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
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
        "## Guardas de alcance",
        "",
        "- No modifica Documento 04.",
        "- No modifica Canon ni Nivel C.",
        "- No cierra Confluencia global.",
        "- No cierra Equivalencia global.",
        "- No promueve ni exporta R4/Gamma.",
        "- No canoniza ni cierra `TCS-001`.",
        "- No autoriza transformaciones materiales.",
        "",
        "## Deudas conservadas abiertas",
        "",
    ]
    for key, value in report["debt_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")

    lines.extend(["", "## Resultados", ""])
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}` (`{result['test_id']}`): {result['detail']}")
        if result["route_a_blockers"] or result["route_b_blockers"]:
            lines.append(f"  - blockers_a: `{', '.join(result['route_a_blockers'])}`")
            lines.append(f"  - blockers_b: `{', '.join(result['route_b_blockers'])}`")
        if result["route_a_warnings"] or result["route_b_warnings"]:
            lines.append(f"  - warnings_a: `{', '.join(result['route_a_warnings'])}`")
            lines.append(f"  - warnings_b: `{', '.join(result['route_b_warnings'])}`")

    if not report["findings"]:
        lines.extend(["", "## Hallazgos", "", "- Sin hallazgos bloqueantes."])
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Salida fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Pruebas externas no reguladas de Confluencia para AO-001.")
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
