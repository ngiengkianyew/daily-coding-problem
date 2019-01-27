from typing import List, Set


def get_closest_tower_dist(start: int, end: int, towers: Set[int], dist_so_far: int):
    if start in towers or end in towers:
        return dist_so_far

    return get_closest_tower_dist(start - 1, end + 1, towers, dist_so_far + 1)


def get_max_range(listeners: List[int], towers: List[int]):
    max_dist = 0
    for listener in listeners:
        closest_dist = get_closest_tower_dist(
            listener, listener, set(towers), 0)
        max_dist = max(max_dist, closest_dist)

    return max_dist


# Tests
assert get_max_range([1, 5, 11, 20], [4, 8, 15]) == 5
