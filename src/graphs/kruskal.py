"""Kruskal minimum spanning tree construction for weighted undirected graphs."""

from typing import List, Tuple, Union

from src.data_structures.union_find import UnionFind

Weight = Union[int, float]
Edge = Tuple[str, str, Weight]


def kruskal(vertices: List[str], edges: List[Edge]) -> Tuple[List[Edge], Weight]:
    """Returns the minimum spanning tree edges and their total weight.

    Complexity Analysis:
        Time Complexity: O(E log E) where E = Edges, including edge sorting.
        Space Complexity: O(V + E) for Union-Find state and sorted edge storage.
    """
    if not vertices:
        raise ValueError("Graph must contain at least one vertex.")
    if len(set(vertices)) != len(vertices):
        raise ValueError("Graph vertices must be unique.")

    vertex_set = set(vertices)
    validated_edges: List[Edge] = []
    for edge in edges:
        if len(edge) != 3:
            raise ValueError("Every edge must contain two vertices and a weight.")
        first, second, weight = edge
        if first not in vertex_set or second not in vertex_set:
            raise ValueError("Edge references an undeclared vertex.")
        if not isinstance(weight, (int, float)) or isinstance(weight, bool):
            raise ValueError("Edge weights must be numeric.")
        validated_edges.append((first, second, weight))

    union_find = UnionFind(vertices)
    selected_edges: List[Edge] = []
    total_weight: Weight = 0

    for first, second, weight in sorted(validated_edges, key=lambda edge: edge[2]):
        if union_find.union(first, second):
            selected_edges.append((first, second, weight))
            total_weight += weight

    if len(selected_edges) != len(vertices) - 1:
        raise ValueError("Graph is disconnected; minimum spanning tree does not exist.")

    return selected_edges, total_weight
