from __future__ import annotations

import hashlib
import json
from enum import StrEnum
from typing import Annotated, Any, Literal, Mapping, Sequence

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    ValidationError,
    field_validator,
    model_validator,
)


CONTRACT_VERSION = "2.3.0-candidate.1"
EXTRACTOR_ID = "MOC-EXTRACTOR-001-H"
H2_ARTIFACT_ID = "MOC-EXTRACTOR-001-H2"
H3_ARTIFACT_ID = "MOC-EXTRACTOR-001-H3"
MAX_NARRATIVE_CHARS = 20_000
MAX_SPAN_CHARS = 4_096
MAX_CASES = 1_000
MAX_RECORDS_PER_COLLECTION = 1_000
MAX_NORMALIZATION_PROPOSALS = 64
MAX_NORMALIZATION_CANDIDATES = 64

CaseId = Annotated[StrictStr, Field(pattern=r"^EXP-A-DEV-[0-9]{3}$")]
ClaimId = Annotated[StrictStr, Field(pattern=r"^DEV[0-9]{3}-C[0-9]{2}$")]
ConstraintId = Annotated[StrictStr, Field(pattern=r"^DEV[0-9]{3}-R[0-9]{2}$")]
UnknownId = Annotated[StrictStr, Field(pattern=r"^DEV[0-9]{3}-U[0-9]{2}$")]
RecordId = Annotated[StrictStr, Field(pattern=r"^DEV[0-9]{3}-[CRU][0-9]{2}$")]
NormRule = Annotated[
    StrictStr, Field(pattern=r"^NORM-[A-Z0-9-]+$", max_length=64)
]
FrictionRule = Annotated[
    StrictStr, Field(pattern=r"^FRICTION-[A-Z0-9-]+$", max_length=64)
]
MappingId = Annotated[StrictStr, Field(pattern=r"^MAP-[A-Z0-9-]+$", max_length=64)]
Sha256 = Annotated[StrictStr, Field(pattern=r"^[0-9a-f]{64}$")]


class FrozenModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        validate_default=True,
    )


class PrincipalField(StrEnum):
    ACCION_CANDIDATA = "accion_candidata"
    ACCION_RECHAZADA = "accion_rechazada"
    ACCION_REPORTADA = "accion_reportada"
    CLIMA_EMOCIONAL = "clima_emocional"
    CONDICION_FUTURA = "condicion_futura"
    ESTADO_FACTUAL = "estado_factual"
    ESTADO_TEMPORAL = "estado_temporal"
    EVALUACION_SITUACIONAL = "evaluacion_situacional"
    HORIZONTE_TEMPORAL = "horizonte_temporal"
    INTENCION_DECLARADA = "intencion_declarada"
    OBLIGACION_DECLARADA = "obligacion_declarada"
    RECURSO_MENCIONADO = "recurso_mencionado"
    VALOR_DECLARADO = "valor_declarado"


class ConstraintField(StrEnum):
    EXTERNA = "restriccion_externa"
    FINANCIERA = "restriccion_financiera"
    TECNICA = "restriccion_tecnica"


class FrictionType(StrEnum):
    AMBIGUITY = "ambiguity"
    CONTRADICTION = "contradiction"
    TENSION = "tension"


class FrictionVerificationStatus(StrEnum):
    CANDIDATE = "FRICTION_CANDIDATE"
    MECHANICALLY_VERIFIED = "FRICTION_MECHANICALLY_VERIFIED"
    SEMANTIC_REVIEW_REQUIRED = "FRICTION_SEMANTIC_REVIEW_REQUIRED"


class StructuredPredicate(StrEnum):
    SAME_DIMENSION_OPPOSITE_BOOLEAN = "same_dimension_opposite_boolean"


class NormalizationStatus(StrEnum):
    NORMALIZED = "NORMALIZED"
    UNRESOLVED = "NORMALIZATION_UNRESOLVED"
    AMBIGUOUS = "NORMALIZATION_AMBIGUOUS"
    REJECTED_MAPPING = "REJECTED_RULE_FIELD_MAPPING"


class AtomicityStatus(StrEnum):
    STRUCTURAL_ATOMICITY_VALID = "STRUCTURAL_ATOMICITY_VALID"
    SEMANTIC_REVIEW_REQUIRED = "SEMANTIC_REVIEW_REQUIRED"


class ViolationCode(StrEnum):
    STRUCTURAL_INVALID = "STRUCTURAL_INVALID"
    SPAN_BOUNDS_INVALID = "SPAN_BOUNDS_INVALID"
    SPAN_LENGTH_MISMATCH = "SPAN_LENGTH_MISMATCH"
    SPAN_NOT_EXACT = "SPAN_NOT_EXACT"
    SPAN_NOT_CONTAINED = "SPAN_NOT_CONTAINED"
    SURFACE_NOT_MINIMAL_TEXT = "SURFACE_NOT_MINIMAL_TEXT"
    ORDER_NOT_MINIMAL = "ORDER_NOT_MINIMAL"
    ID_NOT_DETERMINISTIC = "ID_NOT_DETERMINISTIC"
    BROKEN_REFERENCE = "BROKEN_REFERENCE"
    DUPLICATE_RECORD = "DUPLICATE_RECORD"
    OVERLAP_SAME_FIELD = "OVERLAP_SAME_FIELD"
    OVERLAP_UNJUSTIFIED = "OVERLAP_UNJUSTIFIED"
    ATOMICITY_COORDINATED_ALTERNATIVE = "ATOMICITY_COORDINATED_ALTERNATIVE"
    SEMANTIC_REVIEW_REQUIRED = "SEMANTIC_REVIEW_REQUIRED"
    CONTRADICTION_CARDINALITY = "CONTRADICTION_CARDINALITY"
    DUPLICATE_FRICTION_REF = "DUPLICATE_FRICTION_REF"
    DUPLICATE_RECORD_ID = "DUPLICATE_RECORD_ID"
    FRICTION_RULE_UNKNOWN = "FRICTION_RULE_UNKNOWN"
    FRICTION_TYPE_MISMATCH = "FRICTION_TYPE_MISMATCH"
    FRICTION_CARDINALITY_MISMATCH = "FRICTION_CARDINALITY_MISMATCH"
    FRICTION_FIELD_MISMATCH = "FRICTION_FIELD_MISMATCH"
    FRICTION_PROVENANCE_MISMATCH = "FRICTION_PROVENANCE_MISMATCH"
    FRICTION_REFERENCE_INVALID = "FRICTION_REFERENCE_INVALID"
    FRICTION_SEMANTIC_REVIEW_REQUIRED = "FRICTION_SEMANTIC_REVIEW_REQUIRED"


class EvidenceSpanVNext(FrozenModel):
    text: Annotated[StrictStr, Field(min_length=1, max_length=MAX_SPAN_CHARS)]
    start: Annotated[StrictInt, Field(ge=0)]
    end: Annotated[StrictInt, Field(gt=0)]

    @model_validator(mode="after")
    def validate_bounds(self) -> "EvidenceSpanVNext":
        if self.end <= self.start:
            raise ValueError("SPAN_BOUNDS_INVALID")
        if self.end - self.start != len(self.text):
            raise ValueError("SPAN_LENGTH_MISMATCH")
        return self


class ContextFact(FrozenModel):
    key: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    value: Annotated[StrictStr, Field(min_length=1, max_length=512)]


class NarrativeCaseInputVNext(FrozenModel):
    case_id: CaseId
    raw_narrative: Annotated[
        StrictStr, Field(min_length=1, max_length=MAX_NARRATIVE_CHARS)
    ]


class NarrativeExtractionInputVNext(FrozenModel):
    schema_version: Literal[CONTRACT_VERSION] = CONTRACT_VERSION
    extractor_id: Literal[EXTRACTOR_ID] = EXTRACTOR_ID
    normalization_catalog_version: Annotated[StrictStr, Field(min_length=1)]
    normalization_catalog_sha256: Sha256
    friction_catalog_version: Annotated[StrictStr, Field(min_length=1)]
    friction_catalog_sha256: Sha256
    cases: Annotated[
        tuple[NarrativeCaseInputVNext, ...], Field(min_length=1, max_length=MAX_CASES)
    ]

    @model_validator(mode="after")
    def unique_cases(self) -> "NarrativeExtractionInputVNext":
        ids = [case.case_id for case in self.cases]
        if len(ids) != len(set(ids)):
            raise ValueError("DUPLICATE_CASE_ID")
        return self


Proposals = Annotated[
    tuple[Annotated[StrictStr, Field(min_length=1, max_length=512)], ...],
    Field(max_length=MAX_NORMALIZATION_PROPOSALS),
]


class AtomicClaimVNext(FrozenModel):
    claim_id: ClaimId
    field: PrincipalField
    surface_value: Annotated[StrictStr, Field(min_length=1, max_length=MAX_SPAN_CHARS)]
    provenance: Literal["reported"] = "reported"
    normalization_rule: NormRule
    minimal_evidence_span: EvidenceSpanVNext
    maximal_semantic_span: EvidenceSpanVNext | None = None
    llm_proposed_normalized_values: Proposals = ()
    overlap_justification: Annotated[
        StrictStr, Field(min_length=1, max_length=512)
    ] | None = None


class ConstraintCandidateVNext(FrozenModel):
    claim_id: ConstraintId
    field: ConstraintField
    surface_value: Annotated[StrictStr, Field(min_length=1, max_length=MAX_SPAN_CHARS)]
    provenance: Literal["reported_constraint"] = "reported_constraint"
    normalization_rule: NormRule
    operational_effect: Literal["unknown"] = "unknown"
    requires_verification: StrictBool = True
    minimal_evidence_span: EvidenceSpanVNext
    maximal_semantic_span: EvidenceSpanVNext | None = None
    llm_proposed_normalized_values: Proposals = ()
    overlap_justification: Annotated[
        StrictStr, Field(min_length=1, max_length=512)
    ] | None = None

    @model_validator(mode="after")
    def verification_must_be_true(self) -> "ConstraintCandidateVNext":
        if self.requires_verification is not True:
            raise ValueError("REQUIRES_VERIFICATION_TRUE")
        return self


class ExplicitUnknownVNext(FrozenModel):
    claim_id: UnknownId
    field: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    type: Literal["explicit_unknown"] = "explicit_unknown"
    surface_value: Annotated[StrictStr, Field(min_length=1, max_length=MAX_SPAN_CHARS)]
    minimal_evidence_span: EvidenceSpanVNext
    maximal_semantic_span: EvidenceSpanVNext | None = None
    overlap_justification: Annotated[
        StrictStr, Field(min_length=1, max_length=512)
    ] | None = None


RecordVNext = AtomicClaimVNext | ConstraintCandidateVNext | ExplicitUnknownVNext


class FrictionCandidateInput(FrozenModel):
    type: FrictionType
    claim_refs: Annotated[tuple[RecordId, ...], Field(min_length=1, max_length=8)]
    annotation_rule: FrictionRule
    description: Annotated[StrictStr, Field(min_length=1, max_length=1_024)]
    verification_status: Literal[FrictionVerificationStatus.CANDIDATE] = (
        FrictionVerificationStatus.CANDIDATE
    )

    @model_validator(mode="after")
    def references_are_unique(self) -> "FrictionCandidateInput":
        if len(self.claim_refs) != len(set(self.claim_refs)):
            raise ValueError("DUPLICATE_FRICTION_REF")
        return self


FrictionCandidateVNext = FrictionCandidateInput


class StructuredFact(FrozenModel):
    record_id: RecordId
    dimension: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    boolean_value: StrictBool
    source_mapping_id: MappingId
    source_mapping_version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    source_mapping_sha256: Sha256
    provenance: Literal["deterministic_mapping"] = "deterministic_mapping"


class FactSourceReference(FrozenModel):
    record_id: RecordId
    source_mapping_id: MappingId
    source_mapping_version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    source_mapping_sha256: Sha256
    provenance: Literal["deterministic_mapping"] = "deterministic_mapping"


class RecomputedStructuredFact(FrozenModel):
    record_id: RecordId
    dimension: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    boolean_value: StrictBool
    derivation_rule_id: Literal["FACT-BOOLEAN-STATE-ES-001"] = (
        "FACT-BOOLEAN-STATE-ES-001"
    )
    canonical_claim_sha256: Sha256


class FrictionMechanicalProof(FrozenModel):
    verification_rule_id: FrictionRule
    rule_version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    claim_refs: Annotated[tuple[RecordId, ...], Field(min_length=2, max_length=8)]
    canonical_claims_sha256: Sha256
    structured_predicate: StructuredPredicate
    predicate_id: StructuredPredicate
    predicate_result: Literal[True] = True
    catalog_version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    catalog_sha256: Sha256
    generated_by: Literal["moc_extractor_001_h3.friction_verifier"] = (
        "moc_extractor_001_h3.friction_verifier"
    )

    def __init__(self, **data: Any) -> None:
        raise TypeError("FRICTION_PROOF_INTERNAL_RESULT_ONLY")

    @classmethod
    def model_validate(cls, obj: Any, **kwargs: Any):
        if isinstance(obj, cls):
            return obj
        raise ValidationError.from_exception_data(
            cls.__name__,
            [
                {
                    "type": "value_error",
                    "loc": (),
                    "input": "redacted",
                    "ctx": {"error": ValueError("FRICTION_PROOF_EXTERNAL_REJECTED")},
                }
            ],
        )

    @classmethod
    def model_validate_json(cls, json_data: str | bytes | bytearray, **kwargs: Any):
        raise ValidationError.from_exception_data(
            cls.__name__,
            [
                {
                    "type": "value_error",
                    "loc": (),
                    "input": "redacted",
                    "ctx": {"error": ValueError("FRICTION_PROOF_EXTERNAL_REJECTED")},
                }
            ],
        )

    @classmethod
    def _from_recomputed(cls, **data: Any) -> "FrictionMechanicalProof":
        return cls.model_construct(**data)


class MechanicallyVerifiedFriction(FrozenModel):
    candidate: FrictionCandidateInput
    verification_status: Literal[FrictionVerificationStatus.MECHANICALLY_VERIFIED] = (
        FrictionVerificationStatus.MECHANICALLY_VERIFIED
    )
    proof: FrictionMechanicalProof

    def __init__(self, **data: Any) -> None:
        raise TypeError("MECHANICALLY_VERIFIED_FRICTION_INTERNAL_RESULT_ONLY")

    @classmethod
    def model_validate(cls, obj: Any, **kwargs: Any):
        if isinstance(obj, cls):
            return obj
        raise ValidationError.from_exception_data(
            cls.__name__,
            [
                {
                    "type": "value_error",
                    "loc": (),
                    "input": "redacted",
                    "ctx": {
                        "error": ValueError(
                            "MECHANICALLY_VERIFIED_FRICTION_EXTERNAL_REJECTED"
                        )
                    },
                }
            ],
        )

    @classmethod
    def model_validate_json(cls, json_data: str | bytes | bytearray, **kwargs: Any):
        raise ValidationError.from_exception_data(
            cls.__name__,
            [
                {
                    "type": "value_error",
                    "loc": (),
                    "input": "redacted",
                    "ctx": {
                        "error": ValueError(
                            "MECHANICALLY_VERIFIED_FRICTION_EXTERNAL_REJECTED"
                        )
                    },
                }
            ],
        )

    @classmethod
    def _from_recomputed(
        cls,
        *,
        candidate: FrictionCandidateInput,
        proof: FrictionMechanicalProof,
    ) -> "MechanicallyVerifiedFriction":
        return cls.model_construct(
            candidate=candidate,
            verification_status=FrictionVerificationStatus.MECHANICALLY_VERIFIED,
            proof=proof,
        )


class FrictionReviewItem(FrozenModel):
    candidate: FrictionCandidateInput
    verification_status: Literal[
        FrictionVerificationStatus.SEMANTIC_REVIEW_REQUIRED
    ] = FrictionVerificationStatus.SEMANTIC_REVIEW_REQUIRED
    reason_code: Literal[
        "NO_STRUCTURED_PREDICATE",
        "STRUCTURED_FACTS_MISSING",
        "STRUCTURED_FACT_SOURCE_UNTRUSTED",
        "STRUCTURED_PREDICATE_FALSE",
    ]


def _prefix(case_id: str) -> str:
    return "DEV" + case_id.rsplit("-", 1)[-1]


def _record_key(record: RecordVNext) -> tuple[int, int, str, str]:
    span = record.minimal_evidence_span
    return (span.start, span.end, str(record.field), record.surface_value)


def _validate_record_span(raw_narrative: str, record: RecordVNext) -> None:
    minimal = record.minimal_evidence_span
    if (
        minimal.end > len(raw_narrative)
        or raw_narrative[minimal.start : minimal.end] != minimal.text
    ):
        raise ValueError("SPAN_NOT_EXACT")
    if record.surface_value != minimal.text:
        raise ValueError("SURFACE_NOT_MINIMAL_TEXT")
    maximal = record.maximal_semantic_span
    if maximal is not None:
        if (
            maximal.end > len(raw_narrative)
            or raw_narrative[maximal.start : maximal.end] != maximal.text
        ):
            raise ValueError("SPAN_NOT_EXACT")
        if not (maximal.start <= minimal.start and minimal.end <= maximal.end):
            raise ValueError("SPAN_NOT_CONTAINED")


def _validate_ids(case_id: str, records: Sequence[RecordVNext], marker: str) -> None:
    prefix = _prefix(case_id)
    for index, record in enumerate(records, start=1):
        expected = f"{prefix}-{marker}{index:02d}"
        if record.claim_id != expected:
            raise ValueError("ID_NOT_DETERMINISTIC")


def _ranges_overlap(left: EvidenceSpanVNext, right: EvidenceSpanVNext) -> bool:
    return left.start < right.end and right.start < left.end


class ValidatedCaseExtractionVNext(FrozenModel):
    case_id: CaseId
    raw_narrative: Annotated[
        StrictStr, Field(min_length=1, max_length=MAX_NARRATIVE_CHARS)
    ]
    claims: Annotated[
        tuple[AtomicClaimVNext, ...], Field(max_length=MAX_RECORDS_PER_COLLECTION)
    ] = ()
    constraint_candidates: Annotated[
        tuple[ConstraintCandidateVNext, ...],
        Field(max_length=MAX_RECORDS_PER_COLLECTION),
    ] = ()
    unknowns: Annotated[
        tuple[ExplicitUnknownVNext, ...], Field(max_length=MAX_RECORDS_PER_COLLECTION)
    ] = ()
    friction_candidates: Annotated[
        tuple[FrictionCandidateInput, ...],
        Field(max_length=MAX_RECORDS_PER_COLLECTION),
    ] = ()

    @model_validator(mode="after")
    def validate_structural_contract(self) -> "ValidatedCaseExtractionVNext":
        collections: tuple[tuple[RecordVNext, ...], ...] = (
            self.claims,
            self.constraint_candidates,
            self.unknowns,
        )
        records = tuple(record for collection in collections for record in collection)
        for record in records:
            _validate_record_span(self.raw_narrative, record)
        for collection in collections:
            if tuple(sorted(collection, key=_record_key)) != collection:
                raise ValueError("ORDER_NOT_MINIMAL")
        _validate_ids(self.case_id, self.claims, "C")
        _validate_ids(self.case_id, self.constraint_candidates, "R")
        _validate_ids(self.case_id, self.unknowns, "U")

        ids = [record.claim_id for record in records]
        if len(ids) != len(set(ids)):
            raise ValueError("DUPLICATE_RECORD_ID")
        signatures = [
            (
                str(record.field),
                record.surface_value,
                record.minimal_evidence_span.start,
                record.minimal_evidence_span.end,
            )
            for record in records
        ]
        if len(signatures) != len(set(signatures)):
            raise ValueError("DUPLICATE_RECORD")

        by_id = {record.claim_id: record for record in records}
        for friction in self.friction_candidates:
            if any(ref not in by_id for ref in friction.claim_refs):
                raise ValueError("BROKEN_REFERENCE")

        for index, left in enumerate(records):
            for right in records[index + 1 :]:
                if not _ranges_overlap(
                    left.minimal_evidence_span, right.minimal_evidence_span
                ):
                    continue
                if str(left.field) == str(right.field):
                    raise ValueError("OVERLAP_SAME_FIELD")
                if not left.overlap_justification or not right.overlap_justification:
                    raise ValueError("OVERLAP_UNJUSTIFIED")
        return self


class ValidatedNarrativeExtractionVNext(FrozenModel):
    schema_version: Literal[CONTRACT_VERSION] = CONTRACT_VERSION
    extractor_id: Literal[EXTRACTOR_ID] = EXTRACTOR_ID
    normalization_catalog_version: Annotated[StrictStr, Field(min_length=1)]
    normalization_catalog_sha256: Sha256
    friction_catalog_version: Annotated[StrictStr, Field(min_length=1)]
    friction_catalog_sha256: Sha256
    cases: Annotated[
        tuple[ValidatedCaseExtractionVNext, ...],
        Field(min_length=1, max_length=MAX_CASES),
    ]

    @model_validator(mode="after")
    def unique_cases(self) -> "ValidatedNarrativeExtractionVNext":
        ids = [case.case_id for case in self.cases]
        if len(ids) != len(set(ids)):
            raise ValueError("DUPLICATE_CASE_ID")
        return self


class ContractViolation(FrozenModel):
    code: ViolationCode
    path: tuple[StrictStr | StrictInt, ...] = ()
    record_ids: tuple[RecordId, ...] = ()


class ContractValidationResult(FrozenModel):
    valid: StrictBool
    structural_valid: StrictBool
    semantic_atomicity: AtomicityStatus
    extraction: ValidatedNarrativeExtractionVNext | None = None
    candidate_extraction: ValidatedNarrativeExtractionVNext | None = None
    accepted_frictions: tuple[MechanicallyVerifiedFriction, ...] = ()
    friction_review_required: tuple[FrictionReviewItem, ...] = ()
    violations: tuple[ContractViolation, ...] = ()


def _code_from_error(error: Mapping[str, Any]) -> ViolationCode:
    message = str(error.get("ctx", {}).get("error", ""))
    for code in ViolationCode:
        if code.value in message:
            return code
    return ViolationCode.STRUCTURAL_INVALID


def validate_extraction(
    payload: Mapping[str, Any],
    *,
    fact_sources: Sequence[FactSourceReference | Mapping[str, Any]] = (),
    structured_facts: Sequence[StructuredFact | Mapping[str, Any]] = (),
) -> ContractValidationResult:
    try:
        extraction = ValidatedNarrativeExtractionVNext.model_validate(payload)
    except ValidationError as exc:
        violations = tuple(
            ContractViolation(code=_code_from_error(error), path=tuple(error["loc"]))
            for error in exc.errors(include_input=False, include_url=False)
        )
        return ContractValidationResult(
            valid=False,
            structural_valid=False,
            semantic_atomicity=AtomicityStatus.SEMANTIC_REVIEW_REQUIRED,
            violations=violations,
        )

    from .atomicity import semantic_atomicity_violations
    from .frictions import validate_friction_candidates

    if fact_sources and structured_facts:
        return ContractValidationResult(
            valid=False,
            structural_valid=False,
            semantic_atomicity=AtomicityStatus.SEMANTIC_REVIEW_REQUIRED,
            candidate_extraction=extraction,
            violations=(
                ContractViolation(
                    code=ViolationCode.STRUCTURAL_INVALID,
                    path=("fact_sources",),
                ),
            ),
        )

    try:
        if structured_facts:
            legacy = tuple(
                item
                if isinstance(item, StructuredFact)
                else StructuredFact.model_validate(item)
                for item in structured_facts
            )
            sources = tuple(
                FactSourceReference(
                    record_id=item.record_id,
                    source_mapping_id=item.source_mapping_id,
                    source_mapping_version=item.source_mapping_version,
                    source_mapping_sha256=item.source_mapping_sha256,
                    provenance=item.provenance,
                )
                for item in legacy
            )
        else:
            sources = tuple(
                item
                if isinstance(item, FactSourceReference)
                else FactSourceReference.model_validate(item)
                for item in fact_sources
            )
    except ValidationError as exc:
        violations = tuple(
            ContractViolation(code=_code_from_error(error), path=tuple(error["loc"]))
            for error in exc.errors(include_input=False, include_url=False)
        )
        return ContractValidationResult(
            valid=False,
            structural_valid=False,
            semantic_atomicity=AtomicityStatus.SEMANTIC_REVIEW_REQUIRED,
            candidate_extraction=extraction,
            violations=violations,
        )

    semantic_violations = semantic_atomicity_violations(extraction)
    friction_violations, accepted_frictions, friction_review = (
        validate_friction_candidates(extraction, fact_sources=sources)
    )
    violations = (*semantic_violations, *friction_violations)
    return ContractValidationResult(
        valid=not violations,
        structural_valid=True,
        semantic_atomicity=AtomicityStatus.SEMANTIC_REVIEW_REQUIRED,
        extraction=extraction if not violations else None,
        candidate_extraction=extraction,
        accepted_frictions=accepted_frictions,
        friction_review_required=friction_review,
        violations=violations,
    )


class NormalizationRequest(FrozenModel):
    record_id: RecordId
    field: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    surface_value: Annotated[StrictStr, Field(min_length=1, max_length=MAX_SPAN_CHARS)]
    normalization_rule: NormRule
    allowed_context: tuple[ContextFact, ...] = ()
    catalog_version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    catalog_sha256: Sha256
    llm_proposed_normalized_values: Proposals = ()

    @field_validator("allowed_context")
    @classmethod
    def context_keys_unique(
        cls, value: tuple[ContextFact, ...]
    ) -> tuple[ContextFact, ...]:
        keys = [item.key for item in value]
        if len(keys) != len(set(keys)):
            raise ValueError("DUPLICATE_CONTEXT_KEY")
        return value


class NormalizationResult(FrozenModel):
    record_id: RecordId
    status: NormalizationStatus
    normalized_value: Annotated[StrictStr, Field(min_length=1, max_length=512)] | None = None
    normalization_family: Annotated[StrictStr, Field(min_length=1, max_length=512)] | None = None
    normalization_subtype: Annotated[StrictStr, Field(min_length=1, max_length=512)] | None = None
    candidates: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=512)], ...],
        Field(max_length=MAX_NORMALIZATION_CANDIDATES),
    ] = ()
    llm_proposed_normalized_values: Proposals = ()
    rule: NormRule
    catalog_version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    mapping_id: MappingId | None = None
    mapping_version: Annotated[StrictStr, Field(min_length=1, max_length=128)] | None = None
    mapping_sha256: Sha256 | None = None
    method: Literal["exact_closed_mapping"] = "exact_closed_mapping"
    provenance: Literal["signed_mapping_contract"] = "signed_mapping_contract"
    catalog_sha256: Sha256
    diagnostic_code: Annotated[StrictStr, Field(min_length=1, max_length=128)]

    @model_validator(mode="after")
    def normalized_value_only_when_authorized(self) -> "NormalizationResult":
        if self.status == NormalizationStatus.NORMALIZED and self.normalized_value is None:
            raise ValueError("NORMALIZED_VALUE_REQUIRED")
        if self.status != NormalizationStatus.NORMALIZED and self.normalized_value is not None:
            raise ValueError("NORMALIZED_VALUE_FORBIDDEN")
        mapping_identity = (self.mapping_id, self.mapping_version, self.mapping_sha256)
        if self.status == NormalizationStatus.NORMALIZED and any(
            item is None for item in mapping_identity
        ):
            raise ValueError("NORMALIZED_MAPPING_IDENTITY_REQUIRED")
        if self.status != NormalizationStatus.NORMALIZED and any(
            item is not None for item in mapping_identity
        ):
            raise ValueError("NON_NORMALIZED_MAPPING_IDENTITY_FORBIDDEN")
        return self


class DeterministicallyNormalizedExtraction(FrozenModel):
    schema_version: Literal[CONTRACT_VERSION] = CONTRACT_VERSION
    extractor_id: Literal[EXTRACTOR_ID] = EXTRACTOR_ID
    source_extraction_sha256: Sha256
    catalog_version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    catalog_sha256: Sha256
    results: tuple[NormalizationResult, ...]


def canonical_json_bytes(value: BaseModel | Mapping[str, Any] | list[Any]) -> bytes:
    data = value.model_dump(mode="json") if isinstance(value, BaseModel) else value
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_sha256(value: BaseModel | Mapping[str, Any] | list[Any]) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()
