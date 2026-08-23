# Algorithm Catalog

A compact reference for the algorithms and data structures implemented in this repository. Each entry links to its implementation and tests; the service layer exposes the public operations through MCP and HTTP.

## Sorting

| Algorithm | Definition | Complexity | Implementation |
| --- | --- | --- | --- |
| Quicksort | Partitions an array around a pivot and recursively sorts the two sides. | Average $O(n \log n)$; worst $O(n^2)$; $O(\log n)$ average stack space. | [Source](../src/sorting/quicksort.py) · [Tests](../tests/test_sorting.py) |
| Merge Sort | Divides an array, sorts each half, and merges the sorted halves. | $O(n \log n)$ time; $O(n)$ space; stable. | [Source](../src/sorting/merge_sort.py) · [Tests](../tests/test_sorting.py) |
| Heap Sort | Builds a max-heap and repeatedly moves its maximum to the sorted suffix. | $O(n \log n)$ time; $O(1)$ auxiliary space. | [Source](../src/sorting/heap_sort.py) · [Tests](../tests/test_sorting.py) |

## Searching and Strings

| Algorithm | Definition | Complexity | Implementation |
| --- | --- | --- | --- |
| Binary Search | Repeatedly halves a sorted search interval to locate a target. | $O(\log n)$ time; $O(1)$ space. Requires sorted input. | [Source](../src/searching/binary_search.py) · [Tests](../tests/test_searching.py) |
| Knuth-Morris-Pratt | Finds a pattern by reusing an LPS prefix table after mismatches. | $O(n + m)$ time; $O(m)$ space. | [Source](../src/string_matching/kmp.py) · [Tests](../tests/test_string_matching.py) |
| Valid Parentheses | Uses a stack to verify that opening and closing brackets are properly nested. | $O(n)$ time; $O(n)$ space. Non-bracket characters are ignored. | [Source](../src/data_structures/valid_parentheses.py) · [Tests](../tests/test_data_structures.py) |

## Graphs

| Algorithm | Definition | Complexity | Implementation |
| --- | --- | --- | --- |
| Dijkstra | Relaxes non-negative weighted edges using a priority queue to find shortest paths. | $O((V + E) \log V)$ time with a binary heap. | [Source](../src/data_structures/dijkstra.py) · [Tests](../tests/test_data_structures.py) |
| Bellman-Ford | Repeatedly relaxes every edge to support negative weights and detect negative cycles. | $O(VE)$ time; $O(V)$ space. | [Source](../src/graphs/bellman_ford.py) · [Tests](../tests/test_graphs.py) |
| A* | Combines path cost with a heuristic estimate to guide shortest-path exploration. | $O((V + E) \log V)$ typical priority-queue bound. | [Source](../src/graphs/a_star.py) · [Tests](../tests/test_graphs.py) |
| Topological Sort | Removes zero-in-degree vertices in BFS order to produce a dependency ordering. | $O(V + E)$ time; $O(V)$ space. Requires a DAG. | [Source](../src/graphs/topological_sort.py) · [Tests](../tests/test_graphs.py) |
| Breadth-First Search | Explores an unweighted graph level by level from a source vertex. | $O(V + E)$ time; $O(V)$ space. | [Source](../src/graphs/breadth_first_search.py) · [Tests](../tests/test_graphs.py) |
| Depth-First Search | Explores as far as possible along each branch before backtracking. | $O(V + E)$ time; $O(V)$ space. | [Source](../src/graphs/depth_first_search.py) · [Tests](../tests/test_graphs.py) |
| Kruskal | Sorts weighted undirected edges and joins components without creating cycles. | $O(E \log E)$ time; $O(V + E)$ space. | [Source](../src/graphs/kruskal.py) · [Tests](../tests/test_graphs.py) |

## Data Structures

| Structure | Definition | Typical operation complexity | Implementation |
| --- | --- | --- | --- |
| Binary Search Tree | Stores ordered keys in recursively partitioned left and right subtrees. | Average search/insert $O(\log n)$; worst $O(n)$. | [Source](../src/data_structures/bst.py) · [Tests](../tests/test_data_structures.py) |
| AVL Tree | Maintains a BST balance invariant through rotations after updates. | Search/insert/delete $O(\log n)$. | [Source](../src/data_structures/avl_tree.py) · [Tests](../tests/test_data_structures.py) |
| Trie | Stores strings character by character for exact lookup and prefix queries. | Insert/search $O(L)$ for word length $L$; autocomplete depends on results. | [Source](../src/data_structures/trie.py) · [Tests](../tests/test_data_structures.py) |
| Union-Find | Tracks disjoint sets with representative lookup and component merging. | Near-constant amortized operations, $O(\alpha(n))$. | [Source](../src/data_structures/union_find.py) · [Tests](../tests/test_data_structures.py) |
| Singly Linked List | Connects values through forward-only node pointers. | Append/prepend $O(1)$; search/delete/reverse $O(n)$. | [Source](../src/data_structures/linked_list.py) · [Tests](../tests/test_data_structures.py) |

## Dynamic Programming

| Algorithm | Definition | Complexity | Implementation |
| --- | --- | --- | --- |
| 0/1 Knapsack | Selects each item at most once to maximize value under a capacity limit. | $O(nC)$ time and space for $n$ items and capacity $C$. | [Source](../src/dynamic_programming/knapsack.py) · [Tests](../tests/test_dynamic_programming.py) |
| Longest Common Subsequence | Builds a table to find the longest ordered sequence shared by two inputs. | $O(nm)$ time and space. | [Source](../src/dynamic_programming/lcs.py) · [Tests](../tests/test_dynamic_programming.py) |

## Numeric, Compression, and Machine Learning

| Algorithm | Definition | Complexity | Implementation |
| --- | --- | --- | --- |
| Euclidean Algorithm | Repeatedly replaces a pair with the divisor and remainder to find their GCD. | $O(\log \min(|a|, |b|))$ time; $O(1)$ space. | [Source](../src/numeric/gcd.py) · [Tests](../tests/test_numeric.py) |
| Sieve of Eratosthenes | Marks composite multiples to enumerate all primes up to a limit. | $O(n \log \log n)$ time; $O(n)$ space. | [Source](../src/numeric/sieve.py) · [Tests](../tests/test_numeric.py) |
| Huffman Coding | Greedily merges the least-frequent symbols into an optimal prefix-code tree. | $O(n + k \log k)$ construction time for $n$ symbols and $k$ distinct characters. | [Source](../src/compression/huffman.py) · [Tests](../tests/test_compression.py) |
| K-Means | Iteratively assigns points to the nearest centroid and recomputes centroids. | $O(i k n d)$ for iterations $i$, clusters $k$, samples $n$, and dimensions $d$. | [Source](../src/machine_learning/kmeans.py) · [Tests](../tests/test_machine_learning.py) |
| Principal Component Analysis | Projects centered data onto directions of greatest covariance. | Dominated by covariance/eigendecomposition cost; depends on samples and dimensions. | [Source](../src/machine_learning/pca.py) · [Tests](../tests/test_machine_learning.py) |

## Choosing an Implementation

Use the linked source and tests as the executable reference. The [roadmap](../ROADMAP.md) tracks planned work, while the [ADR index](../README.md#architectural-decision-records-adrs) records the major implementation choices. Service consumers can use the stateless [MCP server](../service/mcp_server.py) or [HTTP API](../service/http_app.py).
