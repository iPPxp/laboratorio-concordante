"""Grafos tipados y refinamientos celulares para estructuras multinivel."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from math import hypot
from typing import Iterable, Mapping

Node = str
Edge = tuple[Node, Node]


def edge(left: Node, right: Node) -> Edge:
    if left == right:
        raise ValueError("Una arista simple no puede ser un lazo.")
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def complete_edges(nodes: Iterable[Node]) -> frozenset[Edge]:
    ordered = tuple(nodes)
    return frozenset(edge(left, right) for left, right in combinations(ordered, 2))


def triad_nodes(prefix: str) -> tuple[Node, Node, Node]:
    return tuple(f"{prefix}{index}" for index in range(3))  # type: ignore[return-value]


def triad_edges(prefix: str) -> frozenset[Edge]:
    return complete_edges(triad_nodes(prefix))


def matching_edges(permutation: tuple[int, int, int]) -> frozenset[Edge]:
    if tuple(sorted(permutation)) != (0, 1, 2):
        raise ValueError("La correspondencia debe ser una permutacion de (0,1,2).")
    return frozenset(edge(f"H{index}", f"A{permutation[index]}") for index in range(3))


def all_matchings() -> tuple[tuple[int, int, int], ...]:
    return tuple(permutations((0, 1, 2)))


def architecture_edges(permutation: tuple[int, int, int]) -> dict[str, frozenset[Edge]]:
    """Prisma y octaedro sobre las mismas dos ternas etiquetadas.

    El prisma usa el matching M. El octaedro usa las otras seis aristas
    cruzadas. Las dos ternas internas se conservan en ambos grafos.
    """

    h_nodes = triad_nodes("H")
    a_nodes = triad_nodes("A")
    internal = triad_edges("H") | triad_edges("A")
    all_cross = frozenset(edge(left, right) for left in h_nodes for right in a_nodes)
    matching = matching_edges(permutation)
    cross_cycle = all_cross - matching
    prism = internal | matching
    octahedron = internal | cross_cycle
    return {
        "internal_triads": internal,
        "matching": matching,
        "cross_cycle": cross_cycle,
        "prism": prism,
        "octahedron": octahedron,
    }


def degrees(nodes: Iterable[Node], edges: Iterable[Edge]) -> dict[Node, int]:
    result = {node: 0 for node in nodes}
    for left, right in edges:
        result[left] += 1
        result[right] += 1
    return result


def is_single_cycle(nodes: Iterable[Node], edges: Iterable[Edge]) -> bool:
    node_set = frozenset(nodes)
    edge_set = frozenset(edges)
    if len(edge_set) != len(node_set) or set(degrees(node_set, edge_set).values()) != {2}:
        return False
    if not node_set:
        return False
    seen: set[Node] = set()
    frontier = [next(iter(node_set))]
    while frontier:
        node = frontier.pop()
        if node in seen:
            continue
        seen.add(node)
        for left, right in edge_set:
            if left == node and right not in seen:
                frontier.append(right)
            elif right == node and left not in seen:
                frontier.append(left)
    return seen == set(node_set)


def simple_cycles_of_length(nodes: Iterable[Node], edges: Iterable[Edge], length: int) -> frozenset[tuple[Node, ...]]:
    """Enumera ciclos simples no orientados, modulo rotacion e inversion."""

    ordered_nodes = tuple(sorted(nodes))
    edge_set = frozenset(edges)
    if length < 3 or length > len(ordered_nodes):
        return frozenset()

    canonical: set[tuple[Node, ...]] = set()
    for sequence in permutations(ordered_nodes, length):
        if all(edge(sequence[index], sequence[(index + 1) % length]) in edge_set for index in range(length)):
            rotations = [sequence[index:] + sequence[:index] for index in range(length)]
            reverse = tuple(reversed(sequence))
            rotations.extend(reverse[index:] + reverse[:index] for index in range(length))
            canonical.add(min(rotations))
    return frozenset(canonical)


def graph_invariants(nodes: Iterable[Node], edges: Iterable[Edge]) -> dict[str, object]:
    node_set = frozenset(nodes)
    edge_set = frozenset(edges)
    seen: set[Node] = set()
    components = 0
    for start in node_set:
        if start in seen:
            continue
        components += 1
        frontier = [start]
        while frontier:
            node = frontier.pop()
            if node in seen:
                continue
            seen.add(node)
            for left, right in edge_set:
                if left == node and right not in seen:
                    frontier.append(right)
                elif right == node and left not in seen:
                    frontier.append(left)
    return {
        "vertices": len(node_set),
        "edges": len(edge_set),
        "components": components,
        "degree_multiset": sorted(degrees(node_set, edge_set).values()),
        "cycle_rank_beta1": len(edge_set) - len(node_set) + components,
        "simple_cycle_counts": {
            str(length): len(simple_cycles_of_length(node_set, edge_set, length))
            for length in range(3, len(node_set) + 1)
        },
    }


def architecture_report(permutation: tuple[int, int, int]) -> dict[str, object]:
    components = architecture_edges(permutation)
    nodes = triad_nodes("H") + triad_nodes("A")
    intersection = components["prism"] & components["octahedron"]
    union = components["prism"] | components["octahedron"]
    return {
        "permutation": list(permutation),
        "matching": sorted(components["matching"]),
        "cross_cycle": sorted(components["cross_cycle"]),
        "cross_cycle_is_C6": is_single_cycle(nodes, components["cross_cycle"]),
        "prism_edge_count": len(components["prism"]),
        "octahedron_edge_count": len(components["octahedron"]),
        "same_matching_intersection": sorted(intersection),
        "same_matching_union_is_K6": union == complete_edges(nodes),
        "prism_degrees": degrees(nodes, components["prism"]),
        "octahedron_degrees": degrees(nodes, components["octahedron"]),
        "prism_invariants": graph_invariants(nodes, components["prism"]),
        "octahedron_invariants": graph_invariants(nodes, components["octahedron"]),
        "cross_cycle_invariants": graph_invariants(nodes, components["cross_cycle"]),
    }


@dataclass(frozen=True)
class Cell:
    cell_id: str
    level: int
    boundary: tuple[Node, ...]

    def __post_init__(self) -> None:
        if self.level < 0:
            raise ValueError("level debe ser no negativo.")
        if len(self.boundary) < 3 or len(set(self.boundary)) != len(self.boundary):
            raise ValueError("La frontera debe contener al menos tres vertices distintos.")

    @property
    def kind(self) -> str:
        return f"F{len(self.boundary)}"


@dataclass(frozen=True)
class StarRefinement:
    parent: Cell
    center: Node
    children: tuple[Cell, ...]

    @property
    def roles(self) -> Mapping[int, tuple[str, ...]]:
        return {
            self.parent.level: ("CENTRO_DE_CELDA_PADRE",),
            self.parent.level + 1: ("VERTICE_DE_FRONTERA_DE_CELDAS_HIJAS",),
        }


def star_refine(parent: Cell, center: Node) -> StarRefinement:
    if center in parent.boundary:
        raise ValueError("El centro nuevo no puede ser un vertice previo de la frontera.")
    children = tuple(
        Cell(
            cell_id=f"{parent.cell_id}.{index}",
            level=parent.level + 1,
            boundary=(center, parent.boundary[index], parent.boundary[(index + 1) % len(parent.boundary)]),
        )
        for index in range(len(parent.boundary))
    )
    return StarRefinement(parent=parent, center=center, children=children)


def star_refinement_delta(boundary_size: int) -> tuple[int, int, int]:
    """Cambio (vertices, aristas, caras) al sustituir una k-celda por un hub."""

    if isinstance(boundary_size, bool) or not isinstance(boundary_size, int) or boundary_size < 3:
        raise ValueError("boundary_size debe ser un entero mayor o igual que 3.")
    return (1, boundary_size, boundary_size - 1)


@dataclass(frozen=True)
class ProjectedSegment:
    segment_id: str
    layer: str
    source: Node
    target: Node
    source_xy: tuple[float, float]
    target_xy: tuple[float, float]

    def __post_init__(self) -> None:
        if self.source == self.target:
            raise ValueError("Un segmento requiere extremos distintos.")


def _orientation_sign(
    a: tuple[float, float],
    b: tuple[float, float],
    c: tuple[float, float],
    tolerance: float,
) -> int:
    """Signo de orientacion con tolerancia angular relativa a la escala."""

    ab_x, ab_y = b[0] - a[0], b[1] - a[1]
    ac_x, ac_y = c[0] - a[0], c[1] - a[1]
    determinant = ab_x * ac_y - ab_y * ac_x
    scale = hypot(ab_x, ab_y) * hypot(ac_x, ac_y)
    if scale == 0.0 or abs(determinant) <= tolerance * scale:
        return 0
    return 1 if determinant > 0.0 else -1


def projected_intersection_kind(first: ProjectedSegment, second: ProjectedSegment, tolerance: float = 1e-12) -> str:
    """Distingue incidencia declarada de un cruce interior de proyeccion."""

    if tolerance < 0.0:
        raise ValueError("tolerance debe ser no negativa.")
    if {first.source, first.target} & {second.source, second.target}:
        return "VERTICE_COMPARTIDO"
    a, b = first.source_xy, first.target_xy
    c, d = second.source_xy, second.target_xy
    o1 = _orientation_sign(a, b, c, tolerance)
    o2 = _orientation_sign(a, b, d, tolerance)
    o3 = _orientation_sign(c, d, a, tolerance)
    o4 = _orientation_sign(c, d, b, tolerance)
    proper = (o1 * o2 < 0) and (o3 * o4 < 0)
    if proper:
        return "CRUCE_DE_PROYECCION_NO_VERTICE"
    if all(value == 0 for value in (o1, o2, o3, o4)):
        return "COLINEALIDAD_REQUIERE_TIPADO"
    return "SIN_INCIDENCIA"
