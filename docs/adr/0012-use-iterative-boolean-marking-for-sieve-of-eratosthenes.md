# 12. Use Iterative Boolean Marking for the Sieve of Eratosthenes

* **Status:** Approved
* **Context:** Phase 3 required a prime-number generation utility for boundary-based sequences, favoring throughput over the per-check simplicity of trial division for larger ranges.
* **Decision:** We implemented the **Sieve of Eratosthenes** using a single boolean list, marking composite numbers starting at each prime's square and skipping ahead by that prime's value, rather than checking primality candidate-by-candidate via trial division.
* **Consequences:**
  * Achieves $O(n \log \log n)$ time complexity, substantially faster than $O(n \sqrt{n})$ trial-division approaches for generating all primes up to a boundary.
  * Requires $O(n)$ space for the boolean tracking array, trading memory for the batch-marking speed advantage.
  * *Trade-off:* The full boolean array must be allocated up front, making this approach less suitable than trial division for a single, very large primality check in isolation.

