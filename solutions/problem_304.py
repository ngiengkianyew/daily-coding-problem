from typing import Set, List


BOARD_SIZE = 8
POSSIBLE_MOVES = 8
CACHE = dict()
KNIGHT_RANGE = [-2, -1, 1, 2]


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return "Pos[x={},y={}]".format(self.x, self.y)

    def is_valid(self) -> bool:
        return self.x > 0 and self.x <= BOARD_SIZE and self.y > 0 and self.y <= BOARD_SIZE


def get_valid_moves(start: Position) -> Set[Position]:
    if start in CACHE:
        return CACHE[start]

    candidates = set()
    for hor in KNIGHT_RANGE:
        for ver in KNIGHT_RANGE:
            if abs(hor) + abs(ver) == 3:
                candidates.add(Position(start.x + hor, start.y + ver))
    val_candidates = [pos for pos in candidates if pos.is_valid()]

    CACHE[start] = val_candidates

    return val_candidates


def explore(start: Position, turns: int, counts: List) -> None:
    if not turns:
        return

    valid_moves = get_valid_moves(start)
    counts[0] += POSSIBLE_MOVES
    counts[1] += len(valid_moves)

    for next_pos in valid_moves:
        explore(next_pos, turns - 1, counts)


def get_prob_remain(start: Position, turns: int) -> float:
    global CACHE
    CACHE = dict()

    counts = [0, 0]
    explore(start, turns, counts)

    return counts[1] / counts[0]


# Tests
assert get_prob_remain(Position(4, 4), 1) == 1.0
assert get_prob_remain(Position(1, 1), 3) < 0.66
