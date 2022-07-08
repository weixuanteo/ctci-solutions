import unittest
from check_balanced import is_balanced
from tree_node import TreeNode


class TestCheckBalanced(unittest.TestCase):
    def setUp(self):
        self.tree1 = TreeNode(1)
        self.tree1.left = TreeNode(2)
        self.tree1.right = TreeNode(3)
        self.tree1.left.left = TreeNode(4)
        self.tree1.left.right = TreeNode(5)
        self.tree1.right.left = TreeNode(6)
        self.tree1.right.right = TreeNode(7)

        self.tree2 = TreeNode(1)
        self.tree2.left = TreeNode(2)
        self.tree2.left.left = TreeNode(3)

        self.tree3 = TreeNode(1)

    def test_is_balanced(self):
        self.assertTrue(is_balanced(self.tree1))
        self.assertFalse(is_balanced(self.tree2))
        self.assertTrue(is_balanced(self.tree3))
