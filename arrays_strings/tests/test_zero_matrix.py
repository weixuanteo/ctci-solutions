import unittest
from zero_matrix import zero_matrix, zero_matrix_efficient

class TestZeroMatrix(unittest.TestCase):
    
    def setUp(self):
        self.matrix1 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 11, 12],
            [13, 14, 15, 16]
        ]
        self.expected1 = [
            [1, 0, 3, 4],
            [5, 0, 7, 8],
            [0, 0, 0, 0],
            [13, 0, 15, 16]
        ]
        self.matrix2 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.expected2 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.matrix3 = [
            [1, 2, 3, 0],
            [5, 6, 7, 8],
            [9, 0, 11, 12],
            [13, 14, 15, 16]
        ]
        self.expected3 = [
            [0, 0, 0, 0],
            [5, 0, 7, 0],
            [0, 0, 0, 0],
            [13, 0, 15, 0]
        ]


    def test_zero_matrix(self):
        self.assertEqual(zero_matrix(self.matrix1), self.expected1)
        self.assertEqual(zero_matrix(self.matrix2), self.expected2)
        self.assertEqual(zero_matrix(self.matrix3), self.expected3)
    
    def test_zero_matrix_efficient(self):
        self.assertEqual(zero_matrix_efficient(self.matrix1), self.expected1)
        self.assertEqual(zero_matrix_efficient(self.matrix2), self.expected2)
        self.assertEqual(zero_matrix_efficient(self.matrix3), self.expected3)