import random


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Position=[x={},y={}]".format(self.x, self.y)


def get_potential_knight_moves(start, size, visited):
    moves = list()
    moves.append(Position(start.x + 1, start.y + 2))
    moves.append(Position(start.x + 1, start.y - 2))
    moves.append(Position(start.x - 1, start.y + 2))
    moves.append(Position(start.x - 1, start.y - 2))
    moves.append(Position(start.x + 2, start.y + 1))
    moves.append(Position(start.x + 2, start.y - 1))
    moves.append(Position(start.x - 2, start.y + 1))
    moves.append(Position(start.x - 2, start.y - 1))

    valid_moves = [pos for pos in moves if
                   pos.x >= 0 and pos.x < size and
                   pos.y >= 0 and pos.y < size and
                   pos not in visited]

    return valid_moves


def run_knights_tour(start, size, visited):
    if len(visited) == size * size:
        return 1

    moves = get_potential_knight_moves(start, size, visited)

    count = 0
    for move in moves:
        tmp_visted = visited.copy()
        tmp_visted.add(move)
        count += run_knights_tour(move, size, tmp_visted)

    return count


def count_knights_tours(size):
    count = 0
    for i in range(size):
        for j in range(size):
            start = Position(i, j)
            count += run_knights_tour(start, size, set([start]))

    return count


assert count_knights_tours(1) == 1
assert count_knights_tours(2) == 0
assert count_knights_tours(3) == 0
assert count_knights_tours(4) == 0
assert count_knights_tours(5) == 1728
