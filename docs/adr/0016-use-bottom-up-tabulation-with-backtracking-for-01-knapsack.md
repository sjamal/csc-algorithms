# 16. Use Bottom-Up Tabulation with Backtracking for 0/1 Knapsack

* **Status:** Approved
* **Context:** Phase 5 required a solver for the classic 0/1 Knapsack Problem — selecting a subset of items, each usable at most once, to maximize total value without exceeding a fixed weight capacity. A brute-force approach is exponential ($O(2^n)$), motivating a polynomial dynamic programming solution.
* **Decision:** We implemented **bottom-up tabulation**: a `(items + 1) x (capacity + 1)` matrix where `table[i][c]` holds the best value achievable using the first `i` items within capacity `c`, built iteratively rather than via top-down memoized recursion. A backtracking pass then walks the completed matrix in reverse to recover which specific items were selected.
* **Consequences:**
  * Achieves $O(n \times \text{capacity})$ time and space complexity — pseudo-polynomial, but efficient for any bounded capacity encountered in practice.
  * The iterative tabulation approach avoids Python's recursion depth limits entirely, unlike a naive top-down memoized recursive solution which could hit `RecursionError` on a large item count.
  * *Trade-off:* The full `(items + 1) x (capacity + 1)` matrix is retained in memory to support backtracking; a space-optimized single-row variant would reduce memory to $O(\text{capacity})$ but would lose the ability to reconstruct which items were chosen without additional bookkeeping.

---
**ADRs:** Previous: [0015](0015-use-iterative-pointer-rewiring-for-singly-linked-list-reversal.md) · Next: [0017](0017-use-bottom-up-tabulation-with-diagonal-backtracking-for-lcs.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)

