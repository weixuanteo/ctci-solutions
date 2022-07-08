# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def reverse_matrix(matrix):
    for m in matrix:
        m.reverse()


def transpose_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotate_matrix(matrix) -> list[list[int]]:
    # Time complexity: O(n^2), space complexity: O(1)

    transpose_matrix(matrix)
    reverse_matrix(matrix)

    return matrix
