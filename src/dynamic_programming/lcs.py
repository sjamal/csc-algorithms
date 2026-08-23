"""Longest Common Subsequence (LCS) solver using bottom-up tabular dynamic programming."""

from typing import List, Tuple


def longest_common_subsequence(first: str, second: str) -> Tuple[int, str]:
    """Finds the length and content of the longest subsequence common to both strings.

    A subsequence need not be contiguous, but must preserve relative character order.

    Complexity Analysis:
        Time Complexity: O(n * m) where n, m are the lengths of the two strings.
        Space Complexity: O(n * m) for the tabulation matrix.
    """
    n, m = len(first), len(second)

    # table[i][j] = LCS length between first[:i] and second[:j]
    table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i - 1] == second[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    subsequence = _backtrack_subsequence(table, first, second)
    return table[n][m], subsequence


def _backtrack_subsequence(table: List[List[int]], first: str, second: str) -> str:
    """Walks the completed tabulation matrix backward to reconstruct the matched characters."""
    characters = []
    i, j = len(first), len(second)

    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            characters.append(first[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    characters.reverse()
    return "".join(characters)
