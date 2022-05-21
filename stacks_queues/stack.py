from singly_linked_list import SinglyLinkedList
from node import Node

class Stack:
    def __init__(self):
        self.stack = SinglyLinkedList()
    
    def pop(self) -> Node:
        return self.stack.remove_from_head()

    def push(self, data):
        self.stack.add_to_head(data)

    def peek(self) -> Node:
        return self.stack.head
    
    def is_empty(self) -> bool:
        return self.stack.is_empty()