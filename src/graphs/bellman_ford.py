"""Graph exploration module resolving shortest paths across negative edge weight systems."""

from typing import Dict, List, Tuple, Union


def bellman_ford(
    graph: Dict[str, List[Tuple[str, Union[int, float]]]], source: str
) -> Tuple[Dict[str, float], Dict[str, Union[str, None]]]:
    """Finds shortest paths from a source to all nodes, tolerating negative edge weights.

    Complexity Analysis:
        Time Complexity: O(V * E) where V = Vertices, E = Edges.
        Space Complexity: O(V) tracking footprint for distance and predecessor maps.
    """
    # Guard clause ensuring source node visibility boundary
    if source not in graph:
        raise ValueError(f"Target initial seed key '{source}' does not exist.")

    # Distance map initialized to infinity for untracked locations
    distances: Dict[str, float] = {node: float("inf") for node in graph}
    distances[source] = 0.0

    # Backtracking infrastructure for rebuilding node pathways
    predecessors: Dict[str, Union[str, None]] = {node: None for node in graph}

    # Flatten the adjacency map into a discrete edge list for repeated relaxation passes
    edges: List[Tuple[str, str, Union[int, float]]] = [
        (node, neighbor, weight)
        for node, adjacency in graph.items()
        for neighbor, weight in adjacency
    ]

    # Relax every edge up to (V - 1) times; this guarantees convergence absent negative cycles
    for _ in range(len(graph) - 1):
        for node, neighbor, weight in edges:
            if distances[node] == float("inf"):
                continue

            distance = distances[node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = node

    # Final pass detects reachable negative-weight cycles that would loop infinitely
    for node, neighbor, weight in edges:
        if distances[node] == float("inf"):
            continue

        if distances[node] + weight < distances[neighbor]:
            raise ValueError(
                "Graph contains a negative-weight cycle; execution halted."
            )

    return distances, predecessors
