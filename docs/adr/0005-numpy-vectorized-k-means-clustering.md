# 5. NumPy Vectorized K-Means Clustering

* **Status:** Approved
* **Context:** Multi-dimensional coordinate distance updates are incredibly slow when written using nested native Python loops.
* **Decision:** We built an independent **K-Means algorithm** using **NumPy broadcasting** matrices to vectorize distance comparisons.
* **Consequences:**
  * Massively increases performance via vectorized array math.
  * Standardizes multi-dimensional inputs smoothly.
  * *Trade-off:* Adds NumPy as a project package dependency.
