# 17. Use Bottom-Up Tabulation with Diagonal Backtracking for LCS

* **Status:** Approved
* **Context:** Phase 5's second item required finding the longest subsequence (not necessarily contiguous, but order-preserving) common to two strings — a classic sequence-alignment problem underlying diff tools and bioinformatics sequence comparison.
* **Decision:** We implemented **bottom-up tabulation**: an `(n + 1) x (m + 1)` matrix where `table[i][j]` holds the LCS length between `first[:i]` and `second[:j]`, built iteratively character by character. A backtracking pass then walks the matrix diagonally from the bottom-right corner to reconstruct the actual matched characters.
* **Consequences:**
  * Achieves $O(n \times m)$ time and space complexity, the standard optimal bound for this problem via dynamic programming.
  * Reuses the same tabulation-plus-backtracking pattern established by the 0/1 Knapsack solver (ADR 0016), keeping the `dynamic_programming` module's design internally consistent.
  * *Trade-off:* When multiple distinct longest subsequences exist (a tie in matched length), the backtracking pass deterministically favors the "move up" direction over "move left" on ties, returning one valid LCS rather than enumerating all of them.

