"""Principal Component Analysis (PCA) linear dimensionality reduction matrix tool."""

import numpy as np


class PCA:
    """Reduces dataset dimensionality while maximizing architectural variance."""

    def __init__(self, n_components: int) -> None:
        self.n_components: int = n_components
        self.components: np.ndarray = np.array([])
        self.mean: np.ndarray = np.array([])

    def fit_transform(self, data: np.ndarray) -> np.ndarray:
        """Extracts tracking coordinate bounds and transforms initial inputs."""
        # Shift coordinate center data around 0.0 mean
        self.mean = np.mean(data, axis=0)
        centered_data = data - self.mean

        # Build raw Covariance tracking matrix
        covariance_matrix = np.cov(centered_data, rowvar=False)

        # Calculate values via linear algebra Hermetian extraction methods
        eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

        # Sort weights in descending order to capture highest variance first
        sorted_indices = np.argsort(eigenvalues)[::-1]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]

        # Extract selected principal components based on configured bounds
        self.components = sorted_eigenvectors[:, : self.n_components]

        # Project the original data onto the component vectors
        return np.dot(centered_data, self.components)
