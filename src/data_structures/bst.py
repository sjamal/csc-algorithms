"""Custom Binary Search Tree (BST) data structure implementation."""

from typing import Optional, List


class BSTNode:
    """Represents a single structural node within a Binary Search Tree."""

    def __init__(self, key: int) -> None:
        self.key: int = key
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BinarySearchTree:
    """Standard Binary Search Tree implementing entry mutation operations."""

    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None

    def insert(self, key: int) -> None:
        """Inserts a new numerical key into the tree hierarchy."""
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current: BSTNode, key: int) -> None:
        # Traverse left if incoming value is less than current node key
        if key < current.key:
            if not current.left:
                current.left = BSTNode(key)
            else:
                self._insert_recursive(current.left, key)
        # Traverse right if incoming value is greater or equal
        else:
            if not current.right:
                current.right = BSTNode(key)
            else:
                self._insert_recursive(current.right, key)

    def search(self, key: int) -> bool:
        """Returns True if the key exists within the tree, False otherwise."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current: Optional[BSTNode], key: int) -> bool:
        # Base case: Node is empty or value isn't found
        if not current:
            return False
        # Base case: Exact value found
        if current.key == key:
            return True

        # Tail call down target branch pathways
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    def inorder_traversal(self) -> List[int]:
        """Returns the keys sorted in ascending order using inorder traversal."""
        result: List[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current: Optional[BSTNode], result: List[int]) -> None:
        # Left -> Root -> Right traversal pattern
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.key)
            self._inorder_recursive(current.right, result)
