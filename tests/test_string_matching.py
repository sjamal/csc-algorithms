"""Unit tests for the Knuth-Morris-Pratt string matching implementation."""

from src.string_matching.kmp import kmp_search


def test_kmp_matches():
    """Validates string match detection arrays."""
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AAAAA", "AA") == [0, 1, 2, 3]
    assert kmp_search("ABC", "XYZ") == []
    assert kmp_search("", "A") == []
