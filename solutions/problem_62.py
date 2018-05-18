def matrix_traversal_helper(row_count, col_count, curr_row, curr_col):

    if curr_row == row_count - 1 and curr_col == col_count - 1:
        return 1

    count = 0
    if curr_row < row_count - 1:
        count += matrix_traversal_helper(row_count, col_count,
                                         curr_row + 1, curr_col)
    if curr_col < col_count - 1:
        count += matrix_traversal_helper(row_count, col_count,
                                         curr_row, curr_col + 1)

    return count


def get_matrix_traversals(row_count, col_count):
    if not row_count or not col_count:
        return None
    count = matrix_traversal_helper(row_count, col_count, 0, 0)
    return count


assert not get_matrix_traversals(1, 0)
assert get_matrix_traversals(1, 1) == 1
assert get_matrix_traversals(2, 2) == 2
assert get_matrix_traversals(5, 5) == 70
