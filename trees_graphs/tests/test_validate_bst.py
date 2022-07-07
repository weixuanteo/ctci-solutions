import unittest
from validate_bst import is_bst
from tree_node import TreeNode

class TestValidateBST(unittest.TestCase):
    def setUp(self):
        self.tree1 = TreeNode(5)
        self.tree1.left = TreeNode(3)
        self.tree1.right = TreeNode(7)
        self.tree1.left.left = TreeNode(2)
        self.tree1.left.right = TreeNode(4)
        self.tree1.right.left = TreeNode(6)
        self.tree1.right.right = TreeNode(8)

        self.tree2 = TreeNode(5)
        self.tree2.left = TreeNode(3)
        self.tree2.right = TreeNode(7)
        self.tree2.left.left = TreeNode(8)
        self.tree2.left.right = TreeNode(4)

        self.tree3 = None

        self.tree4 = TreeNode(5)
        self.tree4.left = TreeNode(4)
        self.tree4.right = TreeNode(6)
        self.tree4.right.left = TreeNode(3)
        self.tree4.right.right = TreeNode(7)

        self.tree5 = TreeNode(2)
        self.tree5.left = TreeNode(2)
        self.tree5.right = TreeNode(2)
    
    def test_is_bst(self):
        self.assertTrue(is_bst(self.tree1))
        self.assertFalse(is_bst(self.tree2))
        self.assertTrue(is_bst(self.tree3))
        self.assertFalse(is_bst(self.tree4))
        self.assertFalse(is_bst(self.tree5))