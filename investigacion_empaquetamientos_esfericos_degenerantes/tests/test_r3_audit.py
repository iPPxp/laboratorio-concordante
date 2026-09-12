import csv
import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.r3_audit import audit_r3_bundle, enumerate_r3_cycle_geometry


def fixture_rows():
    rows = []
    for cycle_id, item in enumerate(enumerate_r3_cycle_geometry(), start=1):
        rows.append(
            {
                "cycle_id": str(cycle_id),
                "vertices_barycentric_integer": repr(item["vertices"]),
                "collinear_vertices": str(item["collinear_vertices"]),
                "six_geometric_corners": str(item["six_geometric_corners"]),
                "convex": str(item["convex"]),
                "regular": str(item["regular"]),
            }
        )
    return rows


def write_bundle(path, rows):
    counts = {
        "abstract_C6_cycles": len(rows),
        "six_corner_cycles": sum(row["six_geometric_corners"] == "True" for row in rows),
        "convex_six_corner_cycles": sum(row["convex"] == "True" for row in rows),
        "regular_hexagons": sum(row["regular"] == "True" for row in rows),
    }
    summary = (
        "R_n,abstract_C6_cycles,six_corner_cycles,convex_six_corner_cycles,regular_hexagons\n"
        f"3,{counts['abstract_C6_cycles']},{counts['six_corner_cycles']},"
        f"{counts['convex_six_corner_cycles']},{counts['regular_hexagons']}\n"
    )
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=rows[0].keys(), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    readme = "R3_CANONICAL_CENTRAL_HEXAGON_COUNT=1\nun solo hexágono regular central canónico\n"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("root/R3_exact_experiment/R1_R5_summary.csv", summary)
        archive.writestr("root/R3_exact_experiment/R3_C6_cycles.csv", stream.getvalue())
        archive.writestr("root/README_MASTER_RESULTS.md", readme)


class R3AuditTests(unittest.TestCase):
    def test_recomputes_cycles_and_geometry_from_bundle(self):
        rows = fixture_rows()
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory) / "bundle.zip"
            write_bundle(bundle, rows)
            report = audit_r3_bundle(bundle)
        self.assertTrue(report["cycle_set_matches_csv"])
        self.assertTrue(report["geometry_flags_match_csv"])
        self.assertTrue(report["csv_counts_consistent"])
        self.assertTrue(report["readme_declares_one_canonical_central_hexagon"])
        self.assertEqual(report["r3_recomputed"]["abstract_C6_cycles"], 16)
        self.assertEqual(report["r3_recomputed"]["regular_hexagons"], 1)

    def test_detects_a_tampered_geometry_flag(self):
        rows = fixture_rows()
        rows[0]["regular"] = "True" if rows[0]["regular"] == "False" else "False"
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory) / "bundle.zip"
            write_bundle(bundle, rows)
            report = audit_r3_bundle(bundle)
        self.assertFalse(report["geometry_flags_match_csv"])
        self.assertFalse(report["csv_counts_consistent"])
        self.assertEqual(report["geometry_flag_mismatches"][0]["cycle_id"], 1)


if __name__ == "__main__":
    unittest.main()
