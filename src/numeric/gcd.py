"""Greatest common divisor calculation using Euclid's iterative algorithm."""


def greatest_common_divisor(first: int, second: int) -> int:
    """Returns the non-negative greatest common divisor of two integers.

    Complexity Analysis:
        Time Complexity: O(log(min(|first|, |second|))).
        Space Complexity: O(1).
    """
    first, second = abs(first), abs(second)
    while second:
        first, second = second, first % second
    return first
