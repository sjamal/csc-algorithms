"""Dependency ordering module resolving directed acyclic graph sequencing via in-degree tracking."""

from collections import deque
from typing import Dict, List


def topological_sort(graph: Dict[str, List[str]]) -> List[str]:
    """Orders nodes such that every directed edge points from an earlier to a later node.

    Complexity Analysis:
        Time Complexity: O(V + E) where V = Vertices, E = Edges.
        Space Complexity: O(V) tracking footprint for in-degree counts and the BFS queue.
    """
    # In-degree map initialized to zero for every node, then tallied across all edges
    in_degrees: Dict[str, int] = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            # Guard clause against edges referencing undeclared destination nodes
            if neighbor not in in_degrees:
                raise ValueError(f"Edge references undeclared node '{neighbor}'.")
            in_degrees[neighbor] += 1

    # Seed the BFS frontier with every node that has no incoming dependency edges
    queue: deque = deque(node for node, degree in in_degrees.items() if degree == 0)
    order: List[str] = []

    while queue:
        current_node = queue.popleft()
        order.append(current_node)

        # Peeling this node away reduces the in-degree of each of its dependents
        for neighbor in graph[current_node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    # A shorter-than-total order means a cycle prevented some nodes from ever reaching zero
    if len(order) != len(graph):
        raise ValueError("Graph contains a cycle; topological order does not exist.")

    return order
