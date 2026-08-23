"""Self-balancing Binary Search Tree implementation using AVL rotation mechanics."""

from typing import List, Optional


class AVLNode:
    """Represents a single structural node within an AVL Tree."""

    def __init__(self, key: int) -> None:
        self.key: int = key
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height: int = 1


class AVLTree:
    """Height-balanced Binary Search Tree guaranteeing O(log n) depth via rotations."""

    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def insert(self, key: int) -> None:
        """Inserts a new numerical key, rebalancing ancestor nodes as needed."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current: Optional[AVLNode], key: int) -> AVLNode:
        # Standard BST insertion descending left/right by key comparison
        if not current:
            return AVLNode(key)
        if key < current.key:
            current.left = self._insert_recursive(current.left, key)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key)
        else:
            # Duplicate keys are ignored to preserve set-like uniqueness
            return current

        return self._rebalance(current)

    def delete(self, key: int) -> None:
        """Removes a numerical key from the tree, rebalancing ancestor nodes as needed."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(
        self, current: Optional[AVLNode], key: int
    ) -> Optional[AVLNode]:
        # Base case: key does not exist within this subtree
        if not current:
            return None

        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            # Single or no child: promote the remaining child directly
            if not current.left:
                return current.right
            if not current.right:
                return current.left

            # Two children: splice in the in-order successor (smallest of right subtree)
            successor = current.right
            while successor.left:
                successor = successor.left
            current.key = successor.key
            current.right = self._delete_recursive(current.right, successor.key)

        return self._rebalance(current)

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """Recomputes height and applies rotations to restore the AVL balance invariant."""
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance_factor(node)

        # Left-heavy subtree requiring a right (or left-right) rotation
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-heavy subtree requiring a left (or right-left) rotation
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        pivot = node.right
        node.right = pivot.left
        pivot.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        pivot.height = 1 + max(self._height(pivot.left), self._height(pivot.right))
        return pivot

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        pivot = node.left
        node.left = pivot.right
        pivot.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        pivot.height = 1 + max(self._height(pivot.left), self._height(pivot.right))
        return pivot

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _balance_factor(self, node: Optional[AVLNode]) -> int:
        return self._height(node.left) - self._height(node.right) if node else 0

    def search(self, key: int) -> bool:
        """Returns True if the key exists within the tree, False otherwise."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current: Optional[AVLNode], key: int) -> bool:
        if not current:
            return False
        if current.key == key:
            return True
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    def inorder_traversal(self) -> List[int]:
        """Returns the keys sorted in ascending order using inorder traversal."""
        result: List[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current: Optional[AVLNode], result: List[int]) -> None:
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.key)
            self._inorder_recursive(current.right, result)
