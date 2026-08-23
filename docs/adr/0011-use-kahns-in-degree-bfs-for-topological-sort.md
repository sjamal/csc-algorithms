# 11. Use Kahn's In-Degree BFS for Topological Sort

* **Status:** Approved
* **Context:** Phase 3 required a mechanism to linearize a directed acyclic graph (DAG) such that every dependency edge points from an earlier node to a later one, while also detecting when no valid ordering exists.
* **Decision:** We implemented **Kahn's Algorithm**, tallying in-degree counts for every node and repeatedly dequeuing nodes with zero remaining incoming edges via a `collections.deque`-backed BFS frontier.
* **Consequences:**
  * Achieves standard $O(V + E)$ time complexity, matching the theoretical lower bound for reading every node and edge once.
  * Naturally detects cycles: if the final order's length is shorter than the total node count, some nodes never reached a zero in-degree, indicating an unresolvable dependency cycle.
  * *Trade-off:* Unlike a DFS-based topological sort, Kahn's approach requires an explicit up-front in-degree tally pass before traversal begins, trading a small amount of extra bookkeeping for simpler, non-recursive cycle detection.

