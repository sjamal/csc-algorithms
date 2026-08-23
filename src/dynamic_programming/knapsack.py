"""0/1 Knapsack Problem solver using bottom-up tabular dynamic programming memoization."""

from typing import List, Tuple


def knapsack_01(
    weights: List[int], values: List[int], capacity: int
) -> Tuple[int, List[int]]:
    """Selects a subset of items maximizing total value within a fixed weight capacity.

    Each item may be taken at most once (0/1 constraint, as opposed to the
    unbounded/fractional variants).

    Complexity Analysis:
        Time Complexity: O(n * capacity) where n = number of items.
        Space Complexity: O(n * capacity) for the tabulation matrix.
    """
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must be the same length.")

    # Guard clause against malicious or invalid negative-magnitude inputs
    if (
        capacity < 0
        or any(weight < 0 for weight in weights)
        or any(value < 0 for value in values)
    ):
        raise ValueError("Capacity, weights, and values must be non-negative.")

    item_count = len(weights)

    # table[i][c] = best achievable value using the first i items within capacity c
    table = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):
        weight, value = weights[i - 1], values[i - 1]
        for c in range(capacity + 1):
            # Excluding the current item always remains a valid baseline option
            table[i][c] = table[i - 1][c]

            # Including the current item is only possible if it fits within capacity
            if weight <= c:
                table[i][c] = max(table[i][c], table[i - 1][c - weight] + value)

    selected_indices = _backtrack_selection(table, weights, capacity)
    return table[item_count][capacity], selected_indices


def _backtrack_selection(
    table: List[List[int]], weights: List[int], capacity: int
) -> List[int]:
    """Walks the completed tabulation matrix backward to recover which items were chosen."""
    selected_indices: List[int] = []
    remaining_capacity = capacity

    for i in range(len(weights), 0, -1):
        # A changed value versus the row above means item (i - 1) was included
        if table[i][remaining_capacity] != table[i - 1][remaining_capacity]:
            selected_indices.append(i - 1)
            remaining_capacity -= weights[i - 1]

    selected_indices.reverse()
    return selected_indices
