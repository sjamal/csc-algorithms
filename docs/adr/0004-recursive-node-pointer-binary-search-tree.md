# 4. Recursive Node Pointer Binary Search Tree

* **Status:** Approved
* **Context:** Memory representations for dynamic order-based search keys require distinct child-pointer isolation.
* **Decision:** We selected a node-link class pointer model (`BSTNode`) managed through standard recursive sub-tree traversals.
* **Consequences:**
  * Simplifies data operations (Insert, Search, Inorder Traversal) directly without heavy tracking arrays.
  * Offers an intuitive look into binary structure trees.
  * *Trade-off:* Does not self-balance natively. Worst-case shape approaches a linear linked list O(n) if values are inserted in pre-sorted order.

---
**ADRs:** Previous: [0003](0003-use-lps-array-for-kmp-string-matching.md) · Next: [0005](0005-numpy-vectorized-k-means-clustering.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)
