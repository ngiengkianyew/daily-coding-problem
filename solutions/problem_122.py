def get_max_coins_helper(matrix, crow, ccol, rows, cols):
    cval = matrix[crow][ccol]

    if crow == rows - 1 and ccol == cols - 1:
        return cval

    down, right = cval, cval
    if crow < rows - 1:
        down += get_max_coins_helper(
            matrix, crow + 1, ccol, rows, cols)
    if ccol < cols - 1:
        right += get_max_coins_helper(
            matrix, crow, ccol + 1, rows, cols)

    return max(down, right)


def get_max_coins(matrix):
    if matrix:
        return get_max_coins_helper(
            matrix, 0, 0, len(matrix), len(matrix[0]))


coins = [[0, 3, 1, 1],
         [2, 0, 0, 4],
         [1, 5, 3, 1]]
assert get_max_coins(coins) == 12

coins = [[0, 3, 1, 1],
         [2, 8, 9, 4],
         [1, 5, 3, 1]]
assert get_max_coins(coins) == 25
