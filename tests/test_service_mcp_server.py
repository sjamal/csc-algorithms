"""Comprehensive evaluation suite tracking the MCP stdio server tool registrations.

These tests call the `@mcp.tool()`-decorated functions directly (the decorator
registers them with the FastMCP instance but returns the original callable),
verifying they delegate correctly to service/tools.py without needing to spin
up an actual stdio transport session.
"""

from service import mcp_server


def test_mcp_tool_registry_contains_all_algorithms():
    """Ensures every algorithm is registered as a discoverable MCP tool."""
    tool_manager = mcp_server.mcp._tool_manager
    registered_names = {tool.name for tool in tool_manager.list_tools()}

    assert registered_names == {
        "sort_quicksort",
        "sort_merge_sort",
        "sort_heap_sort",
        "search_binary_search",
        "search_kmp",
        "build_and_query_bst",
        "build_and_query_avl_tree",
        "build_and_query_union_find",
        "build_and_query_linked_list",
        "build_and_query_trie",
        "dp_knapsack_01",
        "dp_longest_common_subsequence",
        "graph_dijkstra",
        "graph_bellman_ford",
        "graph_a_star",
        "graph_topological_sort",
        "graph_breadth_first_search",
        "graph_depth_first_search",
        "graph_kruskal",
        "compress_huffman_encode",
        "compress_huffman_decode",
        "numeric_sieve_of_eratosthenes",
        "numeric_greatest_common_divisor",
        "validate_parentheses",
        "ml_kmeans_cluster",
        "ml_pca_project",
    }


def test_mcp_sort_quicksort():
    """Verifies the Quicksort tool returns an ascending-order list."""
    assert mcp_server.sort_quicksort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_mcp_sort_merge_sort():
    """Verifies the Merge Sort tool returns an ascending-order list."""
    assert mcp_server.sort_merge_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_mcp_sort_heap_sort():
    """Verifies the Heap Sort tool returns an ascending-order list."""
    assert mcp_server.sort_heap_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_mcp_search_binary_search():
    """Verifies the Binary Search tool returns the correct index, or -1 if absent."""
    assert mcp_server.search_binary_search([1, 3, 5, 7, 9], target=7) == {"index": 3}
    assert mcp_server.search_binary_search([1, 3, 5, 7, 9], target=4) == {"index": -1}


def test_mcp_search_kmp():
    """Verifies the KMP search tool returns matching start indices."""
    assert mcp_server.search_kmp("ababcababc", "abc") == [2, 7]


def test_mcp_build_and_query_bst():
    """Verifies the BST tool returns sorted layout and search status."""
    result = mcp_server.build_and_query_bst([50, 30, 70], search_for=30)
    assert result == {"inorder": [30, 50, 70], "found": True}


def test_mcp_build_and_query_avl_tree():
    """Verifies the AVL Tree tool returns a balanced layout, height, and search status."""
    result = mcp_server.build_and_query_avl_tree([1, 2, 3, 4, 5, 6, 7], search_for=4)
    assert result["inorder"] == [1, 2, 3, 4, 5, 6, 7]
    assert result["height"] == 3
    assert result["found"] is True


def test_mcp_build_and_query_union_find():
    """Verifies the Union-Find tool applies unions and reports groups/connectivity."""
    result = mcp_server.build_and_query_union_find(
        elements=["A", "B", "C"],
        unions=[["A", "B"]],
        query=["A", "C"],
    )
    assert result == {"groups": [["A", "B"], ["C"]], "connected": False}


def test_mcp_build_and_query_linked_list():
    """Verifies the Linked List tool builds, optionally reverses, and searches."""
    result = mcp_server.build_and_query_linked_list(
        [1, 2, 3], search_for=2, reverse=True
    )
    assert result == {"values": [3, 2, 1], "found": True}


def test_mcp_build_and_query_trie():
    """Verifies the Trie tool returns exact and prefix query results."""
    assert mcp_server.build_and_query_trie(
        ["cat", "car"], search_for="cat", prefix="ca"
    ) == {
        "found": True,
        "starts_with": True,
        "suggestions": ["car", "cat"],
    }


def test_mcp_dp_knapsack_01():
    """Verifies the Knapsack tool returns the optimal value and selected item indices."""
    result = mcp_server.dp_knapsack_01(
        weights=[1, 3, 4, 5], values=[1, 4, 5, 7], capacity=7
    )
    assert result == {"max_value": 9, "selected_indices": [1, 2]}


def test_mcp_dp_longest_common_subsequence():
    """Verifies the LCS tool returns the matched length and subsequence content."""
    result = mcp_server.dp_longest_common_subsequence("ABCBDAB", "BDCABA")
    assert result == {"length": 4, "subsequence": "BCBA"}


def test_mcp_graph_dijkstra():
    """Verifies the Dijkstra tool computes shortest path distances."""
    graph = {"A": [["B", 1]], "B": [["C", 2]], "C": []}
    result = mcp_server.graph_dijkstra(graph, "A")
    assert result["distances"]["C"] == 3


def test_mcp_graph_bellman_ford():
    """Verifies the Bellman-Ford tool handles negative edge weights."""
    graph = {"A": [["B", 4]], "B": [["C", -1]], "C": []}
    result = mcp_server.graph_bellman_ford(graph, "A")
    assert result["distances"]["C"] == 3


def test_mcp_graph_a_star():
    """Verifies the A* tool reconstructs the optimal path and total cost."""
    graph = {"A": [["B", 1]], "B": [["C", 1]], "C": []}
    positions = {"A": [0, 0], "B": [1, 0], "C": [2, 0]}
    result = mcp_server.graph_a_star(graph, positions, "A", "C")
    assert result == {"path": ["A", "B", "C"], "cost": 2}


def test_mcp_graph_topological_sort():
    """Verifies the Topological Sort tool returns a valid dependency order."""
    graph = {"A": ["B"], "B": ["C"], "C": []}
    assert mcp_server.graph_topological_sort(graph) == {"order": ["A", "B", "C"]}


def test_mcp_graph_breadth_first_search():
    """Verifies the BFS tool returns level-order traversal output."""
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    assert mcp_server.graph_breadth_first_search(graph, "A") == {
        "order": ["A", "B", "C", "D", "E"]
    }


def test_mcp_graph_depth_first_search():
    """Verifies the DFS tool returns deterministic preorder traversal output."""
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    assert mcp_server.graph_depth_first_search(graph, "A") == {
        "order": ["A", "B", "D", "C", "E"]
    }


def test_mcp_graph_kruskal():
    """Verifies the Kruskal tool returns a minimum spanning tree."""
    edges = [["A", "B", 1], ["B", "C", 2], ["A", "C", 4]]
    assert mcp_server.graph_kruskal(["A", "B", "C"], edges) == {
        "edges": [["A", "B", 1], ["B", "C", 2]],
        "weight": 3,
    }


def test_mcp_compress_huffman_round_trip():
    """Verifies the Huffman encode/decode tools recover the original text."""
    encoded = mcp_server.compress_huffman_encode("abracadabra")
    decoded = mcp_server.compress_huffman_decode(
        encoded["encoded_bits"], encoded["codebook"]
    )
    assert decoded == {"text": "abracadabra"}


def test_mcp_numeric_sieve_of_eratosthenes():
    """Verifies the sieve tool returns primes up to the given limit."""
    assert mcp_server.numeric_sieve_of_eratosthenes(10) == {"primes": [2, 3, 5, 7]}


def test_mcp_numeric_greatest_common_divisor():
    """Verifies the GCD tool returns the Euclidean result."""
    assert mcp_server.numeric_greatest_common_divisor(-24, 18) == {"gcd": 6}


def test_mcp_validate_parentheses():
    """Verifies the parentheses tool returns bracket validity."""
    assert mcp_server.validate_parentheses("([)]") == {"valid": False}


def test_mcp_ml_kmeans_cluster():
    """Verifies the K-Means tool returns JSON-serializable labels and centroids."""
    points = [[0, 0], [0, 1], [10, 10], [10, 11]]
    result = mcp_server.ml_kmeans_cluster(points, k=2)
    assert len(result["labels"]) == 4
    assert len(result["centroids"]) == 2


def test_mcp_ml_pca_project():
    """Verifies the PCA tool returns projected points with reduced dimensionality."""
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    result = mcp_server.ml_pca_project(points, n_components=1)
    assert len(result["projected_points"]) == 4
    assert len(result["projected_points"][0]) == 1
