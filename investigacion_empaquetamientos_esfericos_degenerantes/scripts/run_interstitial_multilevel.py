"""Genera el estudio reproducible de intersticios, grafos y capas celulares."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.interstitial import (
    cyclic_tangent_ring_report,
    descartes_inner_curvature,
    descartes_reflection,
    octahedral_gap_ratio,
    regular_ring_gap_ratio,
    simplex_gap_ratio,
)
from spherepack.multilevel import (
    Cell,
    ProjectedSegment,
    all_matchings,
    architecture_report,
    projected_intersection_kind,
    star_refine,
)


def _fmt(value: float) -> str:
    return f"{value:.6f}"


def write_interstitial_svg(path: Path) -> None:
    width, height = 840, 290
    panels = ((3, 140.0), (4, 420.0), (6, 700.0))
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fbfaf7"/>',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#262626}.title{font-size:17px;font-weight:600}.small{font-size:13px}.outer{fill:#d8e8ff;stroke:#3567a8;stroke-width:2}.center{fill:#ffd77a;stroke:#9c6513;stroke-width:2}</style>',
        '<text x="420" y="25" text-anchor="middle" class="title">Centros intersticiales en anillos regulares</text>',
    ]
    display_outer = 34.0
    for n, cx in panels:
        ratio = regular_ring_gap_ratio(n)
        center_r = display_outer * ratio
        orbit = display_outer + center_r
        cy = 145.0
        for index in range(n):
            angle = -math.pi / 2.0 + 2.0 * math.pi * index / n
            x = cx + orbit * math.cos(angle)
            y = cy + orbit * math.sin(angle)
            parts.append(f'<circle class="outer" cx="{x:.3f}" cy="{y:.3f}" r="{display_outer:.3f}"/>')
        parts.append(f'<circle class="center" cx="{cx:.3f}" cy="{cy:.3f}" r="{center_r:.3f}"/>')
        parts.append(f'<text x="{cx}" y="245" text-anchor="middle" class="title">n={n}</text>')
        parts.append(f'<text x="{cx}" y="266" text-anchor="middle" class="small">r/R={_fmt(ratio)}</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts) + "\n", encoding="utf-8", newline="\n")


def _triangle_positions(cx: float, cy: float, radius: float, rotation: float) -> list[tuple[float, float]]:
    return [
        (
            cx + radius * math.cos(rotation + 2.0 * math.pi * index / 3.0),
            cy + radius * math.sin(rotation + 2.0 * math.pi * index / 3.0),
        )
        for index in range(3)
    ]


def write_architecture_svg(path: Path) -> None:
    width, height = 920, 430
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fbfaf7"/>',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#262626}.title{font-size:18px;font-weight:600}.small{font-size:13px}.h{stroke:#2266aa}.a{stroke:#c46920}.m{stroke:#2d8a4b}.x{stroke:#8a43a8}.edge{fill:none;stroke-width:3}.nodeh{fill:#b9dbff;stroke:#2266aa;stroke-width:2}.nodea{fill:#ffd0a8;stroke:#c46920;stroke-width:2}</style>',
        '<text x="460" y="28" text-anchor="middle" class="title">Dos C3 tipados sobre los mismos seis vertices</text>',
    ]
    architecture = architecture_report((0, 1, 2))
    matching = {tuple(item) for item in architecture["matching"]}
    cross = {tuple(item) for item in architecture["cross_cycle"]}
    for panel_index, (label, cross_edges) in enumerate((('Prisma: matching M', matching), ('Octaedro: K3,3 \\ M', cross))):
        cx = 235.0 + panel_index * 450.0
        cy = 220.0
        h_positions = _triangle_positions(cx, cy, 128.0, -math.pi / 2.0)
        a_positions = _triangle_positions(cx, cy, 70.0, math.pi / 2.0)
        positions = {**{f'H{i}': h_positions[i] for i in range(3)}, **{f'A{i}': a_positions[i] for i in range(3)}}
        for prefix, css in (('H', 'h'), ('A', 'a')):
            nodes = [f'{prefix}{i}' for i in range(3)]
            for left, right in ((0, 1), (1, 2), (2, 0)):
                x1, y1 = positions[nodes[left]]
                x2, y2 = positions[nodes[right]]
                parts.append(f'<line class="edge {css}" x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"/>')
        css = 'm' if panel_index == 0 else 'x'
        for left, right in sorted(cross_edges):
            x1, y1 = positions[left]
            x2, y2 = positions[right]
            parts.append(f'<line class="edge {css}" x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" opacity="0.83"/>')
        for node, (x, y) in positions.items():
            css_node = 'nodeh' if node.startswith('H') else 'nodea'
            parts.append(f'<circle class="{css_node}" cx="{x:.2f}" cy="{y:.2f}" r="17"/>')
            parts.append(f'<text x="{x:.2f}" y="{y + 5:.2f}" text-anchor="middle" class="small">{node}</text>')
        parts.append(f'<text x="{cx}" y="395" text-anchor="middle" class="title">{label}</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts) + "\n", encoding="utf-8", newline="\n")


def write_refinement_svg(path: Path) -> None:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="880" height="330" viewBox="0 0 880 330">',
        '<rect width="100%" height="100%" fill="#fbfaf7"/>',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#262626}.title{font-size:18px;font-weight:600}.small{font-size:13px}.parent{fill:#edf3f8;stroke:#3e6078;stroke-width:3}.child{fill:none;stroke:#ca6b2b;stroke-width:2}.center{fill:#ffd77a;stroke:#9c6513;stroke-width:2}</style>',
        '<text x="440" y="26" text-anchor="middle" class="title">La celda padre y sus triangulos hijos viven en niveles distintos</text>',
        '<polygon class="parent" points="80,245 200,65 320,245"/>',
        '<line class="child" x1="200" y1="175" x2="80" y2="245"/><line class="child" x1="200" y1="175" x2="200" y2="65"/><line class="child" x1="200" y1="175" x2="320" y2="245"/>',
        '<circle class="center" cx="200" cy="175" r="12"/>',
        '<text x="200" y="292" text-anchor="middle" class="small">F3 nivel l -> 3 F3 nivel l+1</text>',
        '<polygon class="parent" points="520,70 750,70 750,250 520,250"/>',
        '<line class="child" x1="635" y1="160" x2="520" y2="70"/><line class="child" x1="635" y1="160" x2="750" y2="70"/><line class="child" x1="635" y1="160" x2="750" y2="250"/><line class="child" x1="635" y1="160" x2="520" y2="250"/>',
        '<circle class="center" cx="635" cy="160" r="12"/>',
        '<text x="635" y="292" text-anchor="middle" class="small">F4 nivel l -> 4 F3 nivel l+1</text>',
        '</svg>',
    ]
    path.write_text("\n".join(parts) + "\n", encoding="utf-8", newline="\n")


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "segoeuib.ttf" if bold else "segoeui.ttf"
    candidate = Path("C:/Windows/Fonts") / filename
    if candidate.exists():
        return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def _centered_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    value: str,
    font: ImageFont.ImageFont,
    fill: str = "#262626",
) -> None:
    box = draw.textbbox((0, 0), value, font=font)
    width = box[2] - box[0]
    height = box[3] - box[1]
    draw.text((xy[0] - width / 2, xy[1] - height / 2), value, font=font, fill=fill)


def write_summary_png(path: Path) -> None:
    """Resumen raster legible en telefono; los datos siguen viniendo del JSON."""

    image = Image.new("RGB", (1500, 980), "#fbfaf7")
    draw = ImageDraw.Draw(image)
    title = _font(38, bold=True)
    subtitle = _font(27, bold=True)
    regular = _font(22)
    small = _font(18)
    _centered_text(draw, (750, 46), "Intersticios y dos capas tipadas", title)

    display_outer = 48.0
    for n, cx in ((3, 260.0), (4, 750.0), (6, 1240.0)):
        ratio = regular_ring_gap_ratio(n)
        center_r = display_outer * ratio
        orbit = display_outer + center_r
        cy = 250.0
        for index in range(n):
            angle = -math.pi / 2.0 + 2.0 * math.pi * index / n
            x = cx + orbit * math.cos(angle)
            y = cy + orbit * math.sin(angle)
            draw.ellipse(
                (x - display_outer, y - display_outer, x + display_outer, y + display_outer),
                fill="#d8e8ff",
                outline="#3567a8",
                width=4,
            )
        draw.ellipse(
            (cx - center_r, cy - center_r, cx + center_r, cy + center_r),
            fill="#ffd77a",
            outline="#9c6513",
            width=4,
        )
        _centered_text(draw, (cx, 390), f"n={n}   r/R={_fmt(ratio)}", subtitle)

    _centered_text(draw, (750, 455), "Prisma y octaedro: mismo soporte, distinto tipo de enlace", subtitle)
    report = architecture_report((0, 1, 2))
    matching = {tuple(item) for item in report["matching"]}
    cross = {tuple(item) for item in report["cross_cycle"]}
    for panel, (label, active, color) in enumerate(
        (
            ("Prisma: M", matching, "#2d8a4b"),
            ("Octaedro: K3,3 \\ M = C6", cross, "#8a43a8"),
        )
    ):
        cx = 385.0 + panel * 730.0
        cy = 685.0
        h_positions = _triangle_positions(cx, cy, 170.0, -math.pi / 2.0)
        a_positions = _triangle_positions(cx, cy, 92.0, math.pi / 2.0)
        positions = {
            **{f"H{i}": h_positions[i] for i in range(3)},
            **{f"A{i}": a_positions[i] for i in range(3)},
        }
        for prefix, edge_color in (("H", "#2266aa"), ("A", "#c46920")):
            nodes = [f"{prefix}{index}" for index in range(3)]
            for left, right in ((0, 1), (1, 2), (2, 0)):
                draw.line((positions[nodes[left]], positions[nodes[right]]), fill=edge_color, width=6)
        for left, right in sorted(active):
            draw.line((positions[left], positions[right]), fill=color, width=5)
        for node, (x, y) in positions.items():
            fill = "#b9dbff" if node.startswith("H") else "#ffd0a8"
            outline = "#2266aa" if node.startswith("H") else "#c46920"
            draw.ellipse((x - 23, y - 23, x + 23, y + 23), fill=fill, outline=outline, width=4)
            _centered_text(draw, (x, y), node, small)
        _centered_text(draw, (cx, 910), label, subtitle)

    _centered_text(
        draw,
        (750, 953),
        "El centro de una celda padre se vuelve vertice de sus celdas hijas.",
        regular,
    )
    image.save(path, format="PNG", optimize=True)


def main() -> None:
    rings = []
    for n in range(3, 9):
        ratio = regular_ring_gap_ratio(n)
        rings.append(
            {
                "n": n,
                "center_to_outer_ratio": ratio,
                "contact_graph": "K4" if n == 3 else f"C{n}_join_K1",
                "center_is_smaller_than_outer": ratio < 1.0 - 1e-12,
            }
        )

    b_inner = descartes_inner_curvature((1.0, 1.0, 1.0))
    descendants = [
        {
            "replaced_index": index,
            "curvatures": list(descartes_reflection((1.0, 1.0, 1.0, b_inner), index)),
        }
        for index in range(3)
    ]

    triangle_refinement = star_refine(Cell("f3_parent", 0, ("a", "b", "c")), "g3")
    square_refinement = star_refine(Cell("f4_parent", 0, ("a", "b", "c", "d")), "g4")
    crossing = projected_intersection_kind(
        ProjectedSegment("t", "triangular", "t0", "t1", (-1.0, -1.0), (1.0, 1.0)),
        ProjectedSegment("q", "quadrangular", "q0", "q1", (-1.0, 1.0), (1.0, -1.0)),
    )

    payload = {
        "epistemic_status": "RESULTADO_COMPUTADO",
        "epistemic_scope": "familias geometricas y grafos tipados declarados en este paquete",
        "regular_ring_family": rings,
        "unequal_ring_example": cyclic_tangent_ring_report((1.0, 0.6, 1.4, 0.8)),
        "simplex_gap_ratios": {str(dimension): simplex_gap_ratio(dimension) for dimension in range(2, 6)},
        "octahedral_gap_ratio": octahedral_gap_ratio(),
        "descartes_seed": {
            "outer_curvatures": [1.0, 1.0, 1.0],
            "inner_curvature": b_inner,
            "inner_radius": 1.0 / b_inner,
            "first_reflections_replacing_outer_circle": descendants,
        },
        "six_matchings": [architecture_report(permutation) for permutation in all_matchings()],
        "cell_refinements": {
            "triangle": {
                "parent": triangle_refinement.parent.__dict__,
                "center": triangle_refinement.center,
                "children": [child.__dict__ for child in triangle_refinement.children],
                "roles": triangle_refinement.roles,
            },
            "square": {
                "parent": square_refinement.parent.__dict__,
                "center": square_refinement.center,
                "children": [child.__dict__ for child in square_refinement.children],
                "roles": square_refinement.roles,
            },
        },
        "typed_overlay_example": {"intersection_kind": crossing},
    }

    data_dir = PROJECT / "data"
    viz_dir = PROJECT / "visualizations"
    data_dir.mkdir(exist_ok=True)
    viz_dir.mkdir(exist_ok=True)
    (data_dir / "results_interstitial_multilevel.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_interstitial_svg(viz_dir / "interstitial_regular_rings.svg")
    write_architecture_svg(viz_dir / "prism_octahedron_typed.svg")
    write_refinement_svg(viz_dir / "cell_refinement_levels.svg")
    write_summary_png(viz_dir / "resumen_interstitial_multinivel.png")
    print("RESULTADO_COMPUTADO: 6 anillos, 6 matchings, 2 refinamientos, 1 cruce tipado, 3 SVG y 1 PNG.")


if __name__ == "__main__":
    main()
