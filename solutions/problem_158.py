class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord=(x={}, y={})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def get_adjacent_cells(coord, rows, cols):
    adj_cells = set()

    if coord.x > 0:
        adj_cells.add(Coord(coord.x-1, coord.y))
    if coord.x < rows - 1:
        adj_cells.add(Coord(coord.x+1, coord.y))
    if coord.y > 0:
        adj_cells.add(Coord(coord.x, coord.y-1))
    if coord.y < cols - 1:
        adj_cells.add(Coord(coord.x, coord.y+1))

    return adj_cells


def valid_path_helper(matrix, coord, rows, cols, current_path):
    if coord.x == rows - 1 and coord.y == cols - 1:
        # base case when already at bottom-right cell
        return 1

    # get adjacent cells as candidates
    adj_cells = get_adjacent_cells(coord, rows, cols)

    # exclude already traversed cells as candidates
    next_candidates = adj_cells - current_path

    # exclude wall cells (=1) as candidates
    next_candidates = [nc for nc in next_candidates if matrix[nc.x][nc.y] == 0]

    new_path = current_path.copy()
    new_path.add(coord)
    path_count = 0
    for cand in next_candidates:
        sub_path_count = valid_path_helper(
            matrix, cand, rows, cols, new_path)
        path_count += sub_path_count

    return path_count


def find_paths(matrix):
    num_paths = valid_path_helper(
        matrix, Coord(0, 0), len(matrix), len(matrix[0]), set())
    return num_paths


# Tests
matrix = [[0, 0, 1],
          [0, 0, 1],
          [1, 0, 0]]
assert find_paths(matrix) == 2

matrix = [[0, 0, 1],
          [1, 0, 1],
          [1, 0, 0]]
assert find_paths(matrix) == 1

matrix = [[0, 0, 0],
          [1, 1, 0],
          [0, 0, 0],
          [0, 1, 1],
          [0, 0, 0]]
assert find_paths(matrix) == 1

matrix = [[0, 0, 0],
          [1, 0, 0],
          [0, 0, 0],
          [0, 1, 1],
          [0, 0, 0]]
assert find_paths(matrix) == 4
