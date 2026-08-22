# 2. Use heapq for Dijkstra Priority Queue

* **Status:** Approved
* **Context:** Choosing a backend primitive for track management during vertex exploration impacts time complexity metrics.
* **Decision:** We used Python's native `heapq` module (a binary min-heap implementation).
* **Consequences:**
  * Achieves standard $O((V + E) \log V)$ efficiency.
  * Eliminates external dependencies, preserving pure standard library runtime mechanics.
  * *Trade-off:* Lacks a native `decrease_key` operational primitive, requiring old states to remain on the heap and be skipped lazily via a verification check.

