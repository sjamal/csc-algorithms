"""Heap Sort module implementing in-place, comparison-based array sorting via a binary max-heap."""

from typing import List


def heap_sort(array: List[int]) -> List[int]:
    """Sorts an array of integers in ascending order using Heap Sort.

    This function is completely pure and thread-safe: it builds an isolated
    shallow copy of the collection to eliminate unexpected external mutable mutations.

    Complexity Analysis:
        Time Complexity: O(n log n) in the best, average, and worst cases.
        Space Complexity: O(1) auxiliary space (sorting occurs in place on the copy).
    """
    # Defensive programming: isolate state from side effects
    arr_copy = list(array)
    n = len(arr_copy)

    # Build a max-heap: start from the last parent node and sift downward
    for root in range(n // 2 - 1, -1, -1):
        _sift_down(arr_copy, n, root)

    # Repeatedly swap the max element to the end, then restore heap order
    for end in range(n - 1, 0, -1):
        arr_copy[0], arr_copy[end] = arr_copy[end], arr_copy[0]
        _sift_down(arr_copy, end, 0)

    return arr_copy


def _sift_down(array: List[int], heap_size: int, root: int) -> None:
    """Restores the max-heap property for the subtree rooted at `root`."""
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and array[left] > array[largest]:
        largest = left
    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != root:
        array[root], array[largest] = array[largest], array[root]
        # Continue sifting downward since the swapped subtree may now violate heap order
        _sift_down(array, heap_size, largest)
