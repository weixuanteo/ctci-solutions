# Implement an algorithm to find the kth to last element of a singly linked list.
# k = 1 (last element), k = 2 (second to last element), etc.

from singly_linked_list import SinglyLinkedList

def return_kth_to_last(linked_list: SinglyLinkedList, k: int) -> int:
    # Time complexity: O(n), Space complexity: O(k)
    stack = []
    current = linked_list.head

    while current:
        stack.append(current)
        current = current.next
        if len(stack) > k:
            stack.pop(0)

    if len(stack) != k:
        return None
    return stack[0].data

def return_kth_to_last_ptr(linked_list: SinglyLinkedList, k: int) -> int:
    # Time complexity: O(n), Space complexity: O(1)
    ptr1 = linked_list.head
    ptr2 = linked_list.head

    for _ in range(k):
        if not ptr1:
            return None
        ptr1 = ptr1.next

    while ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr2.data
