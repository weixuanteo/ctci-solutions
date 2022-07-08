import unittest
from bst_sequences import all_sequences, weave
from tree_node import TreeNode


class TestBSTSequences(unittest.TestCase):
    def test_all_sequences(self):
        tree1 = TreeNode(2)
        tree1.left = TreeNode(1)
        tree1.right = TreeNode(3)

        expected1 = [[2, 1, 3], [2, 3, 1]]
        result1 = all_sequences(tree1)
        self.assertEqual(result1, expected1)

    def test_weave(self):
        l1 = [1, 2]
        l2 = [3, 4]
        expected = [
            [1, 2, 3, 4],
            [1, 3, 2, 4],
            [1, 3, 4, 2],
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 4, 1, 2],
        ]
        result = weave(l1, l2, [], [])
        self.assertEqual(result, expected)
