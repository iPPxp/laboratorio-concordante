"""Build a deterministic candidate overlay bound to an exact RC1 archive."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import shutil
import tarfile
import tempfile
from pathlib import Path


PACKAGE_NAME = "MOC-RC1-GEOMETRY-EXTENSION-001"
PAYLOAD_FILES = (
    "moc_geometry_extension.py",
    "test_moc_geometry_extension.py",
    "verify_rc1_adapter.py",
    "README.md",
    "MOC-RC1-GEOMETRY-EXTENSION-001.md",
    "RC1_COMPATIBILITY.md",
    "STATUS.md",
    "pyproject.toml",
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _verify_rc1_archive(archive: Path) -> None:
    with tarfile.open(archive, "r:gz") as bundle:
        names = set(bundle.getnames())
    required_suffixes = ("/MOC-RC1-FREEZE-001.md", "/moc_pipeline_impl.py")
    missing = [suffix for suffix in required_suffixes if not any(name.endswith(suffix) for name in names)]
    if missing:
        raise ValueError(f"archive does not expose the expected RC1 baseline: missing={missing}")


def _add_tree_deterministically(source: Path, output_archive: Path) -> None:
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for path in sorted(source.rglob("*"), key=lambda item: item.as_posix()):
            relative = Path(PACKAGE_NAME) / path.relative_to(source)
            info = tar.gettarinfo(str(path), arcname=relative.as_posix())
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            info.mtime = 0
            if path.is_file():
                with path.open("rb") as stream:
                    tar.addfile(info, stream)
            else:
                tar.addfile(info)
    buffer.seek(0)
    with output_archive.open("wb") as destination:
        with gzip.GzipFile(filename="", mode="wb", fileobj=destination, mtime=0) as compressed:
            shutil.copyfileobj(buffer, compressed)


def build(rc1_archive: Path, output_directory: Path) -> tuple[Path, Path]:
    source_directory = Path(__file__).resolve().parent
    rc1_archive = rc1_archive.resolve()
    output_directory = output_directory.resolve()
    if not rc1_archive.is_file():
        raise FileNotFoundError(rc1_archive)
    _verify_rc1_archive(rc1_archive)
    output_directory.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="moc_rc1_geometry_") as temporary:
        staging = Path(temporary) / PACKAGE_NAME
        staging.mkdir()
        for name in PAYLOAD_FILES:
            source = source_directory / name
            if not source.is_file():
                raise FileNotFoundError(source)
            shutil.copy2(source, staging / name)

        baseline = {
            "BASE_ARCHIVE": rc1_archive.name,
            "BASE_ARCHIVE_SHA256": _sha256(rc1_archive),
            "BASE_RELEASE": "MOC Base 1.0-RC1",
            "EXTENSION_ID": PACKAGE_NAME,
            "EXTENSION_STATUS": "CANDIDATE",
            "INTEGRATION_MODE": "OPTIONAL_NON_MUTATING_SIDECAR",
            "RC1_BYTES_INCLUDED": False,
            "RC1_ORIGINAL_MUTATED": False,
        }
        _write_json(staging / "BASELINE.json", baseline)

        covered = sorted(path for path in staging.iterdir() if path.is_file())
        integrity = {
            "algorithm": "SHA-256",
            "files": {path.name: _sha256(path) for path in covered},
            "package": PACKAGE_NAME,
        }
        _write_json(staging / "INTEGRITY.json", integrity)
        all_except_sums = sorted(path for path in staging.iterdir() if path.is_file())
        sums = "".join(f"{_sha256(path)}  {path.name}\n" for path in all_except_sums)
        (staging / "SHA256SUMS.txt").write_text(sums, encoding="utf-8", newline="\n")

        archive_output = output_directory / f"{PACKAGE_NAME}.tar.gz"
        _add_tree_deterministically(staging, archive_output)

    archive_digest = output_directory / f"{PACKAGE_NAME}.tar.gz.sha256"
    archive_digest.write_text(
        f"{_sha256(archive_output)}  {archive_output.name}\n",
        encoding="utf-8",
        newline="\n",
    )
    return archive_output, archive_digest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rc1-archive", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    arguments = parser.parse_args()
    archive, digest = build(arguments.rc1_archive, arguments.output_dir)
    print(f"PACKAGE={archive}")
    print(f"PACKAGE_SHA256={_sha256(archive)}")
    print(f"DIGEST_FILE={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

