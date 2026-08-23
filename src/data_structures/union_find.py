"""Disjoint-set data structure resolving connectivity queries via path compression and union by rank."""

from typing import Dict, List


class UnionFind:
    """Tracks a partition of elements into disjoint sets with near-constant time operations.

    Complexity Analysis:
        Time Complexity: O(alpha(n)) amortized per operation, where alpha is the
            inverse Ackermann function (effectively constant for any practical n).
        Space Complexity: O(n) for the parent and rank tracking arrays.
    """

    def __init__(self, elements: List[str]) -> None:
        # Every element starts as its own root, forming n singleton sets
        self._parent: Dict[str, str] = {element: element for element in elements}
        self._rank: Dict[str, int] = {element: 0 for element in elements}

    def find(self, element: str) -> str:
        """Returns the representative (root) of the set containing `element`."""
        if element not in self._parent:
            raise ValueError(
                f"Element '{element}' does not exist within this structure."
            )

        # Path compression: flatten the chain so future lookups are near-instant
        if self._parent[element] != element:
            self._parent[element] = self.find(self._parent[element])
        return self._parent[element]

    def union(self, first: str, second: str) -> bool:
        """Merges the sets containing `first` and `second`; returns True if a merge occurred."""
        first_root = self.find(first)
        second_root = self.find(second)

        # Already in the same set; no structural change required
        if first_root == second_root:
            return False

        # Union by rank: attach the shorter tree under the taller tree's root
        if self._rank[first_root] < self._rank[second_root]:
            first_root, second_root = second_root, first_root

        self._parent[second_root] = first_root
        if self._rank[first_root] == self._rank[second_root]:
            self._rank[first_root] += 1

        return True

    def connected(self, first: str, second: str) -> bool:
        """Returns True if `first` and `second` belong to the same set."""
        return self.find(first) == self.find(second)
