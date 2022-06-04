import unittest
from min_heap import MinHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.min_heap = MinHeap()
        self.min_heap.insert(5)
        self.min_heap.insert(2)
        self.min_heap.insert(4)
        self.min_heap.insert(1)
        self.min_heap.insert(3)
    
    def test_get_min(self):
        self.assertEqual(self.min_heap.get_min(), 1)
    
    def test_remove_min(self):
        self.assertEqual(self.min_heap.remove_min(), 1)
        self.assertEqual(self.min_heap.remove_min(), 2)
        self.assertEqual(self.min_heap.remove_min(), 3)
        self.assertEqual(self.min_heap.remove_min(), 4)
        self.assertEqual(self.min_heap.remove_min(), 5)
        self.assertIsNone(self.min_heap.remove_min())
    
    