def get_row_word(matrix, word_len, rows, x, y):
    row_chars = list()
    for i in range(word_len):
        row_chars.append(matrix[x + i][y])

    return "".join(row_chars)


def get_col_word(matrix, word_len, cols, x, y):
    return "".join(matrix[x][y:y + word_len])


def word_checker(matrix, word, word_len, rows, cols, x, y):

    if x >= rows or y >= cols:
        return False

    row_word, col_word = None, None
    if x + word_len <= rows and y < cols:
        row_word = get_row_word(matrix, word_len, rows, x, y)
    if y + word_len <= cols and x < rows:
        col_word = get_col_word(matrix, word_len, cols, x, y)

    if row_word == word or col_word == word:
        return True

    check_1 = word_checker(matrix, word, word_len, rows, cols, x + 1, y) \
        if col_word else None
    check_2 = word_checker(matrix, word, word_len, rows, cols, x, y + 1) \
        if row_word else None

    return check_1 or check_2


def word_exists(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)

    return word_checker(matrix, word, word_len, rows, cols, 0, 0)


matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

assert not word_exists(matrix, "FOAMS")
assert word_exists(matrix, "FOAM")
assert word_exists(matrix, "MASS")
assert not word_exists(matrix, "FORM")
