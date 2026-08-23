"""Comprehensive evaluation suite tracking Dijkstra, BST, AVL Tree, and Union-Find operations."""

import pytest
from src.data_structures.dijkstra import dijkstra
from src.data_structures.bst import BinarySearchTree
from src.data_structures.avl_tree import AVLTree
from src.data_structures.union_find import UnionFind


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


def test_avl_maintains_balance_on_sequential_insert():
    """Ensures ascending-order insertion (a BST worst case) still yields a shallow tree."""
    avl = AVLTree()
    for val in [1, 2, 3, 4, 5, 6, 7]:
        avl.insert(val)

    # A naive BST would degrade to height 7; AVL rotations must keep it near log2(n)
    assert avl.root.height == 3
    assert avl.inorder_traversal() == [1, 2, 3, 4, 5, 6, 7]


def test_avl_search():
    """Validates key detection across present and absent values."""
    avl = AVLTree()
    for val in [50, 30, 20, 40, 70, 60, 80]:
        avl.insert(val)

    assert avl.search(40) is True
    assert avl.search(99) is False


def test_avl_duplicate_insert_ignored():
    """Ensures re-inserting an existing key does not create a duplicate entry."""
    avl = AVLTree()
    for val in [10, 20, 10, 30]:
        avl.insert(val)

    assert avl.inorder_traversal() == [10, 20, 30]


def test_avl_delete_operations():
    """Validates deletion of leaf, single-child, and two-child nodes preserves ordering."""
    avl = AVLTree()
    for val in [20, 10, 30, 5, 15, 25, 35]:
        avl.insert(val)

    # Delete a leaf node
    avl.delete(5)
    assert avl.inorder_traversal() == [10, 15, 20, 25, 30, 35]

    # Delete a node with two children, forcing an in-order successor splice
    avl.delete(20)
    assert avl.inorder_traversal() == [10, 15, 25, 30, 35]
    assert avl.search(20) is False

    # Deleting a non-existent key leaves the tree unchanged
    avl.delete(999)
    assert avl.inorder_traversal() == [10, 15, 25, 30, 35]


def test_avl_delete_triggers_rebalance():
    """Ensures deletions that unbalance the tree trigger corrective rotations."""
    avl = AVLTree()
    for val in [30, 20, 40, 10, 25, 35, 50, 5]:
        avl.insert(val)

    # Removing nodes from the right subtree should leave the left-heavy tree balanced
    avl.delete(35)
    avl.delete(50)
    avl.delete(40)

    root = avl.root
    assert abs(avl._balance_factor(root)) <= 1
    assert avl.inorder_traversal() == [5, 10, 20, 25, 30]


def test_avl_insert_left_right_rotation():
    """Ensures a Left-Right imbalance triggers a double rotation, not a single one."""
    avl = AVLTree()
    for val in [3, 1, 2]:
        avl.insert(val)

    assert avl.root.key == 2
    assert avl.inorder_traversal() == [1, 2, 3]


def test_avl_insert_right_left_rotation():
    """Ensures a Right-Left imbalance triggers a double rotation, not a single one."""
    avl = AVLTree()
    for val in [1, 3, 2]:
        avl.insert(val)

    assert avl.root.key == 2
    assert avl.inorder_traversal() == [1, 2, 3]


def test_avl_delete_node_with_only_left_child():
    """Ensures deleting a node with a left child but no right child promotes it directly."""
    avl = AVLTree()
    for val in [20, 10, 30, 5]:
        avl.insert(val)

    avl.delete(10)

    assert avl.search(10) is False
    assert avl.inorder_traversal() == [5, 20, 30]


def test_union_find_connects_and_reports_membership():
    """Verifies unioned elements report as connected, and unmerged ones do not."""
    uf = UnionFind(["A", "B", "C", "D", "E"])

    assert uf.union("A", "B") is True
    assert uf.union("B", "C") is True

    assert uf.connected("A", "C") is True
    assert uf.connected("A", "D") is False


def test_union_find_redundant_union_returns_false():
    """Ensures unioning already-connected elements is a no-op reported via return value."""
    uf = UnionFind(["A", "B"])
    uf.union("A", "B")

    assert uf.union("A", "B") is False


def test_union_find_path_compression_flattens_chain():
    """Ensures a find() call compresses a multi-level chain so nodes point directly to the root."""
    uf = UnionFind(["A", "B", "C", "D"])
    uf.union("A", "B")  # A becomes root of {A, B}
    uf.union("C", "D")  # C becomes root of {C, D}
    uf.union(
        "A", "C"
    )  # Equal-rank merge: A absorbs C, leaving D two levels deep (D -> C -> A)

    assert (
        uf._parent["D"] == "C"
    )  # Before compression, D is not yet a direct child of the root

    root = uf.find("D")

    assert root == "A"
    assert uf._parent["D"] == root  # After compression, D points directly to the root


def test_union_find_rejects_unknown_element():
    """Ensures querying an element outside the initial set raises a ValueError safely."""
    uf = UnionFind(["A", "B"])

    with pytest.raises(ValueError, match="does not exist"):
        uf.find("Z")


def test_union_find_attaches_lower_rank_tree_under_higher_rank_root():
    """Ensures union() swaps operand order so the shorter tree attaches under the taller one."""
    uf = UnionFind(["A", "B", "C"])
    uf.union("A", "B")  # A becomes rank-1 root of {A, B}

    # C (rank 0) is passed first; union() must still attach it under A's taller tree
    uf.union("C", "A")

    assert uf.find("C") == "A"
