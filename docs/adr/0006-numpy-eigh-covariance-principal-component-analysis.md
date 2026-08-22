# 6. NumPy eigh Covariance Principal Component Analysis

* **Status:** Approved
* **Context:** Reducing dimensions through feature extraction requires highly reliable matrix transformations.
* **Decision:** We implemented **Principal Component Analysis (PCA)** using NumPy's `np.linalg.eigh` function on calculated data covariances.
* **Consequences:**
  * `eigh` is highly optimized for symmetric/Hermitian matrices, ensuring fast and mathematically sound eigenvalue extraction.
  * Correctly sorts feature weights by total variance.
  * *Trade-off:* Requires complete in-memory manipulation of the calculated covariance grid.
