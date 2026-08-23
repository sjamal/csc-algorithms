"""Comprehensive evaluation suite tracking Bellman-Ford, A*, and Topological Sort operations."""

import pytest
from src.graphs.bellman_ford import bellman_ford
from src.graphs.a_star import a_star
from src.graphs.breadth_first_search import breadth_first_search
from src.graphs.depth_first_search import depth_first_search
from src.graphs.topological_sort import topological_sort


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
