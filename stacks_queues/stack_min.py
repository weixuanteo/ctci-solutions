# Design a stack, which, in addition to push and pop, has a function min which returns the minimum element? 
# Push, pop and min should all operate in O(1) time.

from node_min import NodeMin
from singly_linked_list import SinglyLinkedList

class StackMin:
    def __init__(self):
        self.stack = SinglyLinkedList()
        self.min = None
        self.size = 0

    def push(self, data):
        new_node = NodeMin(data, data)
        if self.is_empty():
            self.min = data
        self.min = min(new_node.data, self.min)
        new_node.min = self.min
        self.stack.add_to_head(new_node)
        self.size += 1
    
    def pop(self) -> int:
        if self.is_empty():
            return None
        popped_node = self.stack.remove_from_head()
        self.size -= 1
        if self.is_empty():
            self.min = None
        else:
            self.min = min(self.stack.head.data.data, self.stack.head.data.min)
        return popped_node.data.data

    def get_min(self) -> int:
        return self.min
    
    def peek(self) -> int:
        return self.stack.head.data
    
    def is_empty(self) -> bool:
        return self.size == 0 