import math


def calculate_distance(source, target):
    return math.sqrt(
        (source[0] - target[0]) ** 2 +
        (source[1] - target[1]) ** 2
    )


def get_closest_points(source, targets, k):
    if k >= len(targets):
        return targets

    closest_points = \
        sorted(targets, key=lambda x: calculate_distance(source, x))[:k]

    return closest_points



# Tests
assert calculate_distance((0, 0), (3, 4)) == 5
assert get_closest_points(
    (1, 2), [(0, 0), (5, 4), (3, 1)], 2) == [(0, 0), (3, 1)]
