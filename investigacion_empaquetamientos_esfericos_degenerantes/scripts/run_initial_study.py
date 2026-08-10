"""Ejecuta el estudio finito inicial y escribe solamente artefactos del proyecto."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.configurations import named_configurations
from spherepack.geometry import configuration_report
from spherepack.lattices import lattice_catalog
from spherepack.transitions import transition_report
from spherepack.visualization import write_interactive_html, write_shell_svg


def main() -> None:
    configurations = named_configurations()
    reports = [configuration_report(name, directions) for name, directions in configurations.items()]
    transitions = [
        transition_report("n2_antipodal", configurations["n2_antipodal"], "n4_square_transition_witness", configurations["n4_square_transition_witness"]),
        transition_report("n4_square_transition_witness", configurations["n4_square_transition_witness"], "n6_octahedron", configurations["n6_octahedron"]),
        transition_report("n4_tetrahedron", configurations["n4_tetrahedron"], "n6_octahedron", configurations["n6_octahedron"]),
        transition_report("n6_octahedron", configurations["n6_octahedron"], "n12_cuboctahedron_fcc_shell", configurations["n12_cuboctahedron_fcc_shell"]),
    ]
    payload = {
        "epistemic_status": "RESULTADO_COMPUTADO",
        "model_scope": "finite_named_configurations_only",
        "configuration_reports": reports,
        "transition_reports": transitions,
        "lattice_catalog": lattice_catalog(),
    }
    data_dir = PROJECT / "data"
    data_dir.mkdir(exist_ok=True)
    (data_dir / "results_initial.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    fields = ["name", "n", "minimum_unit_chord", "epsilon_infimum", "contact_pair_count_at_infimum", "affine_rank", "centeredness_claim"]
    with (data_dir / "results_initial.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows([{field: report[field] for field in fields} for report in reports])
    viz_dir = PROJECT / "visualizations"
    for name in ("n6_octahedron", "n12_cuboctahedron_fcc_shell", "n12_hcp_shell"):
        write_shell_svg(viz_dir / f"{name}.svg", name, configurations[name])
    write_interactive_html(
        viz_dir / "shells_3d_local.html",
        "Capas locales FCC y HCP",
        {name: configurations[name] for name in ("n6_octahedron", "n12_cuboctahedron_fcc_shell", "n12_hcp_shell")},
    )
    print("RESULTADO_COMPUTADO: 7 configuraciones, 4 consultas de transicion, 3 SVG, visor 3D local, CSV y JSON.")


if __name__ == "__main__":
    main()
