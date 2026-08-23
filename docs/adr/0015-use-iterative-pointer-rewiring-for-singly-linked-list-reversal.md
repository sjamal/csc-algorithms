# 15. Use Iterative Pointer Rewiring for Singly Linked List Reversal

* **Status:** Approved
* **Context:** Phase 4 required a foundational pointer-chained sequential structure as a baseline before more advanced list-based structures, with support for traversal, insertion at both ends, deletion, and in-place reversal.
* **Decision:** We implemented a **Singly Linked List** tracking explicit `head` and `tail` pointers (enabling O(1) `append`/`prepend`), and reversed the list using **iterative pointer rewiring** — walking the chain once while redirecting each node's `next` pointer backward — rather than a recursive approach.
* **Consequences:**
  * `append`/`prepend`/`reverse` all run in O(1)/O(1)/O(n) respectively with O(1) auxiliary space, since the iterative reversal avoids the O(n) call-stack depth a recursive implementation would incur.
  * Tracking a `tail` pointer requires explicit bookkeeping during `delete` (reassigning `tail` when the removed node was the last one) and `reverse` (the old head becomes the new tail), trading a small amount of extra logic for O(1) append performance.
  * *Trade-off:* As a singly-linked (not doubly-linked) structure, there is no O(1) backward traversal or O(1) arbitrary-node deletion without first locating the node via a full scan; this keeps the structure simple and memory-efficient for the append/prepend/reverse-focused use case it targets.

