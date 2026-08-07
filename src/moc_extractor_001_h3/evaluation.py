from __future__ import annotations

from enum import StrEnum
from typing import Literal

from pydantic import StrictBool

from .models import EvidenceSpanVNext, FrozenModel


class SpanAssessmentCode(StrEnum):
    PASS_MINIMAL_EXACT = "PASS_MINIMAL_EXACT"
    PASS_MAXIMAL_LITERAL = "PASS_MAXIMAL_LITERAL"
    FAIL_MINIMAL_NOT_EXACT = "FAIL_MINIMAL_NOT_EXACT"
    FAIL_MAXIMAL_OUTSIDE_ALLOWED = "FAIL_MAXIMAL_OUTSIDE_ALLOWED"
    FAIL_NOT_LITERAL = "FAIL_NOT_LITERAL"
    FAIL_OFFSETS = "FAIL_OFFSETS"


class SpanAssessment(FrozenModel):
    passed: StrictBool
    code: SpanAssessmentCode
    minimal_exact: StrictBool = False
    maximal_coverage: StrictBool = False
    classification_scored_separately: Literal[True] = True
    normalization_scored_separately: Literal[True] = True


def assess_span(
    *,
    raw_narrative: str,
    candidate: EvidenceSpanVNext,
    expected_minimal: EvidenceSpanVNext,
    allowed_maximal: EvidenceSpanVNext | None = None,
    role: str = "minimal",
) -> SpanAssessment:
    if candidate.end > len(raw_narrative):
        return SpanAssessment(passed=False, code=SpanAssessmentCode.FAIL_OFFSETS)
    if raw_narrative[candidate.start : candidate.end] != candidate.text:
        return SpanAssessment(passed=False, code=SpanAssessmentCode.FAIL_NOT_LITERAL)
    if role == "minimal":
        exact = candidate == expected_minimal
        return SpanAssessment(
            passed=exact,
            code=(
                SpanAssessmentCode.PASS_MINIMAL_EXACT
                if exact
                else SpanAssessmentCode.FAIL_MINIMAL_NOT_EXACT
            ),
            minimal_exact=exact,
        )
    if role != "maximal":
        raise ValueError("SPAN_ROLE_INVALID")
    if allowed_maximal is None:
        return SpanAssessment(
            passed=False,
            code=SpanAssessmentCode.FAIL_MAXIMAL_OUTSIDE_ALLOWED,
        )
    contained = (
        allowed_maximal.start <= candidate.start <= expected_minimal.start
        and expected_minimal.end <= candidate.end <= allowed_maximal.end
    )
    return SpanAssessment(
        passed=contained,
        code=(
            SpanAssessmentCode.PASS_MAXIMAL_LITERAL
            if contained
            else SpanAssessmentCode.FAIL_MAXIMAL_OUTSIDE_ALLOWED
        ),
        maximal_coverage=contained,
    )
