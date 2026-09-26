"""Comprehensive evaluation suite tracking graph search, ordering, spanning tree, and tour algorithms."""

import pytest
from src.graphs.bellman_ford import bellman_ford
from src.graphs.a_star import a_star
from src.graphs.breadth_first_search import breadth_first_search
from src.graphs.depth_first_search import depth_first_search
from src.graphs.kruskal import kruskal
from src.graphs.topological_sort import topological_sort
from src.graphs.traveling_salesman import (
    MAX_HELD_KARP_VERTICES,
    held_karp,
    nearest_neighbor_two_opt,
)


@pytest.fixture
def mock_negative_weight_graph():
    """Centralized mock graph configuration including a negative edge weight."""
    return {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 3), ("D", 2), ("E", 3)],
        "C": [("D", 4), ("E", 5)],
        "D": [],
        "E": [("D", -3)],
    }


def test_bellman_ford_routing_matrix(mock_negative_weight_graph):
    """Verifies calculated distance accuracy and predecessor paths match expected models."""
    distances, predecessors = bellman_ford(mock_negative_weight_graph, "A")

    assert distances["A"] == 0
    assert distances["B"] == 4  # Optimal path: A -> B
    assert distances["C"] == 2  # Optimal path: A -> C
    assert distances["E"] == 7  # Optimal path: A -> B -> E (4 + 3)
    assert distances["D"] == 4  # Optimal path: A -> B -> E -> D (4 + 3 - 3)

    assert predecessors["D"] == "E"
    assert predecessors["E"] == "B"


def test_bellman_ford_unreachable_node():
    """Ensures nodes with no incoming path remain flagged as unreachable."""
    isolated_graph = {"A": [("B", 1)], "B": [], "C": [("A", 1)]}

    distances, predecessors = bellman_ford(isolated_graph, "A")

    assert distances["C"] == float("inf")
    assert predecessors["C"] is None


def test_bellman_ford_negative_cycle_detection():
    """Ensures reachable negative-weight cycles raise a ValueError instead of looping forever."""
    cyclical_graph = {"A": [("B", 1)], "B": [("C", -1)], "C": [("A", -1)]}

    with pytest.raises(ValueError, match="negative-weight cycle"):
        bellman_ford(cyclical_graph, "A")


def test_bellman_ford_invalid_source():
    """Ensures input validation layers catch illegal source parameters safely."""
    with pytest.raises(ValueError, match="Target initial seed key"):
        bellman_ford({"A": []}, "Z")


@pytest.fixture
def mock_spatial_graph():
    """Centralized mock graph configuration paired with 2D grid coordinates."""
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 1), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
        "E": [],
    }
    positions = {
        "A": (0, 0),
        "B": (1, 0),
        "C": (1, 1),
        "D": (2, 1),
        "E": (5, 5),
    }
    return graph, positions


def test_a_star_shortest_path(mock_spatial_graph):
    """Verifies the reconstructed path and total cost match the optimal route."""
    graph, positions = mock_spatial_graph

    path, cost = a_star(graph, positions, "A", "D")

    assert path == ["A", "B", "C", "D"]
    assert cost == 3


def test_a_star_unreachable_target(mock_spatial_graph):
    """Ensures an empty path and infinite cost are returned when no route exists."""
    graph, positions = mock_spatial_graph

    path, cost = a_star(graph, positions, "A", "E")

    assert path == []
    assert cost == float("inf")


def test_a_star_security_vulnerabilities(mock_spatial_graph):
    """Ensures input validation layers catch illegal parameters safely."""
    graph, positions = mock_spatial_graph
    malicious_graph = {"A": [("B", -5)], "B": []}
    malicious_positions = {"A": (0, 0), "B": (1, 0)}

    with pytest.raises(ValueError, match="Graph contains a negative weight"):
        a_star(malicious_graph, malicious_positions, "A", "B")

    with pytest.raises(ValueError, match="Source or target key does not exist"):
        a_star(graph, positions, "Z", "A")

    with pytest.raises(ValueError, match="missing spatial coordinates"):
        a_star(graph, {"A": (0, 0)}, "A", "D")


def test_topological_sort_dependency_order():
    """Verifies nodes are ordered such that every edge points forward in the sequence."""
    graph = {"A": ["C"], "B": ["C"], "C": ["D"], "D": []}

    assert topological_sort(graph) == ["A", "B", "C", "D"]


def test_topological_sort_empty_graph():
    """Ensures an empty graph resolves to an empty order without error."""
    assert topological_sort({}) == []


def test_topological_sort_cycle_detection():
    """Ensures a cyclical graph raises a ValueError instead of returning a partial order."""
    cyclical_graph = {"A": ["B"], "B": ["C"], "C": ["A"]}

    with pytest.raises(ValueError, match="Graph contains a cycle"):
        topological_sort(cyclical_graph)


def test_topological_sort_undeclared_node_reference():
    """Ensures an edge pointing to an undeclared node raises a ValueError safely."""
    malformed_graph = {"A": ["Z"]}

    with pytest.raises(ValueError, match="undeclared node"):
        topological_sort(malformed_graph)


def test_breadth_first_search_level_order():
    """Verifies BFS visits reachable nodes level by level in adjacency order."""
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": [],
        "F": [],
    }

    assert breadth_first_search(graph, "A") == ["A", "B", "C", "D", "E"]


def test_depth_first_search_preorder():
    """Verifies iterative DFS preserves adjacency order in preorder traversal."""
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": [],
    }

    assert depth_first_search(graph, "A") == ["A", "B", "D", "C", "E"]


def test_depth_first_search_handles_cycles():
    """Ensures DFS ignores nodes already visited when a graph contains a cycle."""
    graph = {"A": ["B"], "B": ["A"]}

    assert depth_first_search(graph, "A") == ["A", "B"]


@pytest.mark.parametrize("traversal", [breadth_first_search, depth_first_search])
def test_graph_traversals_validate_source_and_edges(traversal):
    """Ensures both traversals reject missing sources and undeclared neighbors."""
    with pytest.raises(ValueError, match="Source key"):
        traversal({"A": []}, "Z")

    with pytest.raises(ValueError, match="undeclared node"):
        traversal({"A": ["Z"]}, "A")


@pytest.mark.parametrize("traversal", [breadth_first_search, depth_first_search])
def test_graph_traversals_handle_empty_source_component(traversal):
    """Ensures both traversals return the source when it has no outgoing edges."""
    assert traversal({"A": [], "B": []}, "A") == ["A"]


def test_kruskal_builds_minimum_spanning_tree():
    """Verifies Kruskal selects the lightest acyclic edges and totals their weight."""
    edges = [
        ("A", "B", 1),
        ("B", "C", 2),
        ("A", "C", 4),
        ("C", "D", 1),
        ("B", "D", 5),
    ]

    assert kruskal(["A", "B", "C", "D"], edges) == (
        [("A", "B", 1), ("C", "D", 1), ("B", "C", 2)],
        4,
    )


def test_kruskal_supports_negative_weights_and_single_vertex():
    """Ensures negative weights are valid and a singleton graph has an empty tree."""
    assert kruskal(["A", "B"], [("A", "B", -2)]) == ([("A", "B", -2)], -2)
    assert kruskal(["A"], []) == ([], 0)


@pytest.mark.parametrize(
    "vertices, edges, message",
    [
        ([], [], "at least one vertex"),
        (["A", "A"], [], "unique"),
        (["A", "B"], [("A", "B")], "two vertices and a weight"),
        (["A", "B"], [("A", "C", 1)], "undeclared vertex"),
        (["A", "B"], [("A", "B", "heavy")], "numeric"),
        (["A", "B"], [], "disconnected"),
    ],
)
def test_kruskal_validates_graph_input(vertices, edges, message):
    """Ensures malformed and disconnected graph inputs raise clear ValueErrors."""
    with pytest.raises(ValueError, match=message):
        kruskal(vertices, edges)


SQUARE_EDGES = [
    ("A", "B", 1),
    ("B", "C", 1),
    ("C", "D", 1),
    ("D", "A", 1),
    ("A", "C", 2),
    ("B", "D", 2),
]

# Nearest-neighbor alone yields cost 25 here; 2-opt must improve it to the optimum 23.
TWO_OPT_EDGES = [
    ("A", "B", 8),
    ("A", "C", 9),
    ("A", "D", 6),
    ("A", "E", 6),
    ("B", "C", 7),
    ("B", "D", 2),
    ("B", "E", 4),
    ("C", "D", 3),
    ("C", "E", 4),
    ("D", "E", 5),
]


def test_held_karp_finds_optimal_tour():
    """Verifies Held-Karp returns the minimum-cost closed tour around a square."""
    assert held_karp(["A", "B", "C", "D"], SQUARE_EDGES) == (
        ["A", "D", "C", "B", "A"],
        4,
    )


def test_held_karp_respects_start_vertex():
    """Ensures the tour begins and ends at the requested start vertex."""
    tour, cost = held_karp(["A", "B", "C", "D"], SQUARE_EDGES, start="C")

    assert tour[0] == tour[-1] == "C"
    assert cost == 4


def test_nearest_neighbor_two_opt_improves_greedy_tour():
    """Verifies 2-opt repairs a suboptimal nearest-neighbor tour to the optimum."""
    vertices = ["A", "B", "C", "D", "E"]

    heuristic_tour, heuristic_cost = nearest_neighbor_two_opt(vertices, TWO_OPT_EDGES)
    _, optimal_cost = held_karp(vertices, TWO_OPT_EDGES)

    assert heuristic_cost == optimal_cost == 23
    assert heuristic_tour[0] == heuristic_tour[-1] == "A"
    assert sorted(heuristic_tour[:-1]) == vertices


@pytest.mark.parametrize("solver", [held_karp, nearest_neighbor_two_opt])
def test_tsp_trivial_graphs(solver):
    """Ensures single-vertex and two-vertex graphs return valid closed tours."""
    assert solver(["A"], []) == (["A"], 0)
    assert solver(["A", "B"], [("A", "B", 3)]) == (["A", "B", "A"], 6)


def test_tsp_keeps_cheapest_duplicate_edge():
    """Ensures duplicate edges between the same pair resolve to the lowest weight."""
    edges = [("A", "B", 5), ("B", "A", 2), ("A", "B", 9)]

    assert held_karp(["A", "B"], edges) == (["A", "B", "A"], 4)


@pytest.mark.parametrize("solver", [held_karp, nearest_neighbor_two_opt])
@pytest.mark.parametrize(
    "vertices, edges, start, message",
    [
        ([], [], None, "at least one vertex"),
        (["A", "A"], [], None, "unique"),
        (["A", "B"], [("A", "B")], None, "two vertices and a weight"),
        (["A", "B"], [("A", "C", 1)], None, "undeclared vertex"),
        (["A", "B"], [("A", "A", 1)], None, "Self-loop"),
        (["A", "B"], [("A", "B", "far")], None, "numeric"),
        (["A", "B"], [("A", "B", True)], None, "numeric"),
        (["A", "B"], [("A", "B", -1)], None, "non-negative"),
        (["A", "B", "C"], [("A", "B", 1), ("B", "C", 1)], None, "not complete"),
        (["A", "B"], [("A", "B", 1)], "Z", "Start vertex"),
    ],
)
def test_tsp_validates_graph_input(solver, vertices, edges, start, message):
    """Ensures malformed, incomplete, and negative-weight inputs raise clear ValueErrors."""
    with pytest.raises(ValueError, match=message):
        solver(vertices, edges, start=start)


def test_held_karp_rejects_oversized_graphs():
    """Ensures the exponential exact solver refuses inputs beyond its safe size cap."""
    vertices = [f"V{i}" for i in range(MAX_HELD_KARP_VERTICES + 1)]

    with pytest.raises(ValueError, match="at most"):
        held_karp(vertices, [])
