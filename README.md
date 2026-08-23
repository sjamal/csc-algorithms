# Computer Science & Software Engineering Algorithms

A structured repository dedicated to implementing, analyzing, and documenting foundational computer science algorithms and data structures using Python. This project serves as an educational sandbox to study runtime complexities, data architecture, and verification methodologies.

## Project Structure

* `src/`: Core Python implementations categorized by algorithmic domain.
* `service/`: Transport-agnostic wrappers exposing the algorithms via an MCP stdio server and a FastAPI HTTP API.
* `tests/`: Automated unit tests mirroring the codebase layout to validate edge cases and performance boundaries.
* `docs/adr/`: Architectural Decision Records tracking the design choices for each algorithm.
* `docs/CONTRIBUTING.md`: Step-by-step branching, testing, and PR/merge workflow guide.

## Getting Started

### Prerequisites

* Python 3.10 or higher
* pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd csc-algorithms
   ```

2. Initialize a local virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install required development and testing dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Execution and Testing

The repository uses `pytest` for codebase verification. Run the test suite globally using the following command:

```bash
pytest tests/
```

To run syntax and style validation checks using `flake8` or `black`:

```bash
black --check src/ tests/
```

## Running the Service Layer

Every algorithm is also exposed via a stateless MCP server and a REST API, both backed by the same `service/tools.py` wrapper functions.

**MCP server (stdio transport)** — for use with MCP-aware agents/chat clients (Claude Desktop, VS Code, etc.):

```bash
python -m service.mcp_server
```

Register it with your MCP client by pointing it at this command; consult your client's documentation for its `mcp.json`/config format.

**HTTP API** — for any other programmatic caller:

```bash
uvicorn service.http_app:app --reload
```

Each endpoint mirrors an MCP tool, e.g. `POST /sorting/quicksort`, `POST /graphs/dijkstra`, `POST /machine-learning/kmeans`. Interactive OpenAPI docs are available at `http://127.0.0.1:8000/docs` once the server is running.

## Architectural Decision Records (ADRs)

The architectural choices, trade-offs, and design patterns for each algorithm are fully documented below:

* [ADR 0000: Expose Algorithms via MCP and HTTP Service Layer](docs/adr/0000-expose-algorithms-via-mcp-and-http-service-layer.md)
* [ADR 0001: Hoare Partitioning for Quicksort](docs/adr/0001-use-hoare-partitioning-for-quicksort.md)
* [ADR 0002: heapq for Dijkstra Priority Queue](docs/adr/0002-use-heapq-for-dijkstra-priority-queue.md)
* [ADR 0003: LPS Array for KMP String Matching](docs/adr/0003-use-lps-array-for-kmp-string-matching.md)
* [ADR 0004: Recursive Node-Pointer Binary Search Tree](docs/adr/0004-recursive-node-pointer-binary-search-tree.md)
* [ADR 0005: NumPy Vectorized K-Means Clustering](docs/adr/0005-numpy-vectorized-k-means-clustering.md)
* [ADR 0006: NumPy eigh Covariance PCA](docs/adr/0006-numpy-eigh-covariance-principal-component-analysis.md)
* [ADR 0007: Edge-List Relaxation for Bellman-Ford](docs/adr/0007-use-edge-list-relaxation-for-bellman-ford.md)
* [ADR 0008: Euclidean Heuristic for A* Pathfinding](docs/adr/0008-use-euclidean-heuristic-for-a-star.md)
* [ADR 0009: AVL Rotations for Self-Balancing BST](docs/adr/0009-use-avl-rotations-for-self-balancing-bst.md)
* [ADR 0010: Min-Heap Greedy Merge for Huffman Coding](docs/adr/0010-use-min-heap-greedy-merge-for-huffman-coding.md)
* [ADR 0011: Kahn's In-Degree BFS for Topological Sort](docs/adr/0011-use-kahns-in-degree-bfs-for-topological-sort.md)
* [ADR 0012: Iterative Boolean Marking for Sieve of Eratosthenes](docs/adr/0012-use-iterative-boolean-marking-for-sieve-of-eratosthenes.md)
* [ADR 0013: Union by Rank with Path Compression for Union-Find](docs/adr/0013-use-union-by-rank-with-path-compression-for-union-find.md)
* [ADR 0014: Bottom-Up Divide-and-Conquer Merge for Merge Sort](docs/adr/0014-use-bottom-up-divide-and-conquer-merge-for-merge-sort.md)
* [ADR 0015: Iterative Pointer Rewiring for Singly Linked List Reversal](docs/adr/0015-use-iterative-pointer-rewiring-for-singly-linked-list-reversal.md)
* [ADR 0016: Bottom-Up Tabulation with Backtracking for 0/1 Knapsack](docs/adr/0016-use-bottom-up-tabulation-with-backtracking-for-01-knapsack.md)
* [ADR 0017: Bottom-Up Tabulation with Diagonal Backtracking for LCS](docs/adr/0017-use-bottom-up-tabulation-with-diagonal-backtracking-for-lcs.md)

---

## Code Quality and Design Guidelines

### Naming Conventions & Code Style
To ensure uniformity, this repository follows strict standards derived from **PEP 8**:
* **Functions & Variables:** Lowercase word blocks separated by underscores (`snake_case`).
* **Protected Components:** Preceded by a single leading underscore (e.g., `_partition`).
* **Constants:** Full uppercase strings separated by underscores (`UPPER_SNAKE_CASE`).
* **Type Hinting:** Mandatory on all public functions via the `typing` module framework.

### Security, Stability & Privacy Considerations
1. **Input Integrity & Memory Protection:** Sorting algorithms construct a explicit local `list()` copy of tracking variables to prevent input reference mutation bugs.
2. **Denial of Service (DoS) Boundaries:** Quicksort worst-case scaling behavior is $O(n^2)$. For safety-critical systems sorting untrusted or adversarial user inputs, randomizing the pivot selection or utilizing `heap-sort`/`merge-sort` derivatives should be considered.
3. **Graph Payload Resilience:** The Dijkstra parser explicitly references data isolation using explicit `float("inf")` typing arrays. Node configurations must strictly pass hashable unique strings to mitigate graph processing collision events.
4. **Data Isolation:** This package operates entirely locally on internal operational states. No logging pipelines, web tracing, or environment data tracking hooks are implemented, ensuring maximum data privacy.
5. **Negative-Weight Cycle Guarding:** The Bellman-Ford implementation runs an explicit final relaxation pass to detect reachable negative-weight cycles and raises a `ValueError` rather than allowing an untrusted graph payload to loop indefinitely.
6. **Heuristic Input Validation:** The A* implementation validates that source, target, and coordinate metadata exist before search begins, and rejects negative edge weights, preventing malformed spatial graphs from corrupting the heuristic scoring.
7. **Balanced Depth Guarantee:** The AVL Tree rebalances on every insert and delete, preventing adversarial sorted-input sequences from degrading traversal operations to linear time.
8. **Codebook Integrity Validation:** The Huffman decoder rejects malformed or duplicate-code codebooks and dangling/invalid bitstreams with an explicit `ValueError`, rather than silently returning corrupted or truncated text.
9. **Cycle & Referential Integrity Guards:** Topological Sort validates that every edge references a declared node and raises a `ValueError` when a cycle prevents a complete ordering, rather than silently returning a partial or misleading sequence.
10. **Bounded Memory Allocation:** The Sieve of Eratosthenes allocates its boolean tracking array based on the caller-supplied boundary; callers should validate untrusted boundary inputs against a sane upper limit before use to avoid excessive memory allocation.
11. **Service Layer Input Validation:** The HTTP API validates request bodies via Pydantic schemas and translates algorithm-level `ValueError`s into HTTP 400 responses rather than leaking stack traces; both the MCP server and HTTP API are stateless per call, so no client-supplied data persists across requests.
12. **Fixed Element Universe:** Union-Find validates every `find()`/`union()` call against its initial element set and raises a `ValueError` for unknown elements, preventing silent creation of untracked entries.
13. **Worst-Case DoS Mitigation:** Merge Sort guarantees $O(n \log n)$ even on adversarial input, making it the safer default over Quicksort when sorting untrusted, attacker-influenced data where worst-case scaling matters.
14. **Bounded Traversal Footprint:** The Singly Linked List's `search`/`delete`/`reverse` operations are strictly O(n) iterative walks with no recursion, preventing stack-depth exhaustion on very large untrusted input lists.
15. **Iterative DP, No Recursion Limits:** The 0/1 Knapsack solver uses bottom-up tabulation rather than top-down recursion, avoiding Python's `RecursionError` on large item counts.
16. **Quadratic Complexity Awareness:** LCS runs in $O(n \times m)$ time and space; callers should bound input string lengths when comparing untrusted, attacker-controlled text to avoid excessive memory allocation on very large inputs.