"""Prefix tree supporting word lookup and autocomplete suggestions."""

from typing import Dict, List, Optional


class TrieNode:
    """Represents one character position in a Trie."""

    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_word: bool = False


class Trie:
    """Stores words for efficient exact and prefix-based lookup."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Adds ``word`` to the Trie."""
        current = self.root
        for character in word:
            current = current.children.setdefault(character, TrieNode())
        current.is_word = True

    def search(self, word: str) -> bool:
        """Returns whether ``word`` is stored in the Trie."""
        node = self._find_node(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        """Returns whether any stored word begins with ``prefix``."""
        return self._find_node(prefix) is not None

    def autocomplete(self, prefix: str) -> List[str]:
        """Returns stored words beginning with ``prefix`` in sorted order."""
        node = self._find_node(prefix)
        if node is None:
            return []

        words: List[str] = []

        def collect(current: TrieNode, suffix: str) -> None:
            if current.is_word:
                words.append(prefix + suffix)
            for character in sorted(current.children):
                collect(current.children[character], suffix + character)

        collect(node, "")
        return words

    def _find_node(self, text: str) -> Optional[TrieNode]:
        """Returns the node reached by ``text``, or ``None`` when absent."""
        current = self.root
        for character in text:
            if character not in current.children:
                return None
            current = current.children[character]
        return current
