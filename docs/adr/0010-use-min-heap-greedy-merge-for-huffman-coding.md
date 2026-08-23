# 10. Use a Min-Heap Greedy Merge for Huffman Coding

* **Status:** Approved
* **Context:** Phase 3 required a lossless compression scheme that assigns shorter bit codes to more frequent characters, without any character's code becoming a prefix of another's.
* **Decision:** We implemented **Huffman Coding** using Python's `heapq` min-heap to greedily merge the two lowest-frequency nodes into a binary tree, then walked the resulting tree to assign `'0'`/`'1'` prefix codes to each leaf.
* **Consequences:**
  * Produces a provably optimal prefix-free code for a known static frequency distribution, matching the theoretical entropy bound for symbol-by-symbol encoding.
  * Reuses the same `heapq` priority-queue pattern already established by Dijkstra and A*, keeping tie-breaking explicit via an auxiliary counter since `HuffmanNode` instances are not natively orderable.
  * *Trade-off:* The single-character edge case (only one unique symbol) has no natural binary split, so it is special-cased to emit a fixed `"0"` code rather than an empty string.

