# 25. Use Held-Karp and Nearest-Neighbor 2-Opt for the Traveling Salesman Problem

* **Status:** Approved
* **Context:** The repository had shortest-path and spanning-tree primitives but no combinatorial tour optimization. The Traveling Salesman Problem (TSP) asks for the cheapest closed tour visiting every vertex exactly once. It is NP-hard, so no single approach is both exact and scalable.
* **Decision:** We implemented two solvers over the same explicit vertex list and weighted undirected edge list used by Kruskal:
  * **Held-Karp** bitmask dynamic programming for exact answers, capped at `MAX_HELD_KARP_VERTICES = 12` to bound its exponential cost.
  * **Nearest-neighbor construction followed by 2-opt improvement** for larger inputs, returning a good but not guaranteed-optimal tour.
  * The service layer adds an `auto` method that uses Held-Karp within the cap and the heuristic beyond it, reporting which method ran and whether the result is optimal.
* **Consequences:**
  * Held-Karp runs in $O(n^2 2^n)$ time and $O(n 2^n)$ space; the cap keeps it well under a second.
  * The heuristic runs in $O(n^2)$ per 2-opt pass with $O(n^2)$ space for the distance matrix.
  * Inputs must describe a complete graph with non-negative weights; missing pairs, self-loops, and negative weights raise a `ValueError`. Duplicate edges keep the cheapest weight.
  * Tours start and end at an optional `start` vertex (default: the first vertex). Ties resolve deterministically by vertex order.
  * *Trade-off:* Requiring a complete graph keeps both solvers simple and comparable; sparse road-network style inputs must first be completed (for example, with all-pairs shortest paths).

---
**ADRs:** Previous: [0024](0024-use-stack-for-valid-parentheses.md) · Related: [0021 Kruskal](0021-use-edge-sorted-union-find-for-kruskal.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)
