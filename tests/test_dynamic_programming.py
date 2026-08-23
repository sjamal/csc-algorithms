"""Comprehensive evaluation suite tracking 0/1 Knapsack and LCS resolution."""

import pytest
from src.dynamic_programming.knapsack import knapsack_01
from src.dynamic_programming.lcs import longest_common_subsequence


def test_knapsack_typical_selection():
    """Verifies the optimal value and item selection for a classic textbook scenario."""
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    max_value, selected = knapsack_01(weights, values, capacity=7)

    assert max_value == 9
    assert selected == [1, 2]


def test_knapsack_zero_capacity():
    """Ensures zero capacity yields zero value and no selected items."""
    max_value, selected = knapsack_01([1, 2], [10, 20], capacity=0)

    assert max_value == 0
    assert selected == []


def test_knapsack_empty_items():
    """Ensures an empty item set yields zero value regardless of capacity."""
    max_value, selected = knapsack_01([], [], capacity=10)

    assert max_value == 0
    assert selected == []


def test_knapsack_item_exceeding_capacity_is_excluded():
    """Ensures an item heavier than the capacity is never selected."""
    max_value, selected = knapsack_01([10], [100], capacity=5)

    assert max_value == 0
    assert selected == []


def test_knapsack_mismatched_lengths_raises():
    """Ensures mismatched weights/values lengths raise a ValueError safely."""
    with pytest.raises(ValueError, match="same length"):
        knapsack_01([1, 2], [10], capacity=5)


def test_knapsack_rejects_negative_inputs():
    """Ensures negative capacity, weights, or values raise a ValueError safely."""
    with pytest.raises(ValueError, match="non-negative"):
        knapsack_01([1], [10], capacity=-1)

    with pytest.raises(ValueError, match="non-negative"):
        knapsack_01([-1], [10], capacity=5)

    with pytest.raises(ValueError, match="non-negative"):
        knapsack_01([1], [-10], capacity=5)


def test_lcs_typical_match():
    """Verifies the length and content of a classic textbook LCS scenario."""
    length, subsequence = longest_common_subsequence("ABCBDAB", "BDCABA")

    assert length == 4
    assert subsequence == "BCBA"


def test_lcs_identical_strings():
    """Ensures identical strings resolve to the full string as their own LCS."""
    length, subsequence = longest_common_subsequence("hello", "hello")

    assert length == 5
    assert subsequence == "hello"


def test_lcs_no_common_characters():
    """Ensures completely disjoint character sets yield an empty subsequence."""
    length, subsequence = longest_common_subsequence("abc", "xyz")

    assert length == 0
    assert subsequence == ""


def test_lcs_empty_strings():
    """Ensures one or both empty strings resolve to an empty subsequence safely."""
    assert longest_common_subsequence("", "") == (0, "")
    assert longest_common_subsequence("abc", "") == (0, "")
    assert longest_common_subsequence("", "abc") == (0, "")
