# Implementation of stack with size limit

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
    
    def is_full(self):
        return self.top == self.size - 1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, data):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = data
    
    def pop(self):
        if self.is_empty():
            return None
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value
