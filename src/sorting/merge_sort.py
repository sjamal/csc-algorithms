"""Merge Sort module implementing stable, isolated divide-and-conquer array sorting."""

from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """Sorts an array of integers in ascending order using Merge Sort.

    This function is completely pure and thread-safe: it builds an isolated
    copy of the collection to eliminate unexpected external mutable mutations.
    Unlike Quicksort, this implementation is stable: equal elements retain
    their original relative order.

    Complexity Analysis:
        Time Complexity: O(n log n) in the best, average, and worst cases.
        Space Complexity: O(n) auxiliary storage for the merge buffers.
    """
    # Base case: a list of zero or one elements is trivially sorted
    if len(array) <= 1:
        return list(array)

    midpoint = len(array) // 2
    left_half = merge_sort(array[:midpoint])
    right_half = merge_sort(array[midpoint:])

    return _merge(left_half, right_half)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Interleaves two pre-sorted lists into a single sorted list, preserving stability."""
    merged: List[int] = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        # Strict less-than favors the left run on ties, preserving original ordering
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append whichever run still has leftover elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
