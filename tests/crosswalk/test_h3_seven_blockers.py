from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

from pydantic import ValidationError

from moc_extractor_001_h3 import MigrationError, validate_extraction
from moc_extractor_001_h3.models import (
    FrictionCandidateInput,
    FrictionMechanicalProof,
    FrictionVerificationStatus,
    MechanicallyVerifiedFriction,
    StructuredPredicate,
)


HELPER_PATH = Path(__file__).resolve().parents[1] / "test_moc_extractor_001_h3.py"
SPEC = importlib.util.spec_from_file_location("h3_test_helpers", HELPER_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("H3_HELPER_IMPORT_FAILED")
HELPERS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HELPERS)


def forged_proof() -> FrictionMechanicalProof:
    return FrictionMechanicalProof.model_construct(
        verification_rule_id="FRICTION-CONTRA-001",
        rule_version="forged",
        claim_refs=("DEV901-C01", "DEV901-C02"),
        canonical_claims_sha256="f" * 64,
        structured_predicate=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
        predicate_id=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
        predicate_result=True,
        catalog_version="forged",
        catalog_sha256="f" * 64,
        generated_by="moc_extractor_001_h3.friction_verifier",
    )


class H3SevenBlockerCrosswalk(unittest.TestCase):
    def test_01_lying_list_subclass_is_rejected(self) -> None:
        class LyingList(list):
            def __len__(self):
                return 1

        source, projected = HELPERS.source_payload(13)
        source["cases"] = LyingList(source["cases"])
        with self.assertRaises(MigrationError):
            HELPERS.migrate(source, projected)

    def test_02_direct_proof_constructor_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            FrictionMechanicalProof(
                verification_rule_id="FRICTION-CONTRA-001",
                rule_version="forged",
                claim_refs=("DEV901-C01", "DEV901-C02"),
                canonical_claims_sha256="f" * 64,
                structured_predicate=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
                predicate_id=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
                catalog_version="forged",
                catalog_sha256="f" * 64,
            )

    def test_03_direct_verified_constructor_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            MechanicallyVerifiedFriction(
                candidate=FrictionCandidateInput.model_validate(HELPERS.candidate()),
                proof=forged_proof(),
            )

    def test_04_serialized_forged_state_is_rejected(self) -> None:
        forged = MechanicallyVerifiedFriction.model_construct(
            candidate=FrictionCandidateInput.model_validate(HELPERS.candidate()),
            verification_status=FrictionVerificationStatus.MECHANICALLY_VERIFIED,
            proof=forged_proof(),
        )
        with self.assertRaises(ValidationError):
            MechanicallyVerifiedFriction.model_validate_json(forged.model_dump_json())

    def test_05_generator_is_typed_rejection(self) -> None:
        source, projected = HELPERS.source_payload(1)
        source["cases"] = (item for item in source["cases"])
        with self.assertRaises(MigrationError):
            HELPERS.migrate(source, projected)

    def test_06_tuple_is_rejected(self) -> None:
        source, projected = HELPERS.source_payload(1)
        source["cases"] = tuple(source["cases"])
        with self.assertRaises(MigrationError):
            HELPERS.migrate(source, projected)

    def test_07_forged_fact_source_metadata_cannot_verify(self) -> None:
        sources = HELPERS.fact_sources()
        sources[0]["source_mapping_id"] = "MAP-H3-FORGED-001"
        result = validate_extraction(HELPERS.extraction_payload(), fact_sources=sources)
        self.assertFalse(result.valid)
        self.assertEqual(result.accepted_frictions, ())


if __name__ == "__main__":
    unittest.main()
