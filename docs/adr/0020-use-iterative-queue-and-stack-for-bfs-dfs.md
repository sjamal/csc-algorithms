# 20. Use Iterative Queue and Stack for BFS and DFS

* **Status:** Approved
* **Context:** Phase 7 required graph traversal primitives for reachability and unweighted graph exploration. Both traversals need to tolerate cycles and preserve the adjacency-list order supplied by callers.
* **Decision:** We implemented **Breadth-First Search (BFS)** with a `deque` queue and **Depth-First Search (DFS)** with an explicit stack. DFS pushes neighbors in reverse adjacency order so its traversal matches the listed neighbor order. Both algorithms mark nodes when they are scheduled or visited, validate the source and every referenced node, and return only nodes reachable from the source.
* **Consequences:**
  * Both algorithms run in $O(V + E)$ time and use $O(V)$ auxiliary space.
  * Iterative traversal avoids Python recursion-depth limits on large or adversarial graphs.
  * Traversal order is deterministic for deterministic adjacency lists, while disconnected components remain outside the source-rooted result.
  * Malformed edge references fail with a `ValueError` instead of producing partial or misleading traversal output.
