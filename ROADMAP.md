# Algorithmic Development Roadmap

This document serves as the long-term architectural roadmap for this learning repository. Each phase expands upon baseline software engineering, spatial data mapping, and machine learning primitives.

---

## 🗺️ System Blueprint

### Phase 1: Core Framework & Vector Primitives (Completed)
*   **Quicksort**: In-place sorting engine configured using the Hoare partition strategy.
*   **Dijkstra’s Pathfinding**: Shortest-path tracking optimized via native binary min-heaps.
*   **Knuth-Morris-Pratt (KMP)**: Linear-time pattern matching powered by an LPS array.
*   **Binary Search Tree (BST)**: Pointer-linked hierarchical collection data layout.
*   **K-Means Clustering**: Multi-dimensional spatial grouping via vectorized NumPy operations.
*   **Principal Component Analysis (PCA)**: Feature extraction utilizing covariance eigenvalue transformations.

### Phase 2: Advanced Graph Networks & Navigation
*   **Bellman-Ford Algorithm**: Shortest path matrix solver capable of handling negative edge weight systems. (Completed)
*   **A* Pathfinding Optimization**: Heuristic-driven spatial routing designed for rapid topological traversal. (Completed)

### Phase 3: Self-Balancing Trees & Data Compression
*   **AVL or Red-Black Trees**: Self-adjusting trees that maintain a maximum $O(\log n)$ runtime depth across adversarial data sets. (Completed)
*   **Huffman Coding**: Greedy tree construction designed to output optimal variable-length character prefix maps. (Completed)
*   **Topological Sort (Kahn's Algorithm)**: In-degree tracked BFS ordering resolving dependency sequencing across directed acyclic graphs. (Completed)
*   **Sieve of Eratosthenes**: Iterative marking sieve generating prime number sequences up to a defined boundary. (Completed)

### Phase 4: Foundational Structures & Sorting Alternatives
*   **Union-Find (Disjoint Set)**: Path-compressed, rank-unioned set tracking structure resolving connectivity queries in near-constant time. (Completed)
*   **Merge Sort**: Stable divide-and-conquer sorting engine contrasting Quicksort's in-place, non-stable partitioning approach.
*   **Singly Linked List**: Pointer-chained sequential collection supporting traversal, insertion, and reversal operations.

### Phase 5: Dynamic Programming & Sequence Analysis
*   **0/1 Knapsack Problem**: Tabular matrix memoization framework designed to resolve finite profit boundaries.
*   **Longest Common Subsequence (LCS)**: Relational alignment mapping tracking matching sub-segments within strings.

---

## 🔌 Cross-Cutting: Interoperability
*   **MCP Server & HTTP API**: Transport-agnostic `service/` layer exposing every implemented algorithm as a stateless MCP tool (stdio) and a REST endpoint (FastAPI), for consumption by agents, chat clients, and other programmatic callers. (Completed)

---

## ⚙️ Automated Quality Thresholds
Each addition from this roadmap must strive to maintain good engineering standards before being integrated into `main`:
1.  **Strict Compliance**: Explicit adherence to PEP 8 syntax formatting protocols checked via local hooks.
2.  **Architectural Records**: Every core logic model requires an isolated ADR record filed under `docs/adr/`.
3.  **Flawless Test Coverage**: Complete validation suite parsing forcing a mandatory **100% test coverage baseline**.
