# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

def delete_middle_node(node) -> None:
    if not node or not node.next:
        return
    node.data = node.next.data
    node.next = node.next.next
