# 21. Use Edge-Sorted Union-Find for Kruskal's Algorithm

* **Status:** Approved
* **Context:** Phase 7 required a minimum spanning tree primitive for weighted undirected graphs. The repository already provides a Union-Find structure with path compression and union by rank.
* **Decision:** We implemented **Kruskal's Algorithm** over an explicit vertex list and weighted edge list. Edges are processed in ascending weight order, and the existing Union-Find accepts an edge only when its endpoints belong to different components. Equal-weight edges retain their input order.
* **Consequences:**
  * The algorithm runs in $O(E \log E)$ time because of edge sorting, with near-constant amortized Union-Find operations.
  * It uses $O(V + E)$ auxiliary space for the disjoint-set state and validated edge list.
  * Negative edge weights are supported because edge ordering, rather than path-distance assumptions, drives selection.
  * Disconnected graphs raise a `ValueError` instead of returning a partial minimum spanning forest.
