import unittest

from stack_min import StackMin


class TestStackMin(unittest.TestCase):
    def setUp(self):
        self.stack = StackMin()

    def test_min(self):
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(4)
        self.assertEqual(self.stack.get_min(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 5)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), None)
