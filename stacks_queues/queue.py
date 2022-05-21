# Implementation of a queue using a linked list

from singly_linked_list import SinglyLinkedList
from node import Node

class Queue:
    def __init__(self):
        self.queue = SinglyLinkedList()
    
    def enqueue(self, data):
        self.queue.add_to_tail(data)
    
    def dequeue(self) -> Node:
        return self.queue.remove_from_head()
    
    def peek(self) -> Node:
        return self.queue.head
    
    def is_empty(self) -> bool:
        return self.queue.is_empty()