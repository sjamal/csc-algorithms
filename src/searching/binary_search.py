"""Binary Search module implementing iterative divide-and-conquer lookups on sorted arrays."""

from typing import List


def binary_search(sorted_array: List[int], target: int) -> int:
    """Returns the index of `target` within a sorted array, or -1 if absent.

    The input array must already be sorted in ascending order; behavior on an
    unsorted array is undefined.

    Complexity Analysis:
        Time Complexity: O(log n) where n = len(sorted_array).
        Space Complexity: O(1) — iterative, no recursive call stack growth.
    """
    low, high = 0, len(sorted_array) - 1

    while low <= high:
        # Midpoint computed this way avoids integer overflow in lower-level languages
        mid = low + (high - low) // 2

        if sorted_array[mid] == target:
            return mid
        if sorted_array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
