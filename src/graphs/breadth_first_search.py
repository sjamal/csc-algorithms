"""Breadth-first graph traversal over an adjacency-list representation."""

from collections import deque
from typing import Dict, List


def breadth_first_search(graph: Dict[str, List[str]], source: str) -> List[str]:
    """Returns nodes visited level by level from ``source``.

    Complexity Analysis:
        Time Complexity: O(V + E) where V = Vertices, E = Edges.
        Space Complexity: O(V) for the visited set, queue, and traversal order.
    """
    if source not in graph:
        raise ValueError("Source key does not exist within the graph.")

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in graph:
                raise ValueError(f"Edge references undeclared node '{neighbor}'.")

    visited = {source}
    queue = deque([source])
    order: List[str] = []

    while queue:
        current_node = queue.popleft()
        order.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
