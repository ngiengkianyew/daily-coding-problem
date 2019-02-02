FINAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
]


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def get_adj_nums(empty_pos, num_rows, num_cols):
    adj_nums = set()
    if empty_pos.x > 0:
        if empty_pos.y > 0:
            adj_nums.add(Coord(empty_pos.x - 1, empty_pos.y - 1))
        if empty_pos.y < num_cols - 1:
            adj_nums.add(Coord(empty_pos.x - 1, empty_pos.y + 1))
    if empty_pos.y < num_rows - 1:
        if empty_pos.y > 0:
            adj_nums.add(Coord(empty_pos.x + 1, empty_pos.y - 1))
        if empty_pos.y < num_cols - 1:
            adj_nums.add(Coord(empty_pos.x + 1, empty_pos.y + 1))

    return adj_nums


def play(grid, empty_pos, num_rows, num_cols):
    if grid == FINAL_STATE:
        return

    adj_nums = get_adj_nums(empty_pos, num_rows, num_cols)
    for adj_num in adj_nums:
        new_grid = grid.copy()
        new_grid[empty_pos.x][empty_pos.y] = grid[adj_num.x][adj_num.y]
        new_grid[adj_num.x][adj_num.y] = None
        return play(new_grid, adj_num, num_rows, num_cols)


def win_game(grid):
    empty_pos = None
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if not val:
                empty_pos = Coord(x, y)

    play(grid, empty_pos, len(start), len(start[0]))


# Tests
start = [
    [1, 2, 3],
    [4, 5, None],
    [7, 8, 6]
]
assert win_game(start)
