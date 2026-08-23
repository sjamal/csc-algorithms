# 18. Use a Binary Max-Heap for Heap Sort

* **Status:** Approved
* **Context:** Phase 6 required an in-place comparison sort guaranteeing $O(n \log n)$ worst-case time without Merge Sort's $O(n)$ auxiliary space, rounding out the sorting toolkit alongside Quicksort (fast average case, in-place) and Merge Sort (stable, guaranteed worst case, extra space).
* **Decision:** We implemented **Heap Sort**: first heapify the array into a binary max-heap (in place, via repeated `_sift_down` calls from the last parent node upward), then repeatedly swap the root (maximum element) to the end of the unsorted region and sift down to restore heap order.
* **Consequences:**
  * Guarantees $O(n \log n)$ time in the best, average, and worst case, like Merge Sort, but with only $O(1)$ auxiliary space since the heap is built directly within the array being sorted.
  * *Trade-off:* Heap Sort is not stable (equal elements may be reordered during heap restructuring) and has weaker real-world cache locality than Quicksort due to its non-sequential index-jumping access pattern, so it typically runs slower in practice despite matching Merge Sort's worst-case guarantee.

