"""Quicksort module implementing robust, isolated array sorting routines."""

from typing import List


def quicksort(array: List[int]) -> List[int]:
    """Sorts an array of integers in ascending order using Quicksort.

    This function is completely pure and thread-safe: it builds an isolated
    shallow copy of the collection to eliminate unexpected external mutable mutations.

    Complexity Analysis:
        Time Complexity: Best/Average O(n log n), Worst O(n^2)
        Space Complexity: O(log n) auxiliary execution call stack usage.
    """
    # Defensive programming: isolate state from side effects
    arr_copy = list(array)
    _quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def _quicksort_helper(array: List[int], low: int, high: int) -> None:
    """Internal orchestration engine managing targeted split frames recursively."""
    if low < high:
        # Resolve partition array division point
        pivot_index = _partition(array, low, high)

        # Concurrently process split sub-problems via the call stack
        _quicksort_helper(array, low, pivot_index)
        _quicksort_helper(array, pivot_index + 1, high)


def _partition(array: List[int], low: int, high: int) -> int:
    """Executes a dual-pointer Hoare structure optimization around a middle element.

    Note:
        Hoare's arrangement stops pointer parsing efficiently, minimizing overall
        swap tracking operations compared to traditional Lomuto patterns.
    """
    # Pivot selection targeting safe central distribution index
    pivot = array[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        # Move the left index pointer inward
        i += 1
        while array[i] < pivot:
            i += 1

        # Move the right index pointer inward
        j -= 1
        while array[j] > pivot:
            j -= 1

        # Return boundary index if pointers have converged or crossed
        if i >= j:
            return j

        # Swap elements at the out-of-order pointer locations
        array[i], array[j] = array[j], array[i]
