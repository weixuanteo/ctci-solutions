# Imagine a stack of plates. 
# If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. 
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack 
# (that is, pop() should return the same values as it would if there were just a single stack).

class SetOfStacks:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.current_stack = 0
    
    def push(self, data):
        if self.is_empty() or self.is_current_stack_full():
            self.stacks.append([])
            self.current_stack += 1
        self.stacks[self.current_stack - 1].append(data)
    
    def pop(self):
        if self.is_empty():
            return None
        if self.is_current_stack_empty():
            self.current_stack -= 1
            self.stacks.pop()
        if self.is_empty():
            return None
        return self.stacks[self.current_stack - 1].pop()
    
    def peek(self):
        if self.is_current_stack_empty():
            self.current_stack -= 1
            self.stacks.pop()
        if self.is_empty():
            return None
        return self.stacks[self.current_stack - 1][-1]

    def pop_at(self, index: int):
        if index > self.current_stack:
            return None
        return self.stacks[index].pop()
    
    def is_empty(self) -> bool:
        return len(self.stacks) == 0

    def is_current_stack_empty(self) -> bool:
        return len(self.stacks[self.current_stack - 1]) == 0

    def is_current_stack_full(self) -> bool:
        return len(self.stacks[self.current_stack - 1]) == self.capacity