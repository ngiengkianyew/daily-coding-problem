def extendable_row(matrix, erow, scol, ecol):
    return all(matrix[erow][scol:ecol])


def extendable_col(matrix, ecol, srow, erow):
    for row in range(srow, erow):
        if not matrix[row][ecol]:
            return False

    return True


def area_helper(matrix, num_rows, num_cols, srow, erow, scol, ecol):
    current_area = (erow - srow) * (ecol - scol)
    row_ex_area, col_ex_area = 0, 0

    ex_row = erow < num_rows and extendable_row(matrix, erow, scol, ecol)
    if ex_row:
        row_ex_area = area_helper(matrix, num_rows, num_cols,
                                  srow, erow + 1, scol, ecol)

    ex_col = ecol < num_cols and extendable_col(matrix, ecol, srow, erow)
    if ex_col:
        col_ex_area = area_helper(matrix, num_rows, num_cols,
                                  srow, erow, scol, ecol + 1)

    return max(current_area, row_ex_area, col_ex_area)


def get_largest_area(matrix):
    max_area = 0
    if not matrix:
        return max_area

    num_rows, num_cols = len(matrix), len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            upper_bound_area = (num_rows - i) * (num_cols - j)
            if matrix[i][j] and upper_bound_area > max_area:
                area = area_helper(
                    matrix, num_rows, num_cols, i, i + 1, j, j + 1)
                max_area = area if area > max_area else max_area

    return max_area


# Tests

matrix = [[1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 0, 0]]
assert get_largest_area(matrix) == 4


matrix = [[1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 1, 1]]
assert get_largest_area(matrix) == 6

matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]
assert get_largest_area(matrix) == 16

matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
assert get_largest_area(matrix) == 0

matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 0, 0],
          [0, 0, 0, 0]]
assert get_largest_area(matrix) == 8

matrix = [[1, 1, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]]
assert get_largest_area(matrix) == 4
