BOARD_DIM = 9
GRID_DIM = 3


def get_grid_details(x, y):
    grid_row = x - (x % GRID_DIM)
    grid_col = y - (y % GRID_DIM)
    return grid_row, grid_col


def solveSudokuHelper(board, row_elements, col_elements, grid_elements):

    for i in range(BOARD_DIM):
        for k in range(BOARD_DIM):
            if board[i][k] == ".":
                grid_row, grid_col = get_grid_details(i, k)
                grid_key = "{}-{}".format(grid_row, grid_col)
                for m in range(1, BOARD_DIM + 1):
                    if str(m) not in row_elements[i] and \
                            str(m) not in col_elements[k] and \
                            str(m) not in grid_elements[grid_key]:
                        board[i][k] = str(m)
                        row_elements[i].add(str(m))
                        col_elements[k].add(str(m))
                        grid_elements[grid_key].add(str(m))
                        if solveSudokuHelper(
                                board, row_elements, col_elements, grid_elements):
                            return True
                        else:
                            board[i][k] = "."
                            row_elements[i].remove(str(m))
                            col_elements[k].remove(str(m))
                            grid_elements[grid_key].remove(str(m))
                return False
    return True


def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    row_elements = dict()
    col_elements = dict()
    grid_elements = dict()

    for i in range(BOARD_DIM):
        row_elements[i] = set()
        col_elements[i] = set()

    for i in range(BOARD_DIM):
        for k in range(BOARD_DIM):
            if not i % GRID_DIM and not k % GRID_DIM:
                grid_elements["{}-{}".format(i, k)] = set()

    for i in range(BOARD_DIM):
        for k in range(BOARD_DIM):
            if board[i][k].isnumeric():
                row_elements[i].add(board[i][k])
                col_elements[k].add(board[i][k])

                grid_row, grid_col = get_grid_details(i, k)
                grid_elements[
                    "{}-{}".format(grid_row, grid_col)].add(board[i][k])

    solveSudokuHelper(board, row_elements,
                      col_elements, grid_elements)


sudoku_board_1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
solveSudoku(sudoku_board_1)
print(sudoku_board_1)
