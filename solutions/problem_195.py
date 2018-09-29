def get_num_betn(matrix, i1, j1, i2, j2):
    num_1, num_2 = matrix[i1][j1], matrix[i2][j2]
    sm, lg = (num_1, num_2) if num_1 < num_2 else (num_2, num_1)
    count = 0
    for row in matrix:
        count += len([x for x in row if (x > sm and x < lg)])

    return count


# Tests
matrix = [
    [1, 2, 3, 4],
    [5, 8, 9, 13],
    [6, 10, 12, 14],
    [7, 11, 15, 16]
]
assert get_num_betn(matrix, 1, 3, 3, 1) == 1

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [10, 11, 12, 13],
    [20, 21, 22, 23]
]
assert get_num_betn(matrix, 1, 0, 3, 3) == 10
