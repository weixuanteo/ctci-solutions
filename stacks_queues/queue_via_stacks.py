# Implement a MyQueue class which implements a queue using two stacks.

from stack import Stack


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop().data)
        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop().data)
        return self.stack2.peek()

    def is_empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()
