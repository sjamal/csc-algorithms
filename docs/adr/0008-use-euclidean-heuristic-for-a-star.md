# 8. Use Euclidean Heuristic for A* Pathfinding

* **Status:** Approved
* **Context:** Dijkstra's algorithm explores uniformly outward from the source, which wastes cycles on nodes clearly moving away from the target when spatial coordinates are known.
* **Decision:** We implemented **A*** search reusing Dijkstra's `heapq`-based min-priority queue, augmented with a straight-line (Euclidean) distance heuristic computed via `math.hypot` to bias exploration toward the target.
* **Consequences:**
  * Reduces the number of nodes expanded versus Dijkstra on spatially-distributed graphs, while still guaranteeing an optimal path since the Euclidean distance heuristic is admissible (never overestimates true cost) for non-negative edge weights.
  * Requires every node to carry 2D coordinate metadata, adding a data modeling requirement beyond a bare adjacency list.
  * *Trade-off:* The heuristic assumes edge weights are consistent with real-world distances; graphs with weights unrelated to spatial layout should fall back to plain Dijkstra.

---
**ADRs:** Previous: [0007](0007-use-edge-list-relaxation-for-bellman-ford.md) · Next: [0009](0009-use-avl-rotations-for-self-balancing-bst.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)

