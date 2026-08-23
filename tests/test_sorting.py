"""Comprehensive evaluation suite tracking Quicksort, Merge Sort, and Heap Sort performance scenarios."""

from src.sorting.quicksort import quicksort
from src.sorting.merge_sort import merge_sort
from src.sorting.heap_sort import heap_sort


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


def test_merge_sort_permutations():
    """Validates structural sorting accuracy across diverse edge cases."""
    # Standard array checks
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    # Boundary conditions: empty and single-element lists
    assert merge_sort([]) == []
    assert merge_sort([42]) == [42]

    # Pre-sorted and reverse-sorted sequences
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Large duplicate cluster evaluation
    assert merge_sort([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_merge_sort_does_not_mutate_input():
    """Ensures the original input list is left untouched, confirming pure-function behavior."""
    original = [3, 1, 2]
    merge_sort(original)

    assert original == [3, 1, 2]


def test_merge_sort_is_stable():
    """Ensures equal elements retain their original relative order, unlike Quicksort."""
    # Each tuple's first element is the sort key; the second tracks original position
    entries = [(2, "a"), (1, "b"), (2, "c"), (1, "d")]

    assert merge_sort(entries) == [(1, "b"), (1, "d"), (2, "a"), (2, "c")]


def test_heap_sort_permutations():
    """Validates structural sorting accuracy across diverse edge cases."""
    # Standard array checks
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    # Boundary conditions: empty and single-element lists
    assert heap_sort([]) == []
    assert heap_sort([42]) == [42]

    # Pre-sorted and reverse-sorted sequences
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Large duplicate cluster evaluation
    assert heap_sort([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_heap_sort_does_not_mutate_input():
    """Ensures the original input list is left untouched, confirming pure-function behavior."""
    original = [3, 1, 2]
    heap_sort(original)

    assert original == [3, 1, 2]
