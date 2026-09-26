# 3. Use LPS Array for KMP String Matching

* **Status:** Approved
* **Context:** Linear-time string searching requires skipping redundant characters when a mismatch occurs.
* **Decision:** We implemented the **Knuth-Morris-Pratt (KMP)** algorithm powered by a Longest Prefix Suffix (LPS) pre-computed array.
* **Consequences:**
  * Guarantees a strict O(n + m) time complexity execution window.
  * Prevents resetting the main text index pointer back backward during processing loops.
  * *Trade-off:* Requires O(m) additional auxiliary space to store token prefixes.

---
**ADRs:** Previous: [0002](0002-use-heapq-for-dijkstra-priority-queue.md) · Next: [0004](0004-recursive-node-pointer-binary-search-tree.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)
