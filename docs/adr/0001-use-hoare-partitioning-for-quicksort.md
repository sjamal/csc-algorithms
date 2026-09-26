# 1. Use Hoare Partitioning for Quicksort

* **Status:** Approved
* **Context:** Choosing between Lomuto and Hoare partitioning schemes impacts sorting performance on large arrays or arrays with duplicate elements.
* **Decision:** We implemented the **Hoare partition scheme**.
* **Consequences:** 
  * Hoare's scheme makes three times fewer swaps on average compared to Lomuto.
  * It handles arrays with a high volume of duplicate values much more efficiently.
  * *Trade-off:* The implementation is slightly more abstract and non-stable.

---
**ADRs:** Previous: [0000](0000-expose-algorithms-via-mcp-and-http-service-layer.md) · Next: [0002](0002-use-heapq-for-dijkstra-priority-queue.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)

