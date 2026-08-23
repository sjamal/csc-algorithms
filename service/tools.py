"""Transport-agnostic wrapper functions adapting src/ algorithms to JSON-friendly I/O.

This module contains no algorithmic logic of its own — it only translates between
plain JSON-serializable primitives (dict/list/str/int/float) and the native
Python/NumPy types expected by the underlying `src/` implementations. Both the
MCP server (service/mcp_server.py) and the HTTP API (service/http_app.py) call
into these same functions, ensuring both transports return identical results.
"""

from typing import Dict, List, Optional, Tuple, Union

import numpy as np

from src.compression.huffman import decode as _huffman_decode
from src.compression.huffman import encode as _huffman_encode
from src.data_structures.avl_tree import AVLTree
from src.data_structures.bst import BinarySearchTree
from src.data_structures.dijkstra import dijkstra
from src.data_structures.linked_list import SinglyLinkedList
from src.data_structures.union_find import UnionFind
from src.dynamic_programming.knapsack import knapsack_01
from src.dynamic_programming.lcs import longest_common_subsequence
from src.graphs.a_star import a_star
from src.graphs.bellman_ford import bellman_ford
from src.graphs.breadth_first_search import breadth_first_search
from src.graphs.depth_first_search import depth_first_search
from src.graphs.topological_sort import topological_sort
from src.machine_learning.kmeans import KMeans
from src.machine_learning.pca import PCA
from src.numeric.sieve import sieve_of_eratosthenes
from src.searching.binary_search import binary_search
from src.sorting.heap_sort import heap_sort
from src.sorting.merge_sort import merge_sort
from src.sorting.quicksort import quicksort
from src.string_matching.kmp import kmp_search

WeightedGraph = Dict[str, List[List[Union[str, float]]]]


def _to_adjacency_tuples(
    graph: WeightedGraph,
) -> Dict[str, List[Tuple[str, Union[int, float]]]]:
    """Converts JSON-friendly `[neighbor, weight]` edge lists into tuple form."""
    return {
        node: [(neighbor, weight) for neighbor, weight in edges]
        for node, edges in graph.items()
    }


def sort_quicksort(values: List[int]) -> List[int]:
    """Sorts a list of integers in ascending order via Quicksort."""
    return quicksort(values)


def sort_merge_sort(values: List[int]) -> List[int]:
    """Sorts a list of integers in ascending order via Merge Sort."""
    return merge_sort(values)


def sort_heap_sort(values: List[int]) -> List[int]:
    """Sorts a list of integers in ascending order via Heap Sort."""
    return heap_sort(values)


def search_binary_search(sorted_values: List[int], target: int) -> Dict:
    """Returns the index of `target` within a sorted array, or -1 if absent."""
    return {"index": binary_search(sorted_values, target)}


def search_kmp(text: str, pattern: str) -> List[int]:
    """Finds every 0-indexed starting position of `pattern` within `text`."""
    return kmp_search(text, pattern)


def build_and_query_bst(values: List[int], search_for: Optional[int] = None) -> Dict:
    """Builds a Binary Search Tree from `values` and reports its sorted layout."""
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)

    result: Dict = {"inorder": tree.inorder_traversal()}
    if search_for is not None:
        result["found"] = tree.search(search_for)
    return result


def build_and_query_avl_tree(
    values: List[int], search_for: Optional[int] = None
) -> Dict:
    """Builds an AVL Tree from `values` and reports its balanced sorted layout."""
    tree = AVLTree()
    for value in values:
        tree.insert(value)

    result: Dict = {
        "inorder": tree.inorder_traversal(),
        "height": tree.root.height if tree.root else 0,
    }
    if search_for is not None:
        result["found"] = tree.search(search_for)
    return result


def build_and_query_union_find(
    elements: List[str], unions: List[List[str]], query: Optional[List[str]] = None
) -> Dict:
    """Builds a Union-Find over `elements`, applies `unions`, and reports resulting groups."""
    uf = UnionFind(elements)
    for first, second in unions:
        uf.union(first, second)

    groups: Dict[str, List[str]] = {}
    for element in elements:
        groups.setdefault(uf.find(element), []).append(element)

    result: Dict = {"groups": sorted((sorted(members) for members in groups.values()))}
    if query is not None:
        result["connected"] = uf.connected(query[0], query[1])
    return result


def build_and_query_linked_list(
    values: List[int], search_for: Optional[int] = None, reverse: bool = False
) -> Dict:
    """Builds a Singly Linked List from `values`, optionally reversing it and searching."""
    linked_list = SinglyLinkedList()
    for value in values:
        linked_list.append(value)

    if reverse:
        linked_list.reverse()

    result: Dict = {"values": linked_list.to_list()}
    if search_for is not None:
        result["found"] = linked_list.search(search_for)
    return result


def dp_knapsack_01(weights: List[int], values: List[int], capacity: int) -> Dict:
    """Selects a subset of items maximizing total value within a fixed weight capacity."""
    max_value, selected_indices = knapsack_01(weights, values, capacity)
    return {"max_value": max_value, "selected_indices": selected_indices}


def dp_longest_common_subsequence(first: str, second: str) -> Dict:
    """Finds the length and content of the longest subsequence common to both strings."""
    length, subsequence = longest_common_subsequence(first, second)
    return {"length": length, "subsequence": subsequence}


def graph_dijkstra(graph: WeightedGraph, source: str) -> Dict:
    """Computes single-source shortest paths using Dijkstra's algorithm."""
    distances, predecessors = dijkstra(_to_adjacency_tuples(graph), source)
    return {"distances": distances, "predecessors": predecessors}


def graph_bellman_ford(graph: WeightedGraph, source: str) -> Dict:
    """Computes single-source shortest paths, tolerating negative edge weights."""
    distances, predecessors = bellman_ford(_to_adjacency_tuples(graph), source)
    return {"distances": distances, "predecessors": predecessors}


def graph_a_star(
    graph: WeightedGraph,
    positions: Dict[str, List[float]],
    source: str,
    target: str,
) -> Dict:
    """Finds the lowest-cost path between two nodes using heuristic-guided search."""
    typed_positions = {node: tuple(coords) for node, coords in positions.items()}
    path, cost = a_star(_to_adjacency_tuples(graph), typed_positions, source, target)
    return {"path": path, "cost": cost}


def graph_topological_sort(graph: Dict[str, List[str]]) -> Dict:
    """Orders nodes such that every directed edge points from earlier to later."""
    return {"order": topological_sort(graph)}


def graph_breadth_first_search(graph: Dict[str, List[str]], source: str) -> Dict:
    """Traverses a graph level by level from `source` using BFS."""
    return {"order": breadth_first_search(graph, source)}


def graph_depth_first_search(graph: Dict[str, List[str]], source: str) -> Dict:
    """Traverses a graph depth first from `source` using an explicit stack."""
    return {"order": depth_first_search(graph, source)}


def compress_huffman_encode(text: str) -> Dict:
    """Compresses text into a bitstring using greedily-built variable-length codes."""
    encoded_bits, codebook = _huffman_encode(text)
    return {"encoded_bits": encoded_bits, "codebook": codebook}


def compress_huffman_decode(encoded_bits: str, codebook: Dict[str, str]) -> Dict:
    """Reconstructs the original text from an encoded bitstring and its codebook."""
    return {"text": _huffman_decode(encoded_bits, codebook)}


def numeric_sieve_of_eratosthenes(limit: int) -> Dict:
    """Returns every prime number in the inclusive range [2, limit]."""
    return {"primes": sieve_of_eratosthenes(limit)}


def ml_kmeans_cluster(points: List[List[float]], k: int, max_iters: int = 100) -> Dict:
    """Partitions data points into `k` clusters, returning labels and centroids."""
    data = np.array(points, dtype=float)
    model = KMeans(k=k, max_iters=max_iters)
    labels = model.fit(data)
    return {"labels": labels.tolist(), "centroids": model.centroids.tolist()}


def ml_pca_project(points: List[List[float]], n_components: int) -> Dict:
    """Projects data points onto their top `n_components` principal components."""
    data = np.array(points, dtype=float)
    model = PCA(n_components=n_components)
    projected = model.fit_transform(data)
    return {"projected_points": projected.tolist()}
