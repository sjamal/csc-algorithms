"""Stack-based validation for correctly nested parentheses and brackets."""

from typing import Dict, List

_OPEN_TO_CLOSE: Dict[str, str] = {"(": ")", "[": "]", "{": "}"}
_CLOSE_TO_OPEN: Dict[str, str] = {
    close: opening for opening, close in _OPEN_TO_CLOSE.items()
}


def valid_parentheses(text: str) -> bool:
    """Returns whether all brackets in ``text`` are correctly nested and closed.

    Non-bracket characters are ignored, allowing expressions such as ``f(a[0])``.

    Complexity Analysis:
        Time Complexity: O(n) where n = length of ``text``.
        Space Complexity: O(n) for the bracket stack in the worst case.
    """
    stack: List[str] = []
    for character in text:
        if character in _OPEN_TO_CLOSE:
            stack.append(character)
        elif character in _CLOSE_TO_OPEN:
            if not stack or stack.pop() != _CLOSE_TO_OPEN[character]:
                return False
    return not stack
