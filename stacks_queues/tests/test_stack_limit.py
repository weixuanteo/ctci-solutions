import unittest

from stack_limit import Stack

class TestStackLimit(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(3)
    
    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.pop(), None)
    
    def test_is_full(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertFalse(self.stack.is_full())
        self.stack.push(3)
        self.assertTrue(self.stack.is_full())
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
