# Implementation of SinglyLinkedList class
from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_from_head(self) -> Node:
        if self.is_empty():
            return None
        head_node = self.head
        self.head = head_node.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return head_node
