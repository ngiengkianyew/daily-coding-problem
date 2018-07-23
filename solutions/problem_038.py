def is_valid(board, row):
    if row in board:
        return False

    column = len(board)
    for occupied_column, occupied_row in enumerate(board):
        if abs(occupied_row - row) == abs(occupied_column - column):
            return False

    return True


def get_queen_configurations(board, n):
    if n == len(board):
        return 1

    count = 0
    for row in range(n):
        if is_valid(board, row):
            count += get_queen_configurations(board + [row], n)

    return count


assert not is_valid([0, 2], 0)
assert not is_valid([0, 2], 2)
assert is_valid([0, 8], 3)
assert not is_valid([1, 3], 2)
assert is_valid([], 1)

assert get_queen_configurations([], 2) == 0
assert get_queen_configurations([], 4) == 2
assert get_queen_configurations([], 5) == 10
assert get_queen_configurations([], 8) == 92
