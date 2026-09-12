"""Verify the sidecar against the actual RC1 MatrixQ and MatrixRow classes.

On Windows, RC1 cannot be imported directly because its POSIX vault imports
fcntl at module load time.  This verifier installs an inert import-only shim.
It never instantiates or exercises the vault, persistence or locking code.
Consequently, a PASS proves only model-boundary compatibility and
non-mutation; it is not an RC1 runtime or scientific validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import types
from pathlib import Path

from moc_geometry_extension import adapt_rc1_matrix


EXPECTED_FILES = ("moc_pipeline_impl.py", "MOC-RC1-FREEZE-001.md")


def _install_windows_import_only_fcntl_shim() -> bool:
    if os.name != "nt" or "fcntl" in sys.modules:
        return False
    module = types.ModuleType("fcntl")
    module.LOCK_EX = 2
    module.LOCK_SH = 1
    module.LOCK_UN = 8

    def unsupported(*_args: object, **_kwargs: object) -> None:
        raise RuntimeError("the import-only fcntl shim cannot perform file locking")

    module.flock = unsupported
    sys.modules["fcntl"] = module
    return True


def _sha256_json(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def verify(rc1_directory: Path) -> dict[str, object]:
    rc1_directory = rc1_directory.resolve()
    missing = [name for name in EXPECTED_FILES if not (rc1_directory / name).is_file()]
    if missing:
        raise FileNotFoundError(f"not an extracted RC1 directory; missing={missing}")

    shim_used = _install_windows_import_only_fcntl_shim()
    sys.path.insert(0, str(rc1_directory))
    try:
        from moc_pipeline_impl import MatrixQ, MatrixRow
    finally:
        sys.path.pop(0)

    coordinates = {
        "I": (0.10, 0.20, 0.30, 0.40),
        "E": (0.40, 0.30, 0.20, 0.10),
        "A": (0.25, 0.25, 0.25, 0.25),
        "V": (0.55, 0.15, 0.15, 0.15),
        "S": (0.15, 0.15, 0.15, 0.55),
    }
    matrix = MatrixQ(
        rows={
            name: MatrixRow(
                coordinates=values,
                provenance="interpretive_hypothesis",
                confidence=0.50,
            )
            for name, values in coordinates.items()
        }
    )
    before = matrix.model_dump(mode="json")
    before_digest = _sha256_json(before)
    snapshot = adapt_rc1_matrix(
        matrix,
        row_mapping={"I": "P", "E": "Eaf", "A": "Act", "V": "V", "S": "S"},
        snapshot_id="actual-rc1-model-boundary-check",
        time_index=0,
        source_id="local-extracted-rc1-baseline",
    )
    after = matrix.model_dump(mode="json")
    after_digest = _sha256_json(after)
    if before != after or before_digest != after_digest:
        raise AssertionError("the sidecar mutated the RC1 MatrixQ")
    if snapshot.relations:
        raise AssertionError("the adapter created observed relations from a row mapping")

    return {
        "ACTUAL_RC1_MODEL_ADAPTER": "PASS",
        "RC1_MATRIX_UNCHANGED": True,
        "RC1_MATRIX_DIGEST_BEFORE": before_digest,
        "RC1_MATRIX_DIGEST_AFTER": after_digest,
        "SNAPSHOT_DIGEST": snapshot.digest(),
        "OBSERVED_RELATIONS_CREATED": len(snapshot.relations),
        "FCNTL_IMPORT_ONLY_SHIM_USED": shim_used,
        "RUNTIME_SCOPE": "MODEL_BOUNDARY_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rc1_directory", type=Path)
    arguments = parser.parse_args()
    print(json.dumps(verify(arguments.rc1_directory), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

