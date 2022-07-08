# Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be after the elements less than x.
# The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

from singly_linked_list import SinglyLinkedList

def partition(linked_list: SinglyLinkedList, x: int) -> SinglyLinkedList:
    # Time: O(n), Space: O(n)
    current = linked_list.head
    less_than_x = SinglyLinkedList()
    greater_than_x = SinglyLinkedList()
    while current:
        if current.data < x:
            less_than_x.add_to_tail(current.data)
        else:
            greater_than_x.add_to_tail(current.data)
        current = current.next
    less_than_x.tail.next = greater_than_x.head

    return less_than_x
