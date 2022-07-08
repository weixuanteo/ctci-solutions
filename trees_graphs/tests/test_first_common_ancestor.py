import unittest
from first_common_ancestor import first_common_ancestor
from tree_node import TreeNode


class TestFirstCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.tree1 = TreeNode(1)
        self.tree1.left = TreeNode(2)
        self.tree1.left.parent = self.tree1
        self.tree1.right = TreeNode(3)
        self.tree1.right.parent = self.tree1
        self.tree1.left.left = TreeNode(0)
        self.tree1.left.left.parent = self.tree1.left
        self.tree1.left.right = TreeNode(4)
        self.tree1.left.right.parent = self.tree1.left
        self.tree1.left.left.left = TreeNode(9)
        self.tree1.left.left.left.parent = self.tree1.left.left
        self.tree1.right.left = TreeNode(7)
        self.tree1.right.left.parent = self.tree1.right
        self.tree1.right.right = TreeNode(8)
        self.tree1.right.right.parent = self.tree1.right

        self.tree2 = TreeNode(1)
        self.tree2.left = TreeNode(2)
        self.tree2.left.parent = self.tree2
        self.tree2.left.left = TreeNode(0)
        self.tree2.left.left.parent = self.tree2.left

    def test_first_common_ancestor(self):
        self.assertEqual(
            first_common_ancestor(self.tree1.left.left.left, self.tree1.left.right).val,
            2,
        )
        self.assertEqual(
            first_common_ancestor(self.tree1.left.left.left, self.tree1.right).val, 1
        )
        self.assertEqual(
            first_common_ancestor(self.tree2.left, self.tree2.left.left).val, 2
        )

    def test_invalid_first_common_ancestor(self):
        self.assertEqual(
            first_common_ancestor(
                self.tree1.left.left.left, self.tree1.left.right.left
            ),
            None,
        )
