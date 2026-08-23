"""Stdio-based MCP server exposing every csc-algorithms implementation as an agent tool.

Run directly (`python -m service.mcp_server`) or register it with an MCP client
(Claude Desktop, VS Code, etc.) using stdio transport. See docs/CONTRIBUTING.md
for a sample client configuration snippet.
"""

from typing import Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from service import tools

mcp = FastMCP(
    name="csc-algorithms",
    instructions=(
        "Exposes classic computer science algorithms (sorting, graph traversal, "
        "self-balancing trees, compression, and machine learning primitives) as "
        "stateless, JSON-in/JSON-out tools."
    ),
)


@mcp.tool()
def sort_quicksort(values: List[int]) -> List[int]:
    """Sorts a list of integers in ascending order using Quicksort."""
    return tools.sort_quicksort(values)


@mcp.tool()
def sort_merge_sort(values: List[int]) -> List[int]:
    """Sorts a list of integers in ascending order using Merge Sort."""
    return tools.sort_merge_sort(values)


@mcp.tool()
def sort_heap_sort(values: List[int]) -> List[int]:
    """Sorts a list of integers in ascending order using Heap Sort."""
    return tools.sort_heap_sort(values)


@mcp.tool()
def search_binary_search(sorted_values: List[int], target: int) -> Dict:
    """Returns the index of `target` within a sorted array, or -1 if absent."""
    return tools.search_binary_search(sorted_values, target)


@mcp.tool()
def search_kmp(text: str, pattern: str) -> List[int]:
    """Finds every 0-indexed starting position of `pattern` within `text`."""
    return tools.search_kmp(text, pattern)


@mcp.tool()
def build_and_query_bst(values: List[int], search_for: Optional[int] = None) -> Dict:
    """Builds a Binary Search Tree from `values` and returns its sorted layout."""
    return tools.build_and_query_bst(values, search_for)


@mcp.tool()
def build_and_query_avl_tree(
    values: List[int], search_for: Optional[int] = None
) -> Dict:
    """Builds a self-balancing AVL Tree from `values` and returns its layout/height."""
    return tools.build_and_query_avl_tree(values, search_for)


@mcp.tool()
def build_and_query_union_find(
    elements: List[str], unions: List[List[str]], query: Optional[List[str]] = None
) -> Dict:
    """Builds a Union-Find over `elements`, applies `unions`, and returns resulting groups."""
    return tools.build_and_query_union_find(elements, unions, query)


@mcp.tool()
def build_and_query_linked_list(
    values: List[int], search_for: Optional[int] = None, reverse: bool = False
) -> Dict:
    """Builds a Singly Linked List from `values`, optionally reversing it and searching."""
    return tools.build_and_query_linked_list(values, search_for, reverse)


@mcp.tool()
def dp_knapsack_01(weights: List[int], values: List[int], capacity: int) -> Dict:
    """Selects a subset of items maximizing total value within a fixed weight capacity."""
    return tools.dp_knapsack_01(weights, values, capacity)


@mcp.tool()
def dp_longest_common_subsequence(first: str, second: str) -> Dict:
    """Finds the length and content of the longest subsequence common to both strings."""
    return tools.dp_longest_common_subsequence(first, second)


@mcp.tool()
def graph_dijkstra(graph: tools.WeightedGraph, source: str) -> Dict:
    """Computes single-source shortest paths using Dijkstra's algorithm."""
    return tools.graph_dijkstra(graph, source)


@mcp.tool()
def graph_bellman_ford(graph: tools.WeightedGraph, source: str) -> Dict:
    """Computes single-source shortest paths, tolerating negative edge weights."""
    return tools.graph_bellman_ford(graph, source)


@mcp.tool()
def graph_a_star(
    graph: tools.WeightedGraph,
    positions: Dict[str, List[float]],
    source: str,
    target: str,
) -> Dict:
    """Finds the lowest-cost path between two nodes using heuristic-guided search."""
    return tools.graph_a_star(graph, positions, source, target)


@mcp.tool()
def graph_topological_sort(graph: Dict[str, List[str]]) -> Dict:
    """Orders nodes such that every directed edge points from earlier to later."""
    return tools.graph_topological_sort(graph)


@mcp.tool()
def compress_huffman_encode(text: str) -> Dict:
    """Compresses text into a bitstring using greedily-built variable-length codes."""
    return tools.compress_huffman_encode(text)


@mcp.tool()
def compress_huffman_decode(encoded_bits: str, codebook: Dict[str, str]) -> Dict:
    """Reconstructs the original text from an encoded bitstring and its codebook."""
    return tools.compress_huffman_decode(encoded_bits, codebook)


@mcp.tool()
def numeric_sieve_of_eratosthenes(limit: int) -> Dict:
    """Returns every prime number in the inclusive range [2, limit]."""
    return tools.numeric_sieve_of_eratosthenes(limit)


@mcp.tool()
def ml_kmeans_cluster(points: List[List[float]], k: int, max_iters: int = 100) -> Dict:
    """Partitions data points into `k` clusters, returning labels and centroids."""
    return tools.ml_kmeans_cluster(points, k, max_iters)


@mcp.tool()
def ml_pca_project(points: List[List[float]], n_components: int) -> Dict:
    """Projects data points onto their top `n_components` principal components."""
    return tools.ml_pca_project(points, n_components)


if (
    __name__ == "__main__"
):  # pragma: no cover - exercised via manual/integration runs only
    mcp.run(transport="stdio")
