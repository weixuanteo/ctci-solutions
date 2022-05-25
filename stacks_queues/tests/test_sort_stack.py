import unittest
from sort_stack import SortStack

class TestSortStack(unittest.TestCase):
    def setUp(self):
        self.stack = SortStack()
        self.stack.push(6)
        self.stack.push(7)
        self.stack.push(4)
        self.stack.push(2)
        self.stack.push(1)
    
    def test_sort(self):
        self.stack.sort()
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 6)
        self.assertEqual(self.stack.pop(), 7)
        self.assertEqual(self.stack.pop(), None)