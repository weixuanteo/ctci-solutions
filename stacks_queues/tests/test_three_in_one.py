import unittest

from three_in_one import MultiStack

class TestMultiStack(unittest.TestCase):
    def setUp(self):
        self.stack = MultiStack(3, 3)

    def test_push_pop(self):
        self.stack.push(0, 1)
        self.stack.push(0, 2)
        self.stack.push(0, 3)
        self.stack.push(1, 4)
        self.stack.push(1, 5)
        self.stack.push(2, 6)
        self.stack.push(2, 7)
        self.stack.push(2, 8)
        self.assertEqual(self.stack.pop(0), 3)
        self.assertEqual(self.stack.pop(1), 5)
        self.assertEqual(self.stack.pop(2), 8)
        self.assertEqual(self.stack.pop(0), 2)
        self.assertEqual(self.stack.pop(1), 4)
        self.assertEqual(self.stack.pop(2), 7)
        self.assertEqual(self.stack.pop(0), 1)
        self.assertEqual(self.stack.pop(2), 6)
        self.assertEqual(self.stack.pop(0), None)
        self.assertEqual(self.stack.pop(1), None)
        self.assertEqual(self.stack.pop(2), None)
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty(0))
        self.assertTrue(self.stack.is_empty(1))
        self.assertTrue(self.stack.is_empty(2))
        self.stack.push(0, 1)
        self.stack.push(1, 2)
        self.stack.push(2, 3)
        self.assertFalse(self.stack.is_empty(0))
        self.assertFalse(self.stack.is_empty(1))
        self.assertFalse(self.stack.is_empty(2))
    
    def test_is_full(self):
        self.assertFalse(self.stack.is_full(0))
        self.assertFalse(self.stack.is_full(1))
        self.assertFalse(self.stack.is_full(2))
        self.stack.push(0, 1)
        self.stack.push(0, 2)
        self.stack.push(0, 3)
        self.stack.push(1, 4)
        self.stack.push(1, 5)
        self.stack.push(1, 6)
        self.stack.push(2, 7)
        self.stack.push(2, 8)
        self.stack.push(2, 9)
        self.assertTrue(self.stack.is_full(0))
        self.assertTrue(self.stack.is_full(1))
        self.assertTrue(self.stack.is_full(2))
