"""Unit tests validating machine learning primitives."""

import numpy as np
from src.machine_learning.kmeans import KMeans
from src.machine_learning.pca import PCA


def test_kmeans_clustering():
    """Validates multi-dimensional spatial clustering separation."""
    cluster_a = np.array([[1.0, 1.0], [1.2, 0.9], [0.8, 1.1]])
    cluster_b = np.array([[10.0, 10.0], [10.2, 9.8], [9.8, 10.1]])
    dataset = np.vstack((cluster_a, cluster_b))

    model = KMeans(k=2)
    labels = model.fit(dataset)

    # Ensure elements within the same group share identical labels
    assert labels[0] == labels[1] == labels[2]
    assert labels[3] == labels[4] == labels[5]
    assert labels[0] != labels[3]


def test_pca_projection():
    """Validates matrix feature dimensional compression."""
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    data = np.column_stack((x, 2 * x, x * 0.5))

    transformer = PCA(n_components=1)
    transformed_data = transformer.fit_transform(data)

    assert transformed_data.shape == (5, 1)


def test_kmeans_insufficient_data_error():
    """Verifies that KMeans throws a ValueError if input points are fewer than clusters."""
    import pytest

    # Configure an empty or insufficient single coordinate matrix
    insufficient_data = np.array([[1.0, 1.0]])

    # Requesting 3 clusters with only 1 data point must trigger our validation guard
    model = KMeans(k=3)
    with pytest.raises(
        ValueError, match="Dataset elements must exceed or match targeted cluster count"
    ):
        model.fit(insufficient_data)
