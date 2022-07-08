# Use a single array to implement three stacks


class MultiStack:
    def __init__(self, num_of_stacks, stack_size):
        self.num_of_stacks = num_of_stacks
        self.stack_size = stack_size
        self.arr = [None] * (num_of_stacks * stack_size)
        self.sizes = [0] * num_of_stacks

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return None
        value = self.arr[self.index_of_top(stack_num)]
        self.arr[self.index_of_top(stack_num)] = None
        self.sizes[stack_num] -= 1
        return value

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception("Stack is full")
        self.sizes[stack_num] += 1
        self.arr[self.index_of_top(stack_num)] = value

    def index_of_top(self, stack_num):
        return stack_num * self.stack_size + self.sizes[stack_num] - 1
