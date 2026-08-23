"""Greedy prefix-code compression module built on a frequency-ordered binary tree."""

import heapq
from itertools import count
from typing import Dict, Optional, Tuple


class HuffmanNode:
    """Represents a single structural node within the Huffman coding tree."""

    def __init__(
        self,
        frequency: int,
        char: Optional[str] = None,
        left: Optional["HuffmanNode"] = None,
        right: Optional["HuffmanNode"] = None,
    ) -> None:
        self.frequency: int = frequency
        self.char: Optional[str] = char
        self.left: Optional["HuffmanNode"] = left
        self.right: Optional["HuffmanNode"] = right

    def is_leaf(self) -> bool:
        """Returns True if this node represents a terminal character symbol."""
        return self.left is None and self.right is None


def _build_frequency_table(text: str) -> Dict[str, int]:
    """Tallies the occurrence count of each character within the source text."""
    frequency_table: Dict[str, int] = {}
    for char in text:
        frequency_table[char] = frequency_table.get(char, 0) + 1
    return frequency_table


def _build_tree(frequency_table: Dict[str, int]) -> Optional[HuffmanNode]:
    """Greedily merges the two lowest-frequency nodes until a single root remains."""
    # A monotonically increasing tie-breaker prevents heapq from comparing HuffmanNode objects
    tie_breaker = count()
    heap: list = [
        (freq, next(tie_breaker), HuffmanNode(freq, char))
        for char, freq in frequency_table.items()
    ]
    heapq.heapify(heap)

    # Single-symbol edge case: no merge is possible, return the lone leaf as root
    if len(heap) == 1:
        _, _, only_node = heap[0]
        return only_node

    while len(heap) > 1:
        freq_a, _, node_a = heapq.heappop(heap)
        freq_b, _, node_b = heapq.heappop(heap)
        merged = HuffmanNode(freq_a + freq_b, left=node_a, right=node_b)
        heapq.heappush(heap, (merged.frequency, next(tie_breaker), merged))

    return heap[0][2]


def _generate_codes(
    node: Optional[HuffmanNode], prefix: str, codebook: Dict[str, str]
) -> None:
    """Recursively walks the tree, assigning '0'/'1' prefix codes to each leaf."""
    if node.is_leaf():
        # A lone root (single unique character) still needs a valid one-bit code
        codebook[node.char] = prefix or "0"
        return

    _generate_codes(node.left, prefix + "0", codebook)
    _generate_codes(node.right, prefix + "1", codebook)


def encode(text: str) -> Tuple[str, Dict[str, str]]:
    """Compresses text into a bitstring using greedily-built variable-length codes.

    Complexity Analysis:
        Time Complexity: O(n + k log k) where n is text length, k is unique character count.
        Space Complexity: O(k) for the frequency table and codebook.
    """
    if not text:
        return "", {}

    frequency_table = _build_frequency_table(text)
    root = _build_tree(frequency_table)

    codebook: Dict[str, str] = {}
    _generate_codes(root, "", codebook)

    encoded_bits = "".join(codebook[char] for char in text)
    return encoded_bits, codebook


def decode(encoded_bits: str, codebook: Dict[str, str]) -> str:
    """Reconstructs the original text from an encoded bitstring and its codebook."""
    if not encoded_bits or not codebook:
        return ""

    # Guard clause against malformed or adversarial codebook payloads
    reverse_codebook = {code: char for char, code in codebook.items()}
    if len(reverse_codebook) != len(codebook):
        raise ValueError("Codebook contains duplicate codes; execution halted.")

    decoded_chars = []
    current_code = ""
    for bit in encoded_bits:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_chars.append(reverse_codebook[current_code])
            current_code = ""

    if current_code:
        raise ValueError("Encoded bitstring is not a valid sequence of known codes.")

    return "".join(decoded_chars)
