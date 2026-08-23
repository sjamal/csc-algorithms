"""Comprehensive evaluation suite tracking the FastAPI HTTP service layer."""

from fastapi.testclient import TestClient

from service.http_app import app

client = TestClient(app)


def test_http_sort_quicksort():
    """Verifies the Quicksort endpoint returns an ascending-order list."""
    response = client.post("/sorting/quicksort", json={"values": [5, 2, 4, 1, 3]})
    assert response.status_code == 200
    assert response.json() == [1, 2, 3, 4, 5]


def test_http_sort_merge_sort():
    """Verifies the Merge Sort endpoint returns an ascending-order list."""
    response = client.post("/sorting/merge-sort", json={"values": [5, 2, 4, 1, 3]})
    assert response.status_code == 200
    assert response.json() == [1, 2, 3, 4, 5]


def test_http_search_kmp():
    """Verifies the KMP search endpoint returns matching start indices."""
    response = client.post(
        "/string-matching/kmp", json={"text": "ababcababc", "pattern": "abc"}
    )
    assert response.status_code == 200
    assert response.json() == [2, 7]


def test_http_build_and_query_bst():
    """Verifies the BST endpoint returns sorted layout and search status."""
    response = client.post(
        "/data-structures/bst", json={"values": [50, 30, 70], "search_for": 30}
    )
    assert response.status_code == 200
    assert response.json() == {"inorder": [30, 50, 70], "found": True}


def test_http_build_and_query_avl_tree():
    """Verifies the AVL Tree endpoint returns layout, height, and search status."""
    response = client.post(
        "/data-structures/avl-tree",
        json={"values": [1, 2, 3, 4, 5, 6, 7], "search_for": 99},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["height"] == 3
    assert body["found"] is False


def test_http_build_and_query_union_find():
    """Verifies the Union-Find endpoint applies unions and reports groups/connectivity."""
    response = client.post(
        "/data-structures/union-find",
        json={
            "elements": ["A", "B", "C"],
            "unions": [["A", "B"]],
            "query": ["A", "C"],
        },
    )
    assert response.status_code == 200
    assert response.json() == {"groups": [["A", "B"], ["C"]], "connected": False}


def test_http_build_and_query_linked_list():
    """Verifies the Linked List endpoint builds, optionally reverses, and searches."""
    response = client.post(
        "/data-structures/linked-list",
        json={"values": [1, 2, 3], "search_for": 2, "reverse": True},
    )
    assert response.status_code == 200
    assert response.json() == {"values": [3, 2, 1], "found": True}


def test_http_graph_dijkstra():
    """Verifies the Dijkstra endpoint computes shortest path distances."""
    response = client.post(
        "/graphs/dijkstra",
        json={"graph": {"A": [["B", 1]], "B": [["C", 2]], "C": []}, "source": "A"},
    )
    assert response.status_code == 200
    assert response.json()["distances"]["C"] == 3


def test_http_graph_bellman_ford_negative_cycle_returns_400():
    """Ensures a negative cycle is surfaced as an HTTP 400, not a server error."""
    response = client.post(
        "/graphs/bellman-ford",
        json={
            "graph": {"A": [["B", 1]], "B": [["C", -1]], "C": [["A", -1]]},
            "source": "A",
        },
    )
    assert response.status_code == 400
    assert "negative-weight cycle" in response.json()["detail"]


def test_http_graph_a_star():
    """Verifies the A* endpoint reconstructs the optimal path and total cost."""
    response = client.post(
        "/graphs/a-star",
        json={
            "graph": {"A": [["B", 1]], "B": [["C", 1]], "C": []},
            "positions": {"A": [0, 0], "B": [1, 0], "C": [2, 0]},
            "source": "A",
            "target": "C",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"path": ["A", "B", "C"], "cost": 2}


def test_http_graph_topological_sort():
    """Verifies the Topological Sort endpoint returns a valid dependency order."""
    response = client.post(
        "/graphs/topological-sort",
        json={"graph": {"A": ["B"], "B": ["C"], "C": []}},
    )
    assert response.status_code == 200
    assert response.json() == {"order": ["A", "B", "C"]}


def test_http_huffman_round_trip():
    """Verifies the Huffman encode/decode endpoints recover the original text."""
    encode_response = client.post(
        "/compression/huffman/encode", json={"text": "abracadabra"}
    )
    assert encode_response.status_code == 200
    encoded_body = encode_response.json()

    decode_response = client.post(
        "/compression/huffman/decode",
        json={
            "encoded_bits": encoded_body["encoded_bits"],
            "codebook": encoded_body["codebook"],
        },
    )
    assert decode_response.status_code == 200
    assert decode_response.json() == {"text": "abracadabra"}


def test_http_sieve_of_eratosthenes():
    """Verifies the sieve endpoint returns primes up to the given limit."""
    response = client.post("/numeric/sieve-of-eratosthenes", json={"limit": 10})
    assert response.status_code == 200
    assert response.json() == {"primes": [2, 3, 5, 7]}


def test_http_kmeans_cluster():
    """Verifies the K-Means endpoint returns JSON-serializable labels and centroids."""
    response = client.post(
        "/machine-learning/kmeans",
        json={"points": [[0, 0], [0, 1], [10, 10], [10, 11]], "k": 2},
    )
    assert response.status_code == 200
    body = response.json()
    assert len(body["labels"]) == 4
    assert len(body["centroids"]) == 2


def test_http_pca_project():
    """Verifies the PCA endpoint returns projected points with reduced dimensionality."""
    response = client.post(
        "/machine-learning/pca",
        json={"points": [[1, 2], [3, 4], [5, 6], [7, 8]], "n_components": 1},
    )
    assert response.status_code == 200
    body = response.json()
    assert len(body["projected_points"]) == 4
    assert len(body["projected_points"][0]) == 1
