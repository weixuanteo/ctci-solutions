import unittest
from binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.add(5)
        self.bst.add(3)
        self.bst.add(7)
        self.bst.add(2)
        self.bst.add(4)
        self.bst.add(6)
        self.bst.add(8)
        
    def test_contains(self):
        self.assertTrue(self.bst.contains(5))
        self.assertTrue(self.bst.contains(3))
        self.assertTrue(self.bst.contains(7))
        self.assertTrue(self.bst.contains(2))
        self.assertTrue(self.bst.contains(4))
        self.assertTrue(self.bst.contains(6))
        self.assertTrue(self.bst.contains(8))
        self.assertFalse(self.bst.contains(1))
        self.assertFalse(self.bst.contains(9))
        self.assertFalse(self.bst.contains(0))
        self.assertFalse(self.bst.contains(-1))
        self.assertFalse(self.bst.contains(10))

    def test_search(self):
        self.assertEqual(self.bst.search(5).val, 5)
        self.assertEqual(self.bst.search(3).val, 3)
        self.assertEqual(self.bst.search(7).val, 7)
        self.assertEqual(self.bst.search(2).val, 2)
        self.assertEqual(self.bst.search(4).val, 4)
        self.assertEqual(self.bst.search(6).val, 6)
        self.assertEqual(self.bst.search(8).val, 8)
        self.assertEqual(self.bst.search(1), None)
        self.assertEqual(self.bst.search(9), None)
        self.assertEqual(self.bst.search(0), None)
        self.assertEqual(self.bst.search(-1), None)
        self.assertEqual(self.bst.search(10), None)