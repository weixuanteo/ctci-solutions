import unittest
from list_of_depths import *

class TestListOfDepths(unittest.TestCase):
    def setUp(self):
        self.tree = TreeNode(1)
        self.tree.left = TreeNode(2)
        self.tree.right = TreeNode(3)
        self.tree.left.left = TreeNode(4)
        self.tree.left.right = TreeNode(5)
        self.tree.right.left = TreeNode(6)
        self.tree.right.right = TreeNode(7)
        self.tree.right.right.right = TreeNode(8)

    def test_create_level_linked_lists(self):
        result = create_level_linked_lists(self.tree)
        self.assertEqual(len(result), 4)
        self.assertEqual([r.val for r in result[0]], [1])
        self.assertEqual([r.val for r in result[1]], [2, 3])
        self.assertEqual([r.val for r in result[2]], [4, 5, 6, 7])
        self.assertEqual([r.val for r in result[3]], [8])
    
    def test_create_level_linked_lists_recursive(self):
        result = []
        create_level_linked_lists_recursive(self.tree, result, 0)
        self.assertEqual(len(result), 4)
        self.assertEqual([r.val for r in result[0].to_list()], [1])
        self.assertEqual([r.val for r in result[1].to_list()], [2, 3])
        self.assertEqual([r.val for r in result[2].to_list()], [4, 5, 6, 7])
        self.assertEqual([r.val for r in result[3].to_list()], [8])