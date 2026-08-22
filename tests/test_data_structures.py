"""Comprehensive evaluation suite tracking Dijkstra and BST routing operations."""

import pytest
from src.data_structures.dijkstra import dijkstra
from src.data_structures.bst import BinarySearchTree


@pytest.fixture
def mock_standard_graph():
    """Centralized mock graph configuration representing a classic multi-tier path model."""
    return {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 3), ("D", 2), ("E", 3)],
        "C": [("B", 1), ("D", 4), ("E", 5)],
        "D": [],
        "E": [("D", 1)],
    }


def test_dijkstra_routing_matrix(mock_standard_graph):
    """Verifies calculated distance accuracy and predecessor paths match expected models."""
    distances, predecessors = dijkstra(mock_standard_graph, "A")

    assert distances["A"] == 0
    assert distances["B"] == 3  # Optimal path: A -> C -> B (2 + 1)
    assert distances["E"] == 6  # Optimal path: A -> C -> B -> E (2 + 1 + 3)

    assert predecessors["B"] == "C"
    assert predecessors["D"] == "B"


def test_dijkstra_security_vulnerabilities():
    """Ensures input validation layers catch illegal parameters safely."""
    malicious_graph = {"A": [("B", -5)], "B": []}

    with pytest.raises(ValueError, match="Graph contains a negative weight"):
        dijkstra(malicious_graph, "A")

    with pytest.raises(ValueError, match="Target initial seed key"):
        dijkstra({"A": []}, "Z")


def test_bst_operations():
    """Validates Binary Search Tree structural tracking (Fixed syntax error loop)."""
    bst = BinarySearchTree()
    input_values = [50, 30, 20, 40, 70, 60, 80]

    for val in input_values:
        bst.insert(val)

    # Validate value detection checks
    assert bst.search(40) is True
    assert bst.search(99) is False

    # Confirm in-order traversal results in sorted order
    assert bst.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]
