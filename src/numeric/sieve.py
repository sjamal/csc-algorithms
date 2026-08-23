"""Prime number generation module using an iterative composite-marking sieve."""

from typing import List


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Returns every prime number in the inclusive range [2, limit].

    Complexity Analysis:
        Time Complexity: O(n log log n) where n = limit.
        Space Complexity: O(n) for the boolean marking array.
    """
    # Guard clause against negative or undersized boundary inputs
    if limit < 2:
        return []

    # Boolean tracking array; index parity represents primality candidacy
    is_prime: List[bool] = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # Only candidates up to sqrt(limit) can still have unmarked multiples
    candidate = 2
    while candidate * candidate <= limit:
        if is_prime[candidate]:
            # Mark every multiple starting from candidate^2 as composite
            for multiple in range(candidate * candidate, limit + 1, candidate):
                is_prime[multiple] = False
        candidate += 1

    return [number for number, prime in enumerate(is_prime) if prime]
