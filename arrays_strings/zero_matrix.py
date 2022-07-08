# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zero_row(matrix, row):
    matrix[row] = [0] * len(matrix[row])

def zero_col(matrix, col):
    for row in range(len(matrix)):
        matrix[row][col] = 0

def zero_matrix(matrix) -> list[list[int]]:
    # Time complexity: O(n*m), Space complexity: O(m*n)
    zero_indexes = set()
    seen_row = set()
    seen_col = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zero_indexes.add((row, col))
    
    for zero_index in zero_indexes:
        row, col = zero_index
        if row not in seen_row:
            zero_row(matrix, row)
            seen_row.add(row)
        if col not in seen_col:
            zero_col(matrix, col)
            seen_col.add(col)

    return matrix

def is_first_row_with_zero(matrix) -> bool:
    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            return True
    return False

def is_first_col_with_zero(matrix) -> bool:
    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            return True
    return False

def zero_matrix_efficient(matrix):
    # Time complexity: O(n*m), Space complexity: O(1)
    first_row_with_zero = is_first_row_with_zero(matrix)
    first_col_with_zero = is_first_col_with_zero(matrix)

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            zero_row(matrix, row)

    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            zero_col(matrix, col)
    
    if first_row_with_zero:
        zero_row(matrix, 0)
    if first_col_with_zero:
        zero_col(matrix, 0)

    return matrix
