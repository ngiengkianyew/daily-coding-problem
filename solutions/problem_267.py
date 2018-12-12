from enum import Enum


class Type(Enum):
    K = 0
    P = 1
    N = 2
    Q = 3
    R = 4
    B = 5


class Piece:
    def __init__(self, typ, loc):
        self.typ = typ
        self.loc = loc

    def __repr__(self):
        return "Piece=[type={}, loc={}]".format(self.typ, self.loc)


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Loc=[x={}, y={}]".format(self.x, self.y)


class Board:
    def __init__(self, matrix, pieces):
        self.matrix = matrix
        self.pieces = pieces


def read_board(board_str):
    rows = board_str.split("\n")
    pieces = list()
    king = None
    for i, row in enumerate(rows):
        for k, char in enumerate(row):
            if char == ".":
                continue

            pt = Type[char]
            loc = Location(i, k)
            piece = Piece(pt, loc)
            if pt == Type.K:
                king = piece
            else:
                pieces.append(piece)

    return king, pieces


def is_check_by_piece(kl, p):
    straight_attack = (p.loc.x == kl.x or p.loc.y == kl.y)

    dx = abs(p.loc.x - kl.x)
    dy = abs(p.loc.y - kl.y)
    diagonal_attack = (dx == dy)

    knight_attack = (dx * dy == 2)

    pawn_attack = (p.loc.y == kl.x - 1 or p.loc.y == kl.x + 1) and \
        p.loc.x == kl.x + 1

    if p.typ == Type.P:
        if pawn_attack:
            return True
    elif p.typ == Type.N:
        if knight_attack:
            return True
    elif p.typ == Type.R:
        if straight_attack:
            return True
    elif p.typ == Type.B:
        if diagonal_attack:
            return True
    elif p.typ == Type.Q:
        if straight_attack or diagonal_attack:
            return True


def in_check(board_str):
    king, pieces = read_board(board_str)

    for piece in pieces:
        if is_check_by_piece(king.loc, piece):
            print("In check by {}".format(piece))
            return True

    return False


# Tests
board_str = \
    "...K...." + "\n" + \
    "........" + "\n" + \
    ".B......" + "\n" + \
    "......P." + "\n" + \
    ".......R" + "\n" + \
    "..N....." + "\n" + \
    "........" + "\n" + \
    ".....Q.."
assert in_check(board_str)
