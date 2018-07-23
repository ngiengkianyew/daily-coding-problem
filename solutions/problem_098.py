def check_new_coordinate(word, row, col, used_coordinates):
    expected_char = word[0]
    copy_coordinates = used_coordinates.copy()
    char = board[row][col]
    result = False
    if expected_char == char and "{}-{}".format(row, col) not in copy_coordinates:
        copy_coordinates.add("{}-{}".format(row, col))
        result = existence_helper(
            word[1:], board, row, col, copy_coordinates)
    return result


def existence_helper(word, board, crow, ccol, used_coordinates):
    if not word:
        return True

    top, bottom, left, right = (False, False, False, False)
    if crow > 0:
        top = check_new_coordinate(word, crow - 1, ccol, used_coordinates)
    if crow < len(board) - 1:
        bottom = check_new_coordinate(word, crow + 1, ccol, used_coordinates)
    if ccol > 0:
        left = check_new_coordinate(word, crow, ccol - 1, used_coordinates)
    if ccol < len(board[0]) - 1:
        right = check_new_coordinate(word, crow, ccol + 1, used_coordinates)

    return top or bottom or left or right


def exists(board, word):
    if not word:
        return False

    first_char = word[0]
    result = False
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == first_char:
                result = result or existence_helper(
                    word[1:], board, row, col, set(["{}-{}".format(row, col)]))

    return result


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
assert exists(board, "ABCCED")
assert exists(board, "SEE")
assert not exists(board, "ABCB")
