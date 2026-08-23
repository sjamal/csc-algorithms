# 23. Use the Iterative Euclidean Algorithm for GCD

* **Status:** Approved
* **Context:** Phase 6 required a small numeric primitive for greatest-common-divisor calculations, including zero and negative integer inputs.
* **Decision:** We implemented the **Euclidean Algorithm** iteratively, normalizing inputs with `abs()` and repeatedly replacing the pair with `(divisor, remainder)` until the remainder is zero.
* **Consequences:**
  * The algorithm runs in $O(\log \min(|a|, |b|))$ time and $O(1)$ space.
  * It returns a non-negative result and defines `gcd(0, 0)` as `0`, matching the module's total-function behavior.
  * Iteration avoids recursion-depth limits and keeps the implementation easy to audit.
