from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any, Mapping

from pydantic import ValidationError

from .models import (
    ContractViolation,
    FrictionType,
    ValidatedNarrativeExtractionVNext,
    ViolationCode,
)


ATOMICITY_PATTERN_VERSION = "2026-08-06.h2.1"
MAX_ATOMICITY_PATTERNS = 64
MAX_PATTERN_LENGTH = 256
MAX_ATOMICITY_CATALOG_BYTES = 128_000


class AtomicityCatalogError(ValueError):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


def _catalog_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "catalogs"
        / "MOC-EXTRACTOR-001-H2-SEMANTIC-ATOMICITY-PATTERNS.candidate.json"
    )


def _load_patterns() -> tuple[Mapping[str, Any], ...]:
    raw = _catalog_path().read_bytes()
    if len(raw) > MAX_ATOMICITY_CATALOG_BYTES:
        raise AtomicityCatalogError("ATOMICITY_CATALOG_BYTES_EXCEEDED")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AtomicityCatalogError("ATOMICITY_CATALOG_INVALID") from exc
    if not isinstance(data, dict) or data.get("version") != ATOMICITY_PATTERN_VERSION:
        raise AtomicityCatalogError("ATOMICITY_CATALOG_IDENTITY_INVALID")
    patterns = data.get("patterns")
    if not isinstance(patterns, list) or len(patterns) > MAX_ATOMICITY_PATTERNS:
        raise AtomicityCatalogError("ATOMICITY_PATTERN_LIMIT_EXCEEDED")
    frozen: list[Mapping[str, Any]] = []
    for pattern in copy.deepcopy(patterns):
        if not isinstance(pattern, dict):
            raise AtomicityCatalogError("ATOMICITY_PATTERN_INVALID")
        expression = pattern.get("regex")
        if not isinstance(expression, str) or len(expression) > MAX_PATTERN_LENGTH:
            raise AtomicityCatalogError("ATOMICITY_PATTERN_LENGTH_EXCEEDED")
        if not pattern.get("positive_examples") or not pattern.get("counterexamples"):
            raise AtomicityCatalogError("ATOMICITY_PATTERN_EVIDENCE_MISSING")
        re.compile(expression, flags=re.IGNORECASE)
        frozen.append(pattern)
    return tuple(frozen)


def semantic_atomicity_violations(
    extraction: ValidatedNarrativeExtractionVNext,
) -> tuple[ContractViolation, ...]:
    patterns = _load_patterns()
    violations: list[ContractViolation] = []
    for case_index, case in enumerate(extraction.cases):
        records = (*case.claims, *case.constraint_candidates, *case.unknowns)
        by_id = {record.claim_id: record for record in records}
        seen: set[str] = set()
        for pattern in patterns:
            expression = str(pattern["regex"])
            fields = set(pattern.get("fields", []))
            scope = pattern.get("scope")
            if scope == "record":
                for record in records:
                    if str(record.field) not in fields:
                        continue
                    if not re.search(expression, record.surface_value, flags=re.IGNORECASE):
                        continue
                    key = f"{case.case_id}:{record.claim_id}"
                    if key in seen:
                        continue
                    seen.add(key)
                    violations.append(
                        ContractViolation(
                            code=ViolationCode.SEMANTIC_REVIEW_REQUIRED,
                            path=("cases", case_index, "semantic_atomicity"),
                            record_ids=(record.claim_id,),
                        )
                    )
            elif scope == "contradiction_refs":
                for friction in case.friction_candidates:
                    if friction.type != FrictionType.CONTRADICTION:
                        continue
                    matched = tuple(
                        ref
                        for ref in friction.claim_refs
                        if ref in by_id
                        and re.search(
                            expression,
                            by_id[ref].surface_value,
                            flags=re.IGNORECASE,
                        )
                    )
                    if not matched:
                        continue
                    key = f"{case.case_id}:{','.join(matched)}"
                    if key in seen:
                        continue
                    seen.add(key)
                    violations.append(
                        ContractViolation(
                            code=ViolationCode.SEMANTIC_REVIEW_REQUIRED,
                            path=("cases", case_index, "semantic_atomicity"),
                            record_ids=matched,
                        )
                    )
            else:
                raise AtomicityCatalogError("ATOMICITY_SCOPE_INVALID")
    return tuple(violations)
