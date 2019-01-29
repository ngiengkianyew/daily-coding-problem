def check_diagonal(start, matrix, val, rows, cols):
    if start[0] == rows or start[1] == cols:
        return True

    if matrix[start[0]][start[1]] == val:
        return check_diagonal((start[0] + 1, start[1] + 1), matrix, val, rows, cols)

    return False


def is_toeplitz(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for ind in range(rows):
        val = matrix[ind][0]
        if not check_diagonal((ind + 1, 1), matrix, val, rows, cols):
            return False

    for ind in range(1, cols):
        val = matrix[0][ind]
        if not check_diagonal((1, ind + 1), matrix, val, rows, cols):
            return False

    return True


# Tests
matrix = [[1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 4, 5, 1, 2]]
assert is_toeplitz(matrix)
matrix = [[1, 2, 3, 0, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 4, 5, 1, 2]]
assert not is_toeplitz(matrix)
