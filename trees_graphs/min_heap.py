class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self.__bubble_up(len(self.heap) - 1)


    def get_min(self) -> int:
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def remove_min(self) -> int:
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__bubble_down(0)
        return min_value
    
    def __parent(self, index) -> int:
        return (index - 1) // 2

    def __left(self, index) -> int:
        return 2 * index + 1
    
    def __right(self, index) -> int:
        return 2 * index + 2
    
    def __has_left(self, index):
        return self.__left(index) < len(self.heap)
    
    def __has_right(self, index):
        return self.__right(index) < len(self.heap)
    
    def __bubble_up(self, index):
        while index > 0:
            parent = self.__parent(index)
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def __bubble_down(self, index):
        while self.__has_left(index):
            left_index = self.__left(index)
            smaller_child = left_index
            if self.__has_right(index):
                right_index = self.__right(index)
                if self.heap[right_index] < self.heap[left_index]:
                    smaller_child = right_index
            if self.heap[smaller_child] < self.heap[index]:
                self.heap[index], self.heap[smaller_child] = self.heap[smaller_child], self.heap[index]
            index = smaller_child
