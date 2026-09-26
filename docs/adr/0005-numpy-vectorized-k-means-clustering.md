# 5. NumPy Vectorized K-Means Clustering

* **Status:** Approved
* **Context:** Multi-dimensional coordinate distance updates are incredibly slow when written using nested native Python loops.
* **Decision:** We built an independent **K-Means algorithm** using **NumPy broadcasting** matrices to vectorize distance comparisons.
* **Consequences:**
  * Massively increases performance via vectorized array math.
  * Standardizes multi-dimensional inputs smoothly.
  * *Trade-off:* Adds NumPy as a project package dependency.
  * Centroid initialization uses a seeded generator (`seed`, default `42`) so results are reproducible; callers can pass a different seed through `KMeans`, the service wrapper, MCP, or HTTP to explore other initializations.

---
**ADRs:** Previous: [0004](0004-recursive-node-pointer-binary-search-tree.md) · Next: [0006](0006-numpy-eigh-covariance-principal-component-analysis.md) · [ADR index](README.md)  
**Related docs:** [Project README](../../README.md) · [Algorithm catalog](../algorithms.md) · [Runbook](../RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)
