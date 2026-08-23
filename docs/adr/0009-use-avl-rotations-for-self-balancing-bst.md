# 9. Use AVL Rotations for Self-Balancing Binary Search Tree

* **Status:** Approved
* **Context:** Phase 1's Binary Search Tree offers no rebalancing guarantee; adversarial or sorted insertion sequences degrade it to a linked list with $O(n)$ operations. Phase 3 required a tree structure that guarantees $O(\log n)$ depth regardless of insertion order.
* **Decision:** We implemented an **AVL Tree**, choosing height-balance rotations (single left/right and double left-right/right-left) over the alternative Red-Black Tree design.
* **Consequences:**
  * Guarantees a stricter balance invariant (height difference of at most 1 between subtrees) than Red-Black Trees, yielding faster lookups.
  * Requires rebalancing checks on both insertion and deletion, recomputing height and triggering rotations bottom-up via recursion.
  * *Trade-off:* AVL rebalances more aggressively than a Red-Black Tree, so write-heavy workloads with frequent insert/delete cycles incur more rotation overhead in exchange for faster reads.

