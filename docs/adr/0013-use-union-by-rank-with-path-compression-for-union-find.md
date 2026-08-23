# 13. Use Union by Rank with Path Compression for Union-Find

* **Status:** Approved
* **Context:** Phase 4 required a structure to answer "are these two elements connected?" queries efficiently across a dynamically merging partition of elements, without re-traversing full connected components on every query.
* **Decision:** We implemented **Union-Find (Disjoint Set)** combining two standard optimizations: **union by rank** (always attaching the shorter tree under the taller tree's root to bound tree height) and **path compression** (flattening each traversed chain during `find()` so future lookups resolve in one step).
* **Consequences:**
  * Achieves amortized $O(\alpha(n))$ time per operation, where $\alpha$ is the inverse Ackermann function — effectively constant for any input size encountered in practice.
  * `find()` recursively rewrites parent pointers as a side effect of traversal, so the structure self-optimizes with use rather than requiring a separate rebalancing step.
  * *Trade-off:* The element universe is fixed at construction time (`elements` passed to `__init__`); adding new elements after construction is not supported, keeping the implementation simple for the connectivity-query use case it targets.

