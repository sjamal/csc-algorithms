"""Singly Linked List data structure supporting traversal, insertion, and reversal."""

from typing import List, Optional


class ListNode:
    """Represents a single structural node within a Singly Linked List."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional["ListNode"] = None


class SinglyLinkedList:
    """Pointer-chained sequential collection supporting O(1) append/prepend and O(n) traversal.

    Complexity Analysis:
        Time Complexity: O(1) for prepend/append (head/tail tracked), O(n) for
            search, delete, and reversal.
        Space Complexity: O(n) for n stored nodes.
    """

    def __init__(self) -> None:
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def prepend(self, value: int) -> None:
        """Inserts a new value at the front of the list in O(1) time."""
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def append(self, value: int) -> None:
        """Inserts a new value at the end of the list in O(1) time."""
        new_node = ListNode(value)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def search(self, value: int) -> bool:
        """Returns True if `value` exists anywhere within the list."""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def delete(self, value: int) -> bool:
        """Removes the first occurrence of `value`; returns True if a node was removed."""
        previous: Optional[ListNode] = None
        current = self.head

        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                # Fix up the tail pointer if the removed node was the last one
                if current is self.tail:
                    self.tail = previous

                self._size -= 1
                return True

            previous = current
            current = current.next

        return False

    def reverse(self) -> None:
        """Reverses the list in place in O(n) time using iterative pointer rewiring."""
        previous: Optional[ListNode] = None
        current = self.head
        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def to_list(self) -> List[int]:
        """Returns the list's values as a standard Python list, head to tail."""
        values: List[int] = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values
