"""Comprehensive evaluation suite tracking Quicksort performance scenarios."""

from src.sorting.quicksort import quicksort


def test_quicksort_permutations():
    """Validates structural sorting accuracy across diverse edge cases."""
    # Standard array checks
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    # Boundary conditions: empty and single-element lists
    assert quicksort([]) == []
    assert quicksort([42]) == [42]

    # Pre-sorted sequences
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Large duplicate cluster evaluation
    assert quicksort([2, 2, 2, 2]) == [2, 2, 2, 2]
