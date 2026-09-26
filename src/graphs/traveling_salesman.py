"""Traveling Salesman Problem solvers for weighted undirected complete graphs."""

from typing import Dict, List, Optional, Tuple

from src.graphs.kruskal import Edge, Weight

MAX_HELD_KARP_VERTICES = 12


def _build_distance_matrix(
    vertices: List[str], edges: List[Edge]
) -> List[List[Weight]]:
    """Validates input and returns a symmetric distance matrix indexed by vertex order."""
    if not vertices:
        raise ValueError("Graph must contain at least one vertex.")
    if len(set(vertices)) != len(vertices):
        raise ValueError("Graph vertices must be unique.")

    index: Dict[str, int] = {vertex: i for i, vertex in enumerate(vertices)}
    size = len(vertices)
    matrix: List[List[Optional[Weight]]] = [[None] * size for _ in range(size)]

    for edge in edges:
        if len(edge) != 3:
            raise ValueError("Every edge must contain two vertices and a weight.")
        first, second, weight = edge
        if first not in index or second not in index:
            raise ValueError("Edge references an undeclared vertex.")
        if first == second:
            raise ValueError("Self-loop edges are not allowed.")
        if not isinstance(weight, (int, float)) or isinstance(weight, bool):
            raise ValueError("Edge weights must be numeric.")
        if weight < 0:
            raise ValueError("Edge weights must be non-negative.")
        i, j = index[first], index[second]
        # Keep the cheapest edge when duplicates are supplied.
        if matrix[i][j] is None or weight < matrix[i][j]:
            matrix[i][j] = matrix[j][i] = weight

    for i in range(size):
        matrix[i][i] = 0
        for j in range(size):
            if matrix[i][j] is None:
                raise ValueError(
                    "Graph is not complete; every pair of vertices needs an edge."
                )

    return matrix  # type: ignore[return-value]


def _resolve_start(vertices: List[str], start: Optional[str]) -> int:
    if start is None:
        return 0
    if start not in vertices:
        raise ValueError("Start vertex must be one of the declared vertices.")
    return vertices.index(start)


def _tour_cost(tour: List[int], matrix: List[List[Weight]]) -> Weight:
    return sum(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))


def held_karp(
    vertices: List[str], edges: List[Edge], start: Optional[str] = None
) -> Tuple[List[str], Weight]:
    """Returns an optimal closed tour and its total weight via bitmask dynamic programming.

    The tour begins and ends at `start` (defaults to the first vertex).

    Complexity Analysis:
        Time Complexity: O(n^2 * 2^n) where n = Vertices.
        Space Complexity: O(n * 2^n) for the subset-cost table.
    """
    if len(vertices) > MAX_HELD_KARP_VERTICES:
        raise ValueError(
            f"Held-Karp supports at most {MAX_HELD_KARP_VERTICES} vertices; "
            "use the nearest-neighbor 2-opt heuristic for larger graphs."
        )
    matrix = _build_distance_matrix(vertices, edges)
    origin = _resolve_start(vertices, start)
    size = len(vertices)

    if size == 1:
        return [vertices[0]], 0

    # Reorder so the origin is index 0; `others` maps DP bit positions to matrix indices.
    others = [i for i in range(size) if i != origin]
    count = len(others)
    full_mask = (1 << count) - 1

    cost: List[Dict[int, Weight]] = [dict() for _ in range(1 << count)]
    parent: List[Dict[int, int]] = [dict() for _ in range(1 << count)]
    for bit in range(count):
        cost[1 << bit][bit] = matrix[origin][others[bit]]

    for mask in range(1, full_mask + 1):
        for last, last_cost in cost[mask].items():
            for nxt in range(count):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                candidate = last_cost + matrix[others[last]][others[nxt]]
                if nxt not in cost[new_mask] or candidate < cost[new_mask][nxt]:
                    cost[new_mask][nxt] = candidate
                    parent[new_mask][nxt] = last

    best_last = min(
        range(count),
        key=lambda bit: (cost[full_mask][bit] + matrix[others[bit]][origin], bit),
    )
    best_cost = cost[full_mask][best_last] + matrix[others[best_last]][origin]

    order: List[int] = []
    mask, bit = full_mask, best_last
    while True:
        order.append(others[bit])
        if mask == (1 << bit):
            break
        mask, bit = mask ^ (1 << bit), parent[mask][bit]
    order.reverse()

    tour = [origin] + order + [origin]
    return [vertices[i] for i in tour], best_cost


def nearest_neighbor_two_opt(
    vertices: List[str], edges: List[Edge], start: Optional[str] = None
) -> Tuple[List[str], Weight]:
    """Returns an approximate closed tour using nearest-neighbor construction and 2-opt.

    The tour begins and ends at `start` (defaults to the first vertex). The result
    is not guaranteed optimal but is typically close on metric instances.

    Complexity Analysis:
        Time Complexity: O(n^2) construction plus O(n^2) per 2-opt improvement pass.
        Space Complexity: O(n^2) for the distance matrix.
    """
    matrix = _build_distance_matrix(vertices, edges)
    origin = _resolve_start(vertices, start)
    size = len(vertices)

    if size == 1:
        return [vertices[0]], 0

    tour = [origin]
    unvisited = [i for i in range(size) if i != origin]
    while unvisited:
        current = tour[-1]
        nearest = min(unvisited, key=lambda node: (matrix[current][node], node))
        tour.append(nearest)
        unvisited.remove(nearest)
    tour.append(origin)

    improved = True
    while improved:
        improved = False
        for i in range(1, size - 1):
            for j in range(i + 1, size):
                a, b = tour[i - 1], tour[i]
                c, d = tour[j], tour[j + 1]
                delta = (matrix[a][c] + matrix[b][d]) - (matrix[a][b] + matrix[c][d])
                if delta < 0:
                    tour[i : j + 1] = reversed(tour[i : j + 1])
                    improved = True

    return [vertices[i] for i in tour], _tour_cost(tour, matrix)
