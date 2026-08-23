"""Depth-first graph traversal over an adjacency-list representation."""

from typing import Dict, List


def depth_first_search(graph: Dict[str, List[str]], source: str) -> List[str]:
    """Returns nodes visited by iterative depth-first traversal from ``source``.

    Complexity Analysis:
        Time Complexity: O(V + E) where V = Vertices, E = Edges.
        Space Complexity: O(V) for the visited set, stack, and traversal order.
    """
    if source not in graph:
        raise ValueError("Source key does not exist within the graph.")

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in graph:
                raise ValueError(f"Edge references undeclared node '{neighbor}'.")

    visited = set()
    stack = [source]
    order: List[str] = []

    while stack:
        current_node = stack.pop()
        if current_node in visited:
            continue
        visited.add(current_node)
        order.append(current_node)
        stack.extend(reversed(graph[current_node]))

    return order
