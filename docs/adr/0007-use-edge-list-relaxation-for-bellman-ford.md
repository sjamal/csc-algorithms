# 7. Use Edge-List Relaxation for Bellman-Ford Shortest Paths

* **Status:** Approved
* **Context:** Dijkstra's greedy priority-queue approach cannot safely process graphs containing negative edge weights. A more tolerant algorithm was required for Phase 2 negative-weight systems.
* **Decision:** We implemented the classic **Bellman-Ford** algorithm using a flattened edge-list relaxed across `V - 1` iterations, followed by a final pass to detect negative-weight cycles.
* **Consequences:**
  * Achieves standard $O(V \times E)$ time complexity, trading Dijkstra's speed for correctness on negative-weight edges.
  * Explicitly detects and raises on reachable negative-weight cycles rather than looping indefinitely or returning silently incorrect results.
  * *Trade-off:* Slower on dense, non-negative graphs where Dijkstra's heap-based approach remains the preferred choice.

