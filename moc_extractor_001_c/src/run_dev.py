#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from moc_extractor_001_c import (
    EXPECTED_BANK_SHA256,
    ContractError,
    build_report,
    canonicalize_candidate_spans,
    canonical_json,
    load_bank,
    project_model_input,
    report_markdown,
    sha256_file,
    strict_json_load,
    write_json,
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _issue_case_ids(report: Mapping[str, Any], all_case_ids: Sequence[str]) -> list[str]:
    affected = {
        issue["case_id"]
        for issue in report.get("issues", [])
        if issue.get("case_id") not in {"BATCH", None}
    }
    selected = [case_id for case_id in all_case_ids if case_id in affected]
    return selected or list(all_case_ids)


def _retry_feedback(report: Mapping[str, Any]) -> str:
    lines = [
        "Esta es una segunda extracción independiente sobre casos DEV visibles.",
        "Corrige los tipos de fallo indicados sin copiar valores esperados ni ampliar inferencias.",
    ]
    issues = report.get("issues", [])
    if not issues:
        lines.append(
            "El primer intento no produjo hallazgos; repite el autocontrol completo de forma independiente."
        )
        return "\n".join(lines)
    seen: set[tuple[str, str, str]] = set()
    for issue in issues:
        case_id = issue.get("case_id")
        if case_id == "BATCH":
            continue
        key = (case_id, issue.get("category", ""), issue.get("path", ""))
        if key in seen:
            continue
        seen.add(key)
        lines.append(
            f"- {case_id}: {issue.get('category')} en {issue.get('path')}; "
            f"{issue.get('message')}"
        )
    return "\n".join(lines)


def _prompt_text(base_prompt: str, model_input: Mapping[str, Any], retry: str | None) -> str:
    sections = [base_prompt]
    if retry:
        sections.extend(["## Instrucción de reintento", retry])
    sections.extend(
        [
            "## Entrada JSON",
            json.dumps(model_input, ensure_ascii=False, indent=2),
        ]
    )
    return "\n\n".join(sections) + "\n"


def _run_codex_attempt(
    attempt_dir: Path,
    codex_exe: Path,
    schema_path: Path,
    project_root: Path,
    prompt: str,
    model: str | None,
) -> dict[str, Any]:
    attempt_dir.mkdir(parents=True, exist_ok=False)
    prompt_path = attempt_dir / "prompt.txt"
    output_path = attempt_dir / "output.json"
    trace_path = attempt_dir / "trace.jsonl"
    stderr_path = attempt_dir / "stderr.txt"
    prompt_path.write_text(prompt, encoding="utf-8", newline="\n")

    command = [
        str(codex_exe),
        "exec",
        "--ephemeral",
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--output-schema",
        str(schema_path),
        "--json",
        "-o",
        str(output_path),
    ]
    if model:
        command.extend(["--model", model])
    command.append("-")

    started_at = _utc_now()
    completed = subprocess.run(
        command,
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="strict",
        cwd=project_root,
        capture_output=True,
        check=False,
    )
    finished_at = _utc_now()
    trace_path.write_text(completed.stdout, encoding="utf-8", newline="\n")
    stderr_path.write_text(completed.stderr, encoding="utf-8", newline="\n")
    metadata = {
        "started_at": started_at,
        "finished_at": finished_at,
        "command": command,
        "return_code": completed.returncode,
        "prompt_sha256": sha256_file(prompt_path),
        "trace_sha256": sha256_file(trace_path),
        "stderr_sha256": sha256_file(stderr_path),
        "output_exists": output_path.is_file(),
        "output_sha256": sha256_file(output_path) if output_path.is_file() else None,
    }
    write_json(attempt_dir / "execution.json", metadata)
    return metadata


def _validate_attempt(
    attempt_dir: Path,
    bank: Mapping[str, Any],
    bank_path: Path,
    selected_case_ids: Sequence[str],
) -> tuple[dict[str, Any] | None, dict[str, Any] | None, str | None]:
    output_path = attempt_dir / "output.json"
    if not output_path.is_file():
        return None, None, "Codex did not produce output.json"
    try:
        raw_candidate = strict_json_load(output_path)
    except ContractError as exc:
        return None, None, str(exc)
    candidate, span_notes = canonicalize_candidate_spans(raw_candidate, bank)
    parsed_output_path = attempt_dir / "parsed_output.json"
    write_json(parsed_output_path, candidate)
    write_json(attempt_dir / "span_canonicalization.json", span_notes)
    report = build_report(
        candidate,
        bank,
        bank_path,
        parsed_output_path,
        selected_case_ids,
    )
    write_json(attempt_dir / "validation.json", report)
    (attempt_dir / "validation.md").write_text(
        report_markdown(report), encoding="utf-8", newline="\n"
    )
    return candidate, report, None


def _case_score(report: Mapping[str, Any], case_id: str) -> tuple[int, int]:
    structural = sum(
        issue["phase"] == "structural" and issue["case_id"] in {case_id, "BATCH"}
        for issue in report.get("issues", [])
    )
    semantic = sum(
        issue["phase"] == "semantic" and issue["case_id"] == case_id
        for issue in report.get("issues", [])
    )
    return structural, semantic


def _merge_candidates(
    first_candidate: Mapping[str, Any] | None,
    first_report: Mapping[str, Any] | None,
    retry_candidate: Mapping[str, Any] | None,
    retry_report: Mapping[str, Any] | None,
    all_case_ids: Sequence[str],
) -> tuple[dict[str, Any], dict[str, str]]:
    first_cases = {
        case["case_id"]: case
        for case in (first_candidate or {}).get("cases", [])
        if isinstance(case, dict) and isinstance(case.get("case_id"), str)
    }
    retry_cases = {
        case["case_id"]: case
        for case in (retry_candidate or {}).get("cases", [])
        if isinstance(case, dict) and isinstance(case.get("case_id"), str)
    }
    decisions: dict[str, str] = {}
    merged_cases: list[Mapping[str, Any]] = []
    for case_id in all_case_ids:
        first = first_cases.get(case_id)
        retry = retry_cases.get(case_id)
        if first is None and retry is None:
            continue
        if first is None:
            selected = retry
            decisions[case_id] = "retry_missing_in_first"
        elif retry is None or retry_report is None:
            selected = first
            decisions[case_id] = "first_no_retry_case"
        elif first_report is None:
            selected = retry
            decisions[case_id] = "retry_first_unparseable"
        else:
            first_score = _case_score(first_report, case_id)
            retry_score = _case_score(retry_report, case_id)
            if retry_score <= first_score:
                selected = retry
                decisions[case_id] = f"retry_score_{retry_score}_vs_{first_score}"
            else:
                selected = first
                decisions[case_id] = f"first_score_{first_score}_vs_{retry_score}"
        merged_cases.append(selected)
    return {
        "schema_version": "1.0.0",
        "extractor_id": "MOC-EXTRACTOR-001-C",
        "cases": merged_cases,
    }, decisions


def run(args: argparse.Namespace) -> int:
    bank_path = Path(args.bank).resolve()
    codex_exe = Path(args.codex_exe).resolve()
    out_dir = Path(args.out_dir).resolve()
    source_dir = Path(__file__).resolve().parent
    package_dir = source_dir.parent
    project_root = package_dir.parent
    schema_path = package_dir / "schema" / "moc_extractor_001_c.schema.json"
    prompt_path = package_dir / "prompts" / "MOC-EXTRACTOR-001-C_PROMPT.md"

    if out_dir.exists():
        raise ContractError(f"refusing to overwrite existing run directory: {out_dir}")
    if not codex_exe.is_file():
        raise ContractError(f"Codex executable not found: {codex_exe}")
    version_check = subprocess.run(
        [str(codex_exe), "--version"],
        text=True,
        encoding="utf-8",
        errors="strict",
        capture_output=True,
        check=False,
    )
    if version_check.returncode != 0:
        raise ContractError(
            f"unable to resolve Codex CLI version: {version_check.stderr.strip()}"
        )
    codex_cli_version = version_check.stdout.strip()
    bank = load_bank(bank_path, args.expected_sha256)
    all_case_ids = [case["case_id"] for case in bank["dev_cases"]]
    base_prompt = prompt_path.read_text(encoding="utf-8")
    out_dir.mkdir(parents=True, exist_ok=False)

    run_input = project_model_input(bank)
    write_json(out_dir / "projected_input.json", run_input)
    run_started = _utc_now()

    attempt_1_dir = out_dir / "attempt-01"
    first_prompt = _prompt_text(base_prompt, run_input, retry=None)
    first_execution = _run_codex_attempt(
        attempt_1_dir,
        codex_exe,
        schema_path,
        project_root,
        first_prompt,
        args.model,
    )
    first_candidate, first_report, first_error = _validate_attempt(
        attempt_1_dir, bank, bank_path, all_case_ids
    )

    if first_report is not None:
        retry_case_ids = _issue_case_ids(first_report, all_case_ids)
        retry_feedback = _retry_feedback(first_report)
    else:
        retry_case_ids = list(all_case_ids)
        retry_feedback = (
            "El primer intento no produjo JSON validable. Repite todos los casos y aplica "
            "estrictamente el esquema, sin texto fuera del JSON."
        )
    retry_input = project_model_input(bank, retry_case_ids)
    write_json(out_dir / "retry_projected_input.json", retry_input)
    attempt_2_dir = out_dir / "attempt-02-retry"
    retry_prompt = _prompt_text(base_prompt, retry_input, retry_feedback)
    retry_execution = _run_codex_attempt(
        attempt_2_dir,
        codex_exe,
        schema_path,
        project_root,
        retry_prompt,
        args.model,
    )
    retry_candidate, retry_report, retry_error = _validate_attempt(
        attempt_2_dir, bank, bank_path, retry_case_ids
    )

    merged, decisions = _merge_candidates(
        first_candidate,
        first_report,
        retry_candidate,
        retry_report,
        all_case_ids,
    )
    final_dir = out_dir / "final"
    final_dir.mkdir()
    final_output = final_dir / "output.json"
    write_json(final_output, merged)
    final_report = build_report(merged, bank, bank_path, final_output)
    write_json(final_dir / "validation.json", final_report)
    (final_dir / "validation.md").write_text(
        report_markdown(final_report), encoding="utf-8", newline="\n"
    )
    write_json(final_dir / "selection.json", decisions)

    manifest = {
        "run_id": out_dir.name,
        "started_at": run_started,
        "finished_at": _utc_now(),
        "bank_path": str(bank_path),
        "bank_sha256": sha256_file(bank_path),
        "prompt_sha256": sha256_file(prompt_path),
        "schema_sha256": sha256_file(schema_path),
        "model": args.model,
        "codex_cli_version": codex_cli_version,
        "attempt_01": {
            **first_execution,
            "validation_error": first_error,
            "validation_summary": first_report.get("summary") if first_report else None,
        },
        "attempt_02_retry": {
            **retry_execution,
            "case_ids": retry_case_ids,
            "validation_error": retry_error,
            "validation_summary": retry_report.get("summary") if retry_report else None,
        },
        "final": {
            "output_sha256": sha256_file(final_output),
            "validation_sha256": sha256_file(final_dir / "validation.json"),
            "summary": final_report["summary"],
            "selection": decisions,
        },
    }
    write_json(out_dir / "run_manifest.json", manifest)
    print(json.dumps(final_report["summary"], ensure_ascii=False, indent=2))

    execution_ok = first_execution["return_code"] == 0 and retry_execution["return_code"] == 0
    structural_ok = final_report["summary"]["structural_pass"]
    complete_case_set = len(merged["cases"]) == len(all_case_ids)
    return 0 if execution_ok and structural_ok and complete_case_set else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run MOC-EXTRACTOR-001-C on visible DEV")
    parser.add_argument("--bank", required=True)
    parser.add_argument("--codex-exe", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--expected-sha256", default=EXPECTED_BANK_SHA256)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return run(args)
    except ContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
