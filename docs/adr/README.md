# Architectural Decision Records

Design choices and trade-offs for each algorithm and for the service layer. ADR `0000` covers foundational infrastructure; algorithm ADRs follow in implementation order. See [Contributing](../CONTRIBUTING.md#3-implementing-an-algorithmfeature) for when to add one.

| ADR | Decision |
|---|---|
| [0000](0000-expose-algorithms-via-mcp-and-http-service-layer.md) | Expose algorithms via MCP and HTTP service layer (amended: HTTP request size limits) |
| [0001](0001-use-hoare-partitioning-for-quicksort.md) | Hoare partitioning for Quicksort |
| [0002](0002-use-heapq-for-dijkstra-priority-queue.md) | `heapq` for Dijkstra priority queue |
| [0003](0003-use-lps-array-for-kmp-string-matching.md) | LPS array for KMP string matching |
| [0004](0004-recursive-node-pointer-binary-search-tree.md) | Recursive node-pointer Binary Search Tree |
| [0005](0005-numpy-vectorized-k-means-clustering.md) | NumPy vectorized K-Means clustering |
| [0006](0006-numpy-eigh-covariance-principal-component-analysis.md) | NumPy `eigh` covariance PCA |
| [0007](0007-use-edge-list-relaxation-for-bellman-ford.md) | Edge-list relaxation for Bellman-Ford |
| [0008](0008-use-euclidean-heuristic-for-a-star.md) | Euclidean heuristic for A* |
| [0009](0009-use-avl-rotations-for-self-balancing-bst.md) | AVL rotations for self-balancing BST |
| [0010](0010-use-min-heap-greedy-merge-for-huffman-coding.md) | Min-heap greedy merge for Huffman coding |
| [0011](0011-use-kahns-in-degree-bfs-for-topological-sort.md) | Kahn's in-degree BFS for topological sort |
| [0012](0012-use-iterative-boolean-marking-for-sieve-of-eratosthenes.md) | Iterative boolean marking for the Sieve of Eratosthenes |
| [0013](0013-use-union-by-rank-with-path-compression-for-union-find.md) | Union by rank with path compression for Union-Find |
| [0014](0014-use-bottom-up-divide-and-conquer-merge-for-merge-sort.md) | Bottom-up divide-and-conquer merge for Merge Sort |
| [0015](0015-use-iterative-pointer-rewiring-for-singly-linked-list-reversal.md) | Iterative pointer rewiring for linked list reversal |
| [0016](0016-use-bottom-up-tabulation-with-backtracking-for-01-knapsack.md) | Bottom-up tabulation with backtracking for 0/1 Knapsack |
| [0017](0017-use-bottom-up-tabulation-with-diagonal-backtracking-for-lcs.md) | Bottom-up tabulation with diagonal backtracking for LCS |
| [0018](0018-use-binary-max-heap-for-heap-sort.md) | Binary max-heap for Heap Sort |
| [0019](0019-use-iterative-midpoint-bisection-for-binary-search.md) | Iterative midpoint bisection for Binary Search |
| [0020](0020-use-iterative-queue-and-stack-for-bfs-dfs.md) | Iterative queue and stack for BFS and DFS |
| [0021](0021-use-edge-sorted-union-find-for-kruskal.md) | Edge-sorted Union-Find for Kruskal |
| [0022](0022-use-character-branching-trie-for-prefix-lookups.md) | Character-branching Trie for prefix lookups |
| [0023](0023-use-iterative-euclidean-gcd.md) | Iterative Euclidean GCD |
| [0024](0024-use-stack-for-valid-parentheses.md) | Stack for valid parentheses |
| [0025](0025-use-held-karp-and-two-opt-for-traveling-salesman.md) | Held-Karp and nearest-neighbor 2-opt for TSP |

---
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md) · [Roadmap](../../ROADMAP.md)
