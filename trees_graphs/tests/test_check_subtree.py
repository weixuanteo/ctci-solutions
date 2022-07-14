import unittest

from tree_node import TreeNode
from check_subtree import is_subtree, is_same_tree

class TestCheckSubtree(unittest.TestCase):
    def setUp(self):
        self.tree1 = TreeNode(1)
        self.tree1.left = TreeNode(2)
        self.tree1.right = TreeNode(3)

        self.tree2 = TreeNode(1)
        self.tree2.left = TreeNode(2)

        self.tree3 = TreeNode(2)
        self.tree3.left = TreeNode(2)
        self.tree3.left.left = TreeNode(2)

        self.tree4 = TreeNode(2)
        self.tree4.left = TreeNode(2)


    def test_is_same_tree(self):
        self.assertTrue(is_same_tree(self.tree1, self.tree1))
        self.assertFalse(is_same_tree(self.tree1, self.tree2))

    def test_is_subtree(self):
        self.assertFalse(is_subtree(self.tree1, self.tree2))
        self.assertFalse(is_subtree(self.tree1, self.tree3))
        self.assertTrue(is_subtree(self.tree3, self.tree4))