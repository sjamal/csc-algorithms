# 24. Use a Stack for Valid Parentheses

* **Status:** Approved
* **Context:** Phase 6 required validation of nested parentheses and bracket expressions, including early detection of mismatched closing symbols.
* **Decision:** We implemented **Valid Parentheses** with a stack of opening symbols and a closing-to-opening lookup map. Non-bracket characters are ignored so expressions can be validated directly.
* **Consequences:**
  * Validation runs in $O(n)$ time and uses $O(n)$ worst-case auxiliary space.
  * Mismatched and prematurely closed brackets fail immediately; leftover openings fail at the end.
  * The supported bracket pairs are `()`, `[]`, and `{}`.

---
**ADRs:** Previous: [0023](0023-use-iterative-euclidean-gcd.md) · Next: [0025](0025-use-held-karp-and-two-opt-for-traveling-salesman.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)
