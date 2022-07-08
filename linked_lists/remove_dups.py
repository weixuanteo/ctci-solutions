# Write code to remove duplicates from an unsorted linked list.
from singly_linked_list import SinglyLinkedList


def remove_dups(linked_list: SinglyLinkedList) -> SinglyLinkedList:
    # Time Complexity: O(n), Space: O(n)
    seen = set()
    current = linked_list.head
    previous = None
    while current:
        if current.data in seen:
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current
        current = current.next

    return linked_list
