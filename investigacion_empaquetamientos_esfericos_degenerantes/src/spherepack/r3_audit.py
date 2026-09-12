"""Auditoria reproducible de ciclos C6 y geometria del reticulado R3."""

from __future__ import annotations

import ast
import csv
import hashlib
import io
import zipfile
from itertools import product
from pathlib import Path
from typing import Iterable

SUMMARY_SUFFIX = "R3_exact_experiment/R1_R5_summary.csv"
CYCLES_SUFFIX = "R3_exact_experiment/R3_C6_cycles.csv"
README_SUFFIX = "README_MASTER_RESULTS.md"

Barycentric = tuple[int, int, int]
Cycle = tuple[Barycentric, ...]


def _unique_entry(names: list[str], suffix: str) -> str:
    matches = [name for name in names if name.endswith(suffix)]
    if len(matches) != 1:
        raise ValueError(f"Se esperaba una entrada terminada en {suffix!r}; encontradas: {matches}")
    return matches[0]


def _boolean(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError(f"Valor booleano inesperado: {value!r}")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _r3_vertices(level: int = 3) -> tuple[Barycentric, ...]:
    return tuple(
        sorted(
            (a, b, c)
            for a, b, c in product(range(level + 1), repeat=3)
            if a + b + c == level
        )
    )


def _adjacent(left: Barycentric, right: Barycentric) -> bool:
    return sum(abs(a - b) for a, b in zip(left, right, strict=True)) == 2


def _canonical_cycle(vertices: Iterable[Barycentric]) -> Cycle:
    cycle = tuple(vertices)
    rotations = [cycle[index:] + cycle[:index] for index in range(len(cycle))]
    reverse = tuple(reversed(cycle))
    rotations.extend(reverse[index:] + reverse[:index] for index in range(len(cycle)))
    return min(rotations)


def _enumerate_r3_c6(level: int = 3) -> tuple[Cycle, ...]:
    vertices = _r3_vertices(level)
    neighbours = {
        vertex: tuple(other for other in vertices if other != vertex and _adjacent(vertex, other))
        for vertex in vertices
    }
    cycles: set[Cycle] = set()

    def extend(path: tuple[Barycentric, ...]) -> None:
        if len(path) == 6:
            if path[0] in neighbours[path[-1]]:
                cycles.add(_canonical_cycle(path))
            return
        for candidate in neighbours[path[-1]]:
            if candidate not in path:
                extend(path + (candidate,))

    for start in vertices:
        extend((start,))
    return tuple(sorted(cycles))


def _xy_integer(point: Barycentric) -> tuple[int, int]:
    """Coordenadas afines: la metrica euclidea escalada es dx^2+3dy^2."""

    _, b, c = point
    return 2 * b + c, c


def _orientation(
    left: tuple[int, int], middle: tuple[int, int], right: tuple[int, int]
) -> int:
    return (
        (middle[0] - left[0]) * (right[1] - left[1])
        - (middle[1] - left[1]) * (right[0] - left[0])
    )


def _cycle_geometry(cycle: Cycle) -> dict[str, object]:
    points = tuple(_xy_integer(point) for point in cycle)
    turns = tuple(
        _orientation(points[index - 1], points[index], points[(index + 1) % 6])
        for index in range(6)
    )
    collinear = sum(turn == 0 for turn in turns)
    nonzero_signs = {1 if turn > 0 else -1 for turn in turns if turn != 0}
    convex = collinear == 0 and len(nonzero_signs) == 1

    side_squared: list[int] = []
    angle_dot: list[int] = []
    for index in range(6):
        current = points[index]
        following = points[(index + 1) % 6]
        previous = points[index - 1]
        dx, dy = following[0] - current[0], following[1] - current[1]
        side_squared.append(dx * dx + 3 * dy * dy)
        in_x, in_y = previous[0] - current[0], previous[1] - current[1]
        out_x, out_y = following[0] - current[0], following[1] - current[1]
        angle_dot.append(in_x * out_x + 3 * in_y * out_y)

    regular = convex and len(set(side_squared)) == 1 and len(set(angle_dot)) == 1
    return {
        "vertices": cycle,
        "collinear_vertices": collinear,
        "six_geometric_corners": collinear == 0,
        "convex": convex,
        "regular": regular,
        "side_squared_scaled": side_squared,
        "angle_dot_scaled": angle_dot,
    }


def enumerate_r3_cycle_geometry() -> tuple[dict[str, object], ...]:
    """Enumera los C6 de la malla triangular R3 y deriva sus predicados."""

    return tuple(_cycle_geometry(cycle) for cycle in _enumerate_r3_c6(3))


def _parse_cycle(value: str) -> Cycle:
    parsed = ast.literal_eval(value)
    if not isinstance(parsed, tuple) or len(parsed) != 6:
        raise ValueError(f"Ciclo baricentrico inesperado: {value!r}")
    cycle = tuple(tuple(int(coordinate) for coordinate in point) for point in parsed)
    if any(len(point) != 3 or sum(point) != 3 or min(point) < 0 for point in cycle):
        raise ValueError(f"Vertice R3 inesperado: {value!r}")
    if len(set(cycle)) != 6:
        raise ValueError(f"El ciclo repite vertices: {value!r}")
    return _canonical_cycle(cycle)  # type: ignore[arg-type]


def audit_r3_bundle(bundle_path: str | Path) -> dict[str, object]:
    path = Path(bundle_path).resolve()
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        summary_entry = _unique_entry(names, SUMMARY_SUFFIX)
        cycles_entry = _unique_entry(names, CYCLES_SUFFIX)
        readme_entry = _unique_entry(names, README_SUFFIX)
        summary_text = archive.read(summary_entry).decode("utf-8-sig")
        cycles_text = archive.read(cycles_entry).decode("utf-8-sig")
        readme_text = archive.read(readme_entry).decode("utf-8-sig")

    summary_rows = list(csv.DictReader(io.StringIO(summary_text)))
    r3_rows = [row for row in summary_rows if row["R_n"] == "3"]
    if len(r3_rows) != 1:
        raise ValueError("R1_R5_summary.csv debe contener exactamente una fila R_n=3.")
    summary = r3_rows[0]
    csv_cycles = list(csv.DictReader(io.StringIO(cycles_text)))

    geometry = enumerate_r3_cycle_geometry()
    by_cycle = {item["vertices"]: item for item in geometry}
    parsed_rows: list[tuple[dict[str, str], Cycle]] = [
        (row, _parse_cycle(row["vertices_barycentric_integer"])) for row in csv_cycles
    ]
    csv_cycle_set = {cycle for _, cycle in parsed_rows}
    generated_cycle_set = set(by_cycle)

    mismatches: list[dict[str, object]] = []
    regular_cycle_ids: list[int] = []
    for row, cycle in parsed_rows:
        computed_row = by_cycle.get(cycle)
        if computed_row is None:
            mismatches.append({"cycle_id": int(row["cycle_id"]), "reason": "CICLO_NO_GENERADO"})
            continue
        differences: dict[str, object] = {}
        declared_values: dict[str, object] = {
            "collinear_vertices": int(row["collinear_vertices"]),
            "six_geometric_corners": _boolean(row["six_geometric_corners"]),
            "convex": _boolean(row["convex"]),
            "regular": _boolean(row["regular"]),
        }
        for key, declared_value in declared_values.items():
            if declared_value != computed_row[key]:
                differences[key] = {
                    "declared": declared_value,
                    "recomputed": computed_row[key],
                }
        if differences:
            mismatches.append({"cycle_id": int(row["cycle_id"]), "differences": differences})
        if computed_row["regular"]:
            regular_cycle_ids.append(int(row["cycle_id"]))

    recomputed = {
        "abstract_C6_cycles": len(geometry),
        "six_corner_cycles": sum(bool(item["six_geometric_corners"]) for item in geometry),
        "convex_six_corner_cycles": sum(bool(item["convex"]) for item in geometry),
        "regular_hexagons": sum(bool(item["regular"]) for item in geometry),
        "regular_cycle_ids": regular_cycle_ids,
    }
    declared = {
        key: int(summary[key])
        for key in (
            "abstract_C6_cycles",
            "six_corner_cycles",
            "convex_six_corner_cycles",
            "regular_hexagons",
        )
    }
    comparable_recomputed = {key: recomputed[key] for key in declared}
    cycle_set_matches = csv_cycle_set == generated_cycle_set and len(csv_cycles) == len(csv_cycle_set)
    geometry_matches = not mismatches
    return {
        "bundle_name": path.name,
        "bundle_sha256": _sha256(path),
        "entries": {
            "summary": summary_entry,
            "cycles": cycles_entry,
            "readme": readme_entry,
        },
        "r3_declared": declared,
        "r3_recomputed": recomputed,
        "cycle_set_matches_csv": cycle_set_matches,
        "geometry_flags_match_csv": geometry_matches,
        "geometry_flag_mismatches": mismatches,
        "csv_counts_consistent": comparable_recomputed == declared and cycle_set_matches and geometry_matches,
        "readme_declares_one_canonical_central_hexagon": (
            "R3_CANONICAL_CENTRAL_HEXAGON_COUNT=1" in readme_text
            and "un solo hexágono regular central canónico" in readme_text
        ),
    }
