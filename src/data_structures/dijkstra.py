"""Graph exploration module managing weighted shortest path calculation mechanics."""

import heapq
from typing import Dict, List, Tuple, Union


def dijkstra(
    graph: Dict[str, List[Tuple[str, Union[int, float]]]], source: str
) -> Tuple[Dict[str, float], Dict[str, Union[str, None]]]:
    """Finds paths from a source to all available nodes using a Min-Priority Queue.

    Complexity Analysis:
        Time Complexity: O((V + E) * log V) where V = Vertices, E = Edges.
        Space Complexity: O(V + E) initialization footprint tracking.
    """
    # Guard clause ensuring source node visibility boundary
    if source not in graph:
        raise ValueError(f"Target initial seed key '{source}' does not exist.")

    # Distance map initialized to infinity for untracked locations
    distances: Dict[str, float] = {node: float("inf") for node in graph}
    distances[source] = 0.0

    # Backtracking infrastructure for rebuilding node pathways
    predecessors: Dict[str, Union[str, None]] = {node: None for node in graph}

    # Internal Priority Queue tracking structures: stores elements as (distance, vertex_name)
    priority_queue: List[Tuple[float, str]] = [(0.0, source)]

    while priority_queue:
        # Pull the vertex with the lowest calculated distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip stale entries (lazy deletion tracking strategy)
        if current_distance > distances[current_node]:
            continue

        # Evaluate adjacent node connections
        for neighbor, weight in graph[current_node]:
            # Guard clause against malicious or invalid negative edge injections
            if weight < 0:
                raise ValueError("Graph contains a negative weight; execution halted.")

            distance = current_distance + weight

            # Optimal node discovery progression
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors
