def get_col_rem_count(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    if rows == 1:
        return 0

    cols = len(matrix[0])

    col_drop_count = 0
    for i in range(cols):
        for k in range(1, rows):
            if matrix[k][i] < matrix[k-1][i]:
                col_drop_count += 1
                break

    return col_drop_count


assert get_col_rem_count(["cba", "daf", "ghi"]) == 1
assert get_col_rem_count(["abcdef"]) == 0
assert get_col_rem_count(["zyx", "wvu", "tsr"]) == 3
