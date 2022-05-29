import unittest
from tree_node import TreeNode
from tree_traversals import preorder, inorder, postorder

class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(7)

    def test_preorder(self):
        self.assertEqual(preorder(self.root, []), [1, 2, 4, 5, 3, 6, 7])

    def test_inorder(self):
        self.assertEqual(inorder(self.root, []), [4, 2, 5, 1, 6, 3, 7])

    def test_postorder(self):
        self.assertEqual(postorder(self.root, []), [4, 5, 2, 6, 7, 3, 1])