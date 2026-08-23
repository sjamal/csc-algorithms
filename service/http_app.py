"""FastAPI HTTP layer exposing every csc-algorithms implementation as a REST endpoint.

Run with: `uvicorn service.http_app:app --reload`. Each endpoint mirrors the
corresponding MCP tool in service/mcp_server.py and shares the same underlying
service/tools.py wrapper functions, so both transports return identical results.
"""

from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from service import tools

app = FastAPI(
    title="csc-algorithms API",
    description="REST access to classic computer science algorithm implementations.",
    version="1.0.0",
)


def _call(func, *args, **kwargs):
    """Invokes a tools.py function, translating input ValueErrors into HTTP 400s."""
    try:
        return func(*args, **kwargs)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


class SortRequest(BaseModel):
    values: List[int]


class KmpSearchRequest(BaseModel):
    text: str
    pattern: str


class TreeQueryRequest(BaseModel):
    values: List[int]
    search_for: Optional[int] = None


class UnionFindRequest(BaseModel):
    elements: List[str]
    unions: List[List[str]]
    query: Optional[List[str]] = None


class LinkedListRequest(BaseModel):
    values: List[int]
    search_for: Optional[int] = None
    reverse: bool = False


class WeightedGraphRequest(BaseModel):
    graph: Dict[str, List[List[object]]]
    source: str


class AStarRequest(BaseModel):
    graph: Dict[str, List[List[object]]]
    positions: Dict[str, List[float]]
    source: str
    target: str


class TopologicalSortRequest(BaseModel):
    graph: Dict[str, List[str]]


class HuffmanEncodeRequest(BaseModel):
    text: str


class HuffmanDecodeRequest(BaseModel):
    encoded_bits: str
    codebook: Dict[str, str]


class SieveRequest(BaseModel):
    limit: int


class ClusterRequest(BaseModel):
    points: List[List[float]]
    k: int
    max_iters: int = 100


class PcaRequest(BaseModel):
    points: List[List[float]]
    n_components: int


@app.post("/sorting/quicksort")
def sort_quicksort(request: SortRequest) -> List[int]:
    """Sorts a list of integers in ascending order using Quicksort."""
    return _call(tools.sort_quicksort, request.values)


@app.post("/sorting/merge-sort")
def sort_merge_sort(request: SortRequest) -> List[int]:
    """Sorts a list of integers in ascending order using Merge Sort."""
    return _call(tools.sort_merge_sort, request.values)


@app.post("/string-matching/kmp")
def search_kmp(request: KmpSearchRequest) -> List[int]:
    """Finds every 0-indexed starting position of a pattern within a text."""
    return _call(tools.search_kmp, request.text, request.pattern)


@app.post("/data-structures/bst")
def build_and_query_bst(request: TreeQueryRequest) -> Dict:
    """Builds a Binary Search Tree and returns its sorted layout."""
    return _call(tools.build_and_query_bst, request.values, request.search_for)


@app.post("/data-structures/avl-tree")
def build_and_query_avl_tree(request: TreeQueryRequest) -> Dict:
    """Builds a self-balancing AVL Tree and returns its layout/height."""
    return _call(tools.build_and_query_avl_tree, request.values, request.search_for)


@app.post("/data-structures/union-find")
def build_and_query_union_find(request: UnionFindRequest) -> Dict:
    """Builds a Union-Find over a set of elements and returns the resulting groups."""
    return _call(
        tools.build_and_query_union_find,
        request.elements,
        request.unions,
        request.query,
    )


@app.post("/data-structures/linked-list")
def build_and_query_linked_list(request: LinkedListRequest) -> Dict:
    """Builds a Singly Linked List, optionally reversing it, and returns its layout."""
    return _call(
        tools.build_and_query_linked_list,
        request.values,
        request.search_for,
        request.reverse,
    )


@app.post("/graphs/dijkstra")
def graph_dijkstra(request: WeightedGraphRequest) -> Dict:
    """Computes single-source shortest paths using Dijkstra's algorithm."""
    return _call(tools.graph_dijkstra, request.graph, request.source)


@app.post("/graphs/bellman-ford")
def graph_bellman_ford(request: WeightedGraphRequest) -> Dict:
    """Computes single-source shortest paths, tolerating negative edge weights."""
    return _call(tools.graph_bellman_ford, request.graph, request.source)


@app.post("/graphs/a-star")
def graph_a_star(request: AStarRequest) -> Dict:
    """Finds the lowest-cost path between two nodes using heuristic-guided search."""
    return _call(
        tools.graph_a_star,
        request.graph,
        request.positions,
        request.source,
        request.target,
    )


@app.post("/graphs/topological-sort")
def graph_topological_sort(request: TopologicalSortRequest) -> Dict:
    """Orders nodes such that every directed edge points from earlier to later."""
    return _call(tools.graph_topological_sort, request.graph)


@app.post("/compression/huffman/encode")
def compress_huffman_encode(request: HuffmanEncodeRequest) -> Dict:
    """Compresses text into a bitstring using greedily-built variable-length codes."""
    return _call(tools.compress_huffman_encode, request.text)


@app.post("/compression/huffman/decode")
def compress_huffman_decode(request: HuffmanDecodeRequest) -> Dict:
    """Reconstructs the original text from an encoded bitstring and its codebook."""
    return _call(tools.compress_huffman_decode, request.encoded_bits, request.codebook)


@app.post("/numeric/sieve-of-eratosthenes")
def numeric_sieve_of_eratosthenes(request: SieveRequest) -> Dict:
    """Returns every prime number in the inclusive range [2, limit]."""
    return _call(tools.numeric_sieve_of_eratosthenes, request.limit)


@app.post("/machine-learning/kmeans")
def ml_kmeans_cluster(request: ClusterRequest) -> Dict:
    """Partitions data points into `k` clusters, returning labels and centroids."""
    return _call(tools.ml_kmeans_cluster, request.points, request.k, request.max_iters)


@app.post("/machine-learning/pca")
def ml_pca_project(request: PcaRequest) -> Dict:
    """Projects data points onto their top `n_components` principal components."""
    return _call(tools.ml_pca_project, request.points, request.n_components)
