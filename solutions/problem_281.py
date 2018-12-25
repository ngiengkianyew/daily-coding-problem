from collections import Counter


def get_min_cuts(brick_wall):

    for i in range(len(brick_wall)):
        # Make wall of cumulative brick lengths
        prev_bricks_len = 0
        for k in range(len(brick_wall[i])):
            brick_wall[i][k] += prev_bricks_len
            prev_bricks_len = brick_wall[i][k]
        brick_wall[i] = brick_wall[i][:-1]

    # Find the most common edge to cut down through
    brick_counter = Counter()
    for row in brick_wall:
        brick_counter.update(row)

    most_common_bricks = brick_counter.most_common()
    bricks_avoided = most_common_bricks[0][1] if most_common_bricks else 0

    return len(brick_wall) - bricks_avoided


# Tests
brick_wall = [[3, 5, 1, 1],
              [2, 3, 3, 2],
              [5, 5],
              [4, 4, 2],
              [1, 3, 3, 3],
              [1, 1, 6, 1, 1]]
assert get_min_cuts(brick_wall) == 2

brick_wall = [[1]]
assert get_min_cuts(brick_wall) == 1

brick_wall = [[1],
              [1, 2]]
assert get_min_cuts(brick_wall) == 1

brick_wall = [[1, 2],
              [1, 2]]
assert get_min_cuts(brick_wall) == 0
