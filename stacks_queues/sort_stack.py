# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.


class SortStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def sort(self):
        temp_stack = SortStack()
        while not self.is_empty():
            temp = self.pop()
            while not temp_stack.is_empty() and temp_stack.peek() > temp:
                self.push(temp_stack.pop())
            temp_stack.push(temp)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
