"""Comprehensive evaluation suite tracking Sieve of Eratosthenes prime generation."""

from src.numeric.sieve import sieve_of_eratosthenes
from src.numeric.gcd import greatest_common_divisor


def test_sieve_typical_boundary():
    """Verifies correct prime enumeration for a common mid-sized boundary value."""
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sieve_boundary_is_prime():
    """Ensures the boundary value itself is included when it is prime."""
    assert sieve_of_eratosthenes(13) == [2, 3, 5, 7, 11, 13]


def test_sieve_small_boundaries():
    """Ensures boundaries below the first prime resolve to an empty result."""
    assert sieve_of_eratosthenes(0) == []
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(2) == [2]


def test_sieve_rejects_negative_boundary():
    """Ensures negative or otherwise undersized boundary inputs return safely."""
    assert sieve_of_eratosthenes(-10) == []


def test_greatest_common_divisor():
    """Verifies Euclid's algorithm handles positive, negative, and zero inputs."""
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(-24, 18) == 6
    assert greatest_common_divisor(0, 9) == 9
    assert greatest_common_divisor(0, 0) == 0
