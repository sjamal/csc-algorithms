"""Comprehensive evaluation suite tracking the transport-agnostic service tools layer."""

import pytest

from service import tools


def test_sort_quicksort():
    """Verifies Quicksort wrapper returns an ascending-order list."""
    assert tools.sort_quicksort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_sort_merge_sort():
    """Verifies Merge Sort wrapper returns an ascending-order list."""
    assert tools.sort_merge_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_sort_heap_sort():
    """Verifies Heap Sort wrapper returns an ascending-order list."""
    assert tools.sort_heap_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_search_binary_search():
    """Verifies Binary Search wrapper returns the correct index, or -1 if absent."""
    assert tools.search_binary_search([1, 3, 5, 7, 9], target=7) == {"index": 3}
    assert tools.search_binary_search([1, 3, 5, 7, 9], target=4) == {"index": -1}


def test_search_kmp():
    """Verifies KMP wrapper returns matching start indices."""
    assert tools.search_kmp("ababcababc", "abc") == [2, 7]


def test_build_and_query_bst():
    """Verifies BST wrapper returns sorted layout and search status."""
    result = tools.build_and_query_bst([50, 30, 70, 20], search_for=30)
    assert result["inorder"] == [20, 30, 50, 70]
    assert result["found"] is True


def test_build_and_query_bst_without_search():
    """Ensures the 'found' key is omitted when no search value is provided."""
    result = tools.build_and_query_bst([3, 1, 2])
    assert "found" not in result


def test_build_and_query_avl_tree():
    """Verifies AVL wrapper returns a balanced layout, height, and search status."""
    result = tools.build_and_query_avl_tree([1, 2, 3, 4, 5, 6, 7], search_for=4)
    assert result["inorder"] == [1, 2, 3, 4, 5, 6, 7]
    assert result["height"] == 3
    assert result["found"] is True


def test_build_and_query_union_find():
    """Verifies Union-Find wrapper applies unions and reports groups/connectivity."""
    result = tools.build_and_query_union_find(
        elements=["A", "B", "C", "D"],
        unions=[["A", "B"], ["C", "D"]],
        query=["A", "C"],
    )
    assert result["groups"] == [["A", "B"], ["C", "D"]]
    assert result["connected"] is False


def test_build_and_query_union_find_without_query():
    """Ensures the 'connected' key is omitted when no query pair is provided."""
    result = tools.build_and_query_union_find(["A", "B"], unions=[["A", "B"]])
    assert "connected" not in result
    assert result["groups"] == [["A", "B"]]


def test_build_and_query_linked_list():
    """Verifies Linked List wrapper builds, optionally reverses, and searches."""
    result = tools.build_and_query_linked_list([1, 2, 3], search_for=2, reverse=True)
    assert result["values"] == [3, 2, 1]
    assert result["found"] is True


def test_build_and_query_linked_list_without_search_or_reverse():
    """Ensures default behavior omits 'found' and preserves insertion order."""
    result = tools.build_and_query_linked_list([1, 2, 3])
    assert result["values"] == [1, 2, 3]
    assert "found" not in result


def test_dp_knapsack_01():
    """Verifies Knapsack wrapper returns the optimal value and selected item indices."""
    result = tools.dp_knapsack_01(weights=[1, 3, 4, 5], values=[1, 4, 5, 7], capacity=7)
    assert result == {"max_value": 9, "selected_indices": [1, 2]}


def test_dp_longest_common_subsequence():
    """Verifies LCS wrapper returns the matched length and subsequence content."""
    result = tools.dp_longest_common_subsequence("ABCBDAB", "BDCABA")
    assert result == {"length": 4, "subsequence": "BCBA"}


def test_graph_dijkstra():
    """Verifies Dijkstra wrapper converts JSON edge lists and computes distances."""
    graph = {"A": [["B", 1]], "B": [["C", 2]], "C": []}
    result = tools.graph_dijkstra(graph, "A")
    assert result["distances"]["C"] == 3


def test_graph_bellman_ford():
    """Verifies Bellman-Ford wrapper handles negative edge weights."""
    graph = {"A": [["B", 4]], "B": [["C", -1]], "C": []}
    result = tools.graph_bellman_ford(graph, "A")
    assert result["distances"]["C"] == 3


def test_graph_bellman_ford_negative_cycle_raises():
    """Ensures a negative cycle surfaces as a ValueError from the wrapper."""
    graph = {"A": [["B", 1]], "B": [["C", -1]], "C": [["A", -1]]}
    with pytest.raises(ValueError, match="negative-weight cycle"):
        tools.graph_bellman_ford(graph, "A")


def test_graph_a_star():
    """Verifies A* wrapper reconstructs the optimal path and total cost."""
    graph = {"A": [["B", 1]], "B": [["C", 1]], "C": []}
    positions = {"A": [0, 0], "B": [1, 0], "C": [2, 0]}
    result = tools.graph_a_star(graph, positions, "A", "C")
    assert result["path"] == ["A", "B", "C"]
    assert result["cost"] == 2


def test_graph_topological_sort():
    """Verifies Topological Sort wrapper returns a valid dependency order."""
    graph = {"A": ["B"], "B": ["C"], "C": []}
    assert tools.graph_topological_sort(graph) == {"order": ["A", "B", "C"]}


def test_graph_breadth_first_search():
    """Verifies BFS wrapper returns level-order traversal output."""
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    assert tools.graph_breadth_first_search(graph, "A") == {
        "order": ["A", "B", "C", "D", "E"]
    }


def test_graph_depth_first_search():
    """Verifies DFS wrapper returns deterministic preorder traversal output."""
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    assert tools.graph_depth_first_search(graph, "A") == {
        "order": ["A", "B", "D", "C", "E"]
    }


def test_graph_kruskal():
    """Verifies Kruskal wrapper returns JSON-friendly tree edges and total weight."""
    edges = [["A", "B", 1], ["B", "C", 2], ["A", "C", 4]]
    assert tools.graph_kruskal(["A", "B", "C"], edges) == {
        "edges": [["A", "B", 1], ["B", "C", 2]],
        "weight": 3,
    }


def test_compress_huffman_round_trip():
    """Verifies Huffman encode/decode wrappers recover the original text."""
    encoded = tools.compress_huffman_encode("abracadabra")
    decoded = tools.compress_huffman_decode(
        encoded["encoded_bits"], encoded["codebook"]
    )
    assert decoded["text"] == "abracadabra"


def test_numeric_sieve_of_eratosthenes():
    """Verifies the sieve wrapper returns primes up to the given limit."""
    assert tools.numeric_sieve_of_eratosthenes(10) == {"primes": [2, 3, 5, 7]}


def test_ml_kmeans_cluster():
    """Verifies the K-Means wrapper returns JSON-serializable labels and centroids."""
    points = [[0, 0], [0, 1], [10, 10], [10, 11]]
    result = tools.ml_kmeans_cluster(points, k=2)
    assert len(result["labels"]) == 4
    assert len(result["centroids"]) == 2


def test_ml_pca_project():
    """Verifies the PCA wrapper returns projected points with reduced dimensionality."""
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    result = tools.ml_pca_project(points, n_components=1)
    assert len(result["projected_points"]) == 4
    assert len(result["projected_points"][0]) == 1
