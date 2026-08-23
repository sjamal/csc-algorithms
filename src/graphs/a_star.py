"""Graph exploration module resolving heuristic-driven shortest paths between two nodes."""

import heapq
import math
from typing import Dict, List, Tuple, Union


def _heuristic(
    positions: Dict[str, Tuple[float, float]], node: str, target: str
) -> float:
    """Estimates remaining travel cost using straight-line (Euclidean) distance."""
    node_x, node_y = positions[node]
    target_x, target_y = positions[target]
    return math.hypot(node_x - target_x, node_y - target_y)


def a_star(
    graph: Dict[str, List[Tuple[str, Union[int, float]]]],
    positions: Dict[str, Tuple[float, float]],
    source: str,
    target: str,
) -> Tuple[List[str], float]:
    """Finds the lowest-cost path between two nodes using heuristic-guided exploration.

    Complexity Analysis:
        Time Complexity: O((V + E) * log V) where V = Vertices, E = Edges.
        Space Complexity: O(V + E) initialization footprint tracking.
    """
    # Guard clause ensuring source and target node visibility boundary
    if source not in graph or target not in graph:
        raise ValueError("Source or target key does not exist within the graph.")

    # Guard clause ensuring every node carries spatial coordinates for heuristic scoring
    if source not in positions or target not in positions:
        raise ValueError("Source or target key is missing spatial coordinates.")

    # Cost-to-reach map initialized to infinity for untracked locations
    distances: Dict[str, float] = {node: float("inf") for node in graph}
    distances[source] = 0.0

    # Backtracking infrastructure for rebuilding node pathways
    predecessors: Dict[str, Union[str, None]] = {node: None for node in graph}

    # Internal Priority Queue tracking structures: stores elements as (f_score, vertex_name)
    priority_queue: List[Tuple[float, str]] = [
        (_heuristic(positions, source, target), source)
    ]
    visited: set = set()

    while priority_queue:
        # Pull the vertex with the lowest estimated total cost (g_score + heuristic)
        _, current_node = heapq.heappop(priority_queue)

        if current_node == target:
            break

        if current_node in visited:
            continue
        visited.add(current_node)

        # Evaluate adjacent node connections
        for neighbor, weight in graph[current_node]:
            # Guard clause against malicious or invalid negative edge injections
            if weight < 0:
                raise ValueError("Graph contains a negative weight; execution halted.")

            distance = distances[current_node] + weight

            # Optimal node discovery progression
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                f_score = distance + _heuristic(positions, neighbor, target)
                heapq.heappush(priority_queue, (f_score, neighbor))

    # Unreachable target guard: no path exists between source and target
    if distances[target] == float("inf"):
        return [], float("inf")

    # Rebuild the traversed path by walking backwards through predecessor links
    path: List[str] = []
    step: Union[str, None] = target
    while step is not None:
        path.append(step)
        step = predecessors[step]
    path.reverse()

    return path, distances[target]
