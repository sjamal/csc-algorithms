"""K-Means clustering algorithm built natively on top of NumPy tracking."""

import numpy as np


class KMeans:
    """Partitions dataset samples into K distinct, optimized clusters."""
    def __init__(self, k: int, max_iters: int = 100) -> None:
        self.k: int = k
        self.max_iters: int = max_iters
        self.centroids: np.ndarray = np.array([])

    def fit(self, data: np.ndarray) -> np.ndarray:
        """Computes centroids and returns cluster assignments for input vectors."""
        if len(data) < self.k:
            raise ValueError("Dataset elements must exceed or match targeted cluster count 'k'.")

        # Explicitly set random seed to make calculations reproducible across tests
        rng = np.random.default_rng(42)
        random_indices = rng.choice(len(data), self.k, replace=False)
        self.centroids = data[random_indices].copy()

        labels = np.zeros(len(data), dtype=int)

        for _ in range(self.max_iters):
            # Calculate distance between data points and centroids using broadcasting matrix math
            distances = np.linalg.norm(data[:, np.newaxis] - self.centroids, axis=2)
            
            # Map index tracking to nearest centroid
            new_labels = np.argmin(distances, axis=1)

            # Break early if labels have stopped shifting across iterations
            if np.array_equal(labels, new_labels):
                break
            labels = new_labels

            # Recompute centroid location values by calculating the mean of their assigned cluster points
            for i in range(self.k):
                points_in_cluster = data[labels == i]
                if len(points_in_cluster) > 0:
                    self.centroids[i] = points_in_cluster.mean(axis=0)

        return labels
