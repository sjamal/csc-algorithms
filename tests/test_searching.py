"""Comprehensive evaluation suite tracking Binary Search lookup operations."""

from src.searching.binary_search import binary_search


def test_binary_search_finds_present_values():
    """Verifies correct index resolution across first, middle, and last positions."""
    sorted_array = [1, 3, 5, 7, 9, 11, 13]

    assert binary_search(sorted_array, 1) == 0
    assert binary_search(sorted_array, 7) == 3
    assert binary_search(sorted_array, 13) == 6


def test_binary_search_absent_value_returns_negative_one():
    """Ensures a target not present in the array resolves to -1."""
    sorted_array = [2, 4, 6, 8, 10]

    assert binary_search(sorted_array, 5) == -1
    assert binary_search(sorted_array, -1) == -1
    assert binary_search(sorted_array, 100) == -1


def test_binary_search_empty_array():
    """Ensures searching an empty array returns -1 without error."""
    assert binary_search([], 5) == -1


def test_binary_search_single_element_array():
    """Ensures single-element arrays resolve correctly for both match and mismatch."""
    assert binary_search([42], 42) == 0
    assert binary_search([42], 7) == -1
