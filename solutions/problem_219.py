from enum import Enum

ROWS = 6
COLS = 7


class Color(Enum):
    RED = 1
    BLACK = 2


class Board:
    def __init__(self):
        self.grid = list()
        for _ in range(COLS):
            col = list()
            for _ in range(ROWS):
                col.append(None)
            self.grid.append(col)
        self.occupancy = [0] * COLS


class IllegalMove(Exception):
    pass


def play_piece(board, played_column, played_color):
    if board.occupancy[played_column] == 6:
        raise IllegalMove("Illegal move in this column")

    played_row = board.occupancy[played_column]
    board.grid[played_column][played_row] = played_color
    board.occupancy[played_column] += 1

    # check vertical
    consecutive = 0
    if len(board.grid[played_column]) > 4:
        for color in board.grid[played_column]:
            if color == played_color:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive == 4:
                return True

    # check horizontal
    consecutive = 0
    for i in range(COLS):
        color = board.grid[i][played_row]
        if color == played_color:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == 4:
            return True

    # check positive-slope diagonal
    consecutive = 0
    offset = min(played_column, played_row)
    col = played_column - offset
    row = played_row - offset
    while col < COLS and row < ROWS:
        color = board.grid[col][row]
        if color == played_color:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == 4:
            return True

    # check negative-slope diagonal
    consecutive = 0
    col = played_column + offset
    row = played_row - offset
    while col > 0 and row < ROWS:
        color = board.grid[col][row]
        if color == played_color:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == 4:
            return True

    return False


def play_game():

    board = Board()
    print("New board initialized")

    turn = 0
    players = [Color.RED, Color.BLACK]
    while True:
        player = players[turn % (len(players))]
        print("{}'s turn.".format(player))
        col_num = int(input("Enter a column number: "))

        try:
            won = play_piece(board, col_num, player)
        except IllegalMove as e:
            print(e)
            continue

        if won:
            print("{} wins".format(player))
            break

        turn += 1


play_game()
