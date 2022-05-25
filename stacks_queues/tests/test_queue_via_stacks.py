import unittest

from queue_via_stacks import MyQueue

class TestMyQueue(unittest.TestCase):
    def setUp(self):
        self.queue = MyQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek().data, 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue().data, 1)
        self.assertEqual(self.queue.dequeue().data, 2)

    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek().data, 1)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_dequeue_empty(self):
        self.assertEqual(self.queue.dequeue(), None)

    def test_peek_empty(self):
        self.assertEqual(self.queue.peek(), None)