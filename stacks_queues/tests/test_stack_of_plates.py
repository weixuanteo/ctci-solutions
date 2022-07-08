import unittest

from stack_of_plates import SetOfStacks


class TestSetOfStacks(unittest.TestCase):
    def setUp(self):
        self.sos = SetOfStacks(3)

    def test_push_pop(self):
        self.sos.push(1)
        self.sos.push(2)
        self.sos.push(3)
        self.sos.push(4)
        self.sos.push(5)
        self.assertEqual(self.sos.pop(), 5)
        self.assertEqual(self.sos.pop(), 4)
        self.assertEqual(self.sos.pop(), 3)
        self.assertEqual(self.sos.pop(), 2)
        self.assertEqual(self.sos.pop(), 1)
        self.assertEqual(self.sos.pop(), None)

    def test_push_pop_peek(self):
        self.sos.push(1)
        self.sos.push(2)
        self.sos.push(3)
        self.sos.push(4)
        self.assertEqual(self.sos.peek(), 4)
        self.assertEqual(self.sos.pop(), 4)
        self.assertEqual(self.sos.peek(), 3)
        self.assertEqual(self.sos.pop(), 3)
        self.assertEqual(self.sos.peek(), 2)
        self.assertEqual(self.sos.pop(), 2)
        self.assertEqual(self.sos.peek(), 1)
        self.assertEqual(self.sos.pop(), 1)
        self.assertEqual(self.sos.peek(), None)
        self.assertEqual(self.sos.pop(), None)

    def test_pop_at(self):
        self.sos.push(1)
        self.sos.push(2)
        self.sos.push(3)
        self.sos.push(4)
        self.sos.push(5)
        self.assertEqual(self.sos.pop_at(0), 3)
        self.assertEqual(self.sos.pop_at(0), 2)
        self.assertEqual(self.sos.pop_at(1), 5)
        self.assertEqual(self.sos.pop_at(1), 4)
        self.assertEqual(self.sos.pop_at(0), 1)
