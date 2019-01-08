import sys


def get_shortest_path(
        target, elevations, path_map, path_so_far,
        elevations_so_far, distance, switches):

    if 0 == target and path_so_far:
        return path_so_far, distance if switches < 2 else sys.maxsize

    min_dist, min_path = sys.maxsize, None
    for src, dist in path_map[target]:
        if src == target:
            continue

        new_switches = switches + 1 \
            if elevations_so_far and elevations[src] > elevations_so_far[0] \
            else switches

        new_path_so_far, new_dist = get_shortest_path(
            src, elevations, path_map, [src] + path_so_far,
            [elevations[target]] + elevations_so_far, distance + dist, new_switches)

        if new_dist < min_dist:
            min_dist = new_dist
            min_path = new_path_so_far

    return min_path, min_dist


def get_shortest_path_helper(elevations, paths):
    path_map = dict()
    for (src, tgt), dist in paths.items():
        if tgt not in path_map:
            path_map[tgt] = list()
        path_map[tgt].append((src, dist))

    shortest_path, _ = get_shortest_path(
        0, elevations, path_map, list(), list(), 0, 0)

    return shortest_path


# Tests
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10,
}
assert get_shortest_path_helper(elevations, paths) == [0, 2, 4]
