# Given two singly linked lists, determine if the two lists intersect. Return the intersecting node.

from singly_linked_list import SinglyLinkedList
from node import Node


def advance_ptr(ptr: Node, n: int) -> Node:
    for _ in range(n):
        ptr = ptr.next
    return ptr


def intersection(list_a: SinglyLinkedList, list_b: SinglyLinkedList) -> Node:
    a_current = list_a.head
    b_current = list_b.head

    if list_a.size > list_b.size:
        a_current = advance_ptr(a_current, list_a.size - list_b.size)
    else:
        b_current = advance_ptr(b_current, list_b.size - list_a.size)

    while a_current:
        if a_current.data == b_current.data:
            return a_current
        a_current = a_current.next
        b_current = b_current.next
    return None
