# Check if a linked list is a palindrome
from singly_linked_list import SinglyLinkedList


def reverse_linked_list(linked_list: SinglyLinkedList) -> SinglyLinkedList:
    reversed = SinglyLinkedList()
    current = linked_list.head
    while current:
        reversed.add_to_head(current.data)
        current = current.next
    return reversed


def is_palindrome(linked_list: SinglyLinkedList) -> bool:
    reversed = reverse_linked_list(linked_list)
    current = linked_list.head
    reversed_current = reversed.head
    while current:
        if current.data != reversed_current.data:
            return False
        current = current.next
        reversed_current = reversed_current.next
    return True
