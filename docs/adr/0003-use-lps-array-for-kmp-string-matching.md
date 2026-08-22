# 3. Use LPS Array for KMP String Matching

* **Status:** Approved
* **Context:** Linear-time string searching requires skipping redundant characters when a mismatch occurs.
* **Decision:** We implemented the **Knuth-Morris-Pratt (KMP)** algorithm powered by a Longest Prefix Suffix (LPS) pre-computed array.
* **Consequences:**
  * Guarantees a strict O(n + m) time complexity execution window.
  * Prevents resetting the main text index pointer back backward during processing loops.
  * *Trade-off:* Requires O(m) additional auxiliary space to store token prefixes.
