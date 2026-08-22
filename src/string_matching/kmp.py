"""Knuth-Morris-Pratt (KMP) string matching algorithm."""

from typing import List


def kmp_search(text: str, pattern: str) -> List[int]:
    """Finds all 0-indexed starting positions of a pattern within a text string.

    Complexity Analysis:
        Time Complexity: O(n + m) where n is text length and m is pattern length.
        Space Complexity: O(m) to store the partial match prefix table.
    """
    # Handle absolute empty input parameters cleanly
    if not pattern or not text:
        return []

    text_len, pattern_len = len(text), len(pattern)
    
    # Precompute the Longest Prefix Suffix (LPS) layout array
    lps = _compute_lps(pattern)
    match_indices: List[int] = []
    
    i = 0  # Text crawling tracker index
    j = 0  # Pattern crawling tracker index

    while i < text_len:
        # Match confirmed, advance both tracking index pointers
        if pattern[j] == text[i]:
            i += 1
            j += 1

        # Entire pattern verified successfully
        if j == pattern_len:
            match_indices.append(i - j)
            # Rollback pattern tracker back utilizing tracking arrays
            j = lps[j - 1]
            
        # Character mismatch occurred during active tracking
        elif i < text_len and pattern[j] != text[i]:
            if j != 0:
                # Fallback pattern pointer safely to match last known character segment
                j = lps[j - 1]
            else:
                # No tracking segment remains, safely step main index text forward
                i += 1

    return match_indices


def _compute_lps(pattern: str) -> List[int]:
    """Computes the Longest Prefix Suffix (LPS) array for the KMP pattern."""
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        # Segment matches, build out values and save indices
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Shift backward to find a matching prefix sub-window
                length = lps[length - 1]
            else:
                # Basecase hit, zero out matching indexes
                lps[i] = 0
                i += 1
    return lps
