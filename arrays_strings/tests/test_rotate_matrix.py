import unittest
from rotate_matrix import rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(rotate_matrix(matrix), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(
            rotate_matrix(matrix),
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]],
        )
