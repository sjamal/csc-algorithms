# 7. Use Edge-List Relaxation for Bellman-Ford Shortest Paths

* **Status:** Approved
* **Context:** Dijkstra's greedy priority-queue approach cannot safely process graphs containing negative edge weights. A more tolerant algorithm was required for Phase 2 negative-weight systems.
* **Decision:** We implemented the classic **Bellman-Ford** algorithm using a flattened edge-list relaxed across `V - 1` iterations, followed by a final pass to detect negative-weight cycles.
* **Consequences:**
  * Achieves standard $O(V \times E)$ time complexity, trading Dijkstra's speed for correctness on negative-weight edges.
  * Explicitly detects and raises on reachable negative-weight cycles rather than looping indefinitely or returning silently incorrect results.
  * *Trade-off:* Slower on dense, non-negative graphs where Dijkstra's heap-based approach remains the preferred choice.

---
**ADRs:** Previous: [0006](0006-numpy-eigh-covariance-principal-component-analysis.md) · Next: [0008](0008-use-euclidean-heuristic-for-a-star.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)

