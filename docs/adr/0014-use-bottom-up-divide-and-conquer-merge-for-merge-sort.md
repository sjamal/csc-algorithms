# 14. Use Bottom-Up Divide-and-Conquer Merge for Merge Sort

* **Status:** Approved
* **Context:** Phase 4 required a stable sorting alternative to contrast with Quicksort, which is neither stable nor guaranteed $O(n \log n)$ in the worst case ($O(n^2)$ on adversarial pivots).
* **Decision:** We implemented **Merge Sort** using classic recursive divide-and-conquer: the array is split at its midpoint until sublists of length 0 or 1 remain, then repeatedly merged back together via a linear-time two-pointer merge that favors the left run on ties to preserve stability.
* **Consequences:**
  * Guarantees $O(n \log n)$ time complexity in the best, average, **and** worst case, unlike Quicksort's $O(n^2)$ worst case — a meaningful advantage for untrusted or adversarially-ordered input.
  * Stability is preserved (equal elements retain their original relative order), which Quicksort's in-place partitioning scheme does not guarantee.
  * *Trade-off:* Requires $O(n)$ auxiliary space for the merge buffers at each level of recursion, versus Quicksort's $O(\log n)$ call-stack-only footprint; Quicksort remains the better default for large in-memory arrays where its worst case is mitigated (e.g., via pivot randomization).

