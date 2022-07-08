## TWo numbers represented by linked lists, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.

from node import Node
from singly_linked_list import SinglyLinkedList


def get_nodes_data(node_a, node_b) -> tuple[int, int]:
    a_data = node_a.data if node_a else 0
    b_data = node_b.data if node_b else 0
    return a_data, b_data


def get_next_nodes(node_a, node_b) -> tuple[Node]:
    a_next = node_a.next if node_a else None
    b_next = node_b.next if node_b else None
    return a_next, b_next


def sum_lists(list_a: SinglyLinkedList, list_b: SinglyLinkedList) -> SinglyLinkedList:
    # Time: O(n), Space: O(n)
    a_current = list_a.head
    b_current = list_b.head
    result = SinglyLinkedList()
    carry = 0
    while a_current or b_current:
        a_data, b_data = get_nodes_data(a_current, b_current)
        sum = a_data + b_data + carry
        carry = sum // 10
        result.add_to_tail(sum % 10)
        a_current, b_current = get_next_nodes(a_current, b_current)
    if carry:
        result.add_to_tail(carry)
    return result
