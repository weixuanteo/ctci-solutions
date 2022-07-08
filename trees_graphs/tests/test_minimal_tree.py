import unittest
from minimal_tree import construct_minimal_tree


class TestMinimalTree(unittest.TestCase):
    def setUp(self):
        self.elements1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.elements2 = [1]
        self.elements3 = [1, 2]
        self.elements4 = []

    def test_construct_minimal_tree(self):
        tree1 = construct_minimal_tree(self.elements1)
        tree2 = construct_minimal_tree(self.elements2)
        tree3 = construct_minimal_tree(self.elements3)
        tree4 = construct_minimal_tree(self.elements4)

        self.assertEqual(
            tree1.get_structure_by_levels(), [6, 3, 9, 2, 5, 8, 10, 1, 4, 7]
        )
        self.assertEqual(tree2.get_structure_by_levels(), [1])
        self.assertEqual(tree3.get_structure_by_levels(), [2, 1])
        self.assertEqual(tree4.get_structure_by_levels(), [])
