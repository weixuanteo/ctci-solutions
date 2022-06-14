import unittest
from successor import find_successor
from tree_node import TreeNode

class TestSuccessor(unittest.TestCase):
    def setUp(self):
        self.tree1 = TreeNode(4)
        self.tree1.left = TreeNode(2)
        self.tree1.left.parent = self.tree1
        self.tree1.left.left = TreeNode(1)
        self.tree1.left.left.parent = self.tree1.left
        self.tree1.left.right = TreeNode(3)
        self.tree1.left.right.parent = self.tree1.left
        self.tree1.right = TreeNode(6)
        self.tree1.right.parent = self.tree1
        self.tree1.right.left = TreeNode(5)
        self.tree1.right.left.parent = self.tree1.right
        self.tree1.right.right = TreeNode(7)
        self.tree1.right.right.parent = self.tree1.right
        self.tree1.right.right.right = TreeNode(10)
        self.tree1.right.right.right.parent = self.tree1.right.right
        self.tree1.right.right.right.left = TreeNode(9)
        self.tree1.right.right.right.left.parent = self.tree1.right.right.right
        self.tree1.right.right.right.left.left = TreeNode(8)
        self.tree1.right.right.right.left.left.parent = self.tree1.right.right.right.left

    def test_find_successor(self):
        self.assertEqual(find_successor(self.tree1.right).val, 7)
        self.assertEqual(find_successor(self.tree1.left.left).val, 2)
        self.assertIsNone(find_successor(self.tree1.right.right.right))