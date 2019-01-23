import sys
from itertools import permutations


def get_people_indices(arr):
    return set([x for x, y in enumerate(arr) if y == 1])


def get_min_dist(vacant_spots, available_people):
    min_dist = sys.maxsize
    perms = list(permutations(range(len(vacant_spots))))
    for perm in perms:
        dist = 0
        for i in range(len(vacant_spots)):
            k = perm[i]
            dist += abs(vacant_spots[i] - available_people[k])
        min_dist = min(min_dist, dist)
    return min_dist


def get_lowest_cost(arr):
    num_people = sum(arr)
    ovr_people_indices = set([x for x, y in enumerate(arr) if y == 1])

    lowest_cost = sys.maxsize
    for offset in range(len(arr) - num_people + 1):
        subarr = arr[offset:offset + num_people]
        all_indices = set([offset + x for x in range(num_people)])
        people_indices = set([offset + x for x in get_people_indices(subarr)])

        vacant_indices = list(all_indices - people_indices)
        occupied_ovr_indices = list(ovr_people_indices - people_indices)

        lowest_cost = min(lowest_cost, get_min_dist(
            vacant_indices, occupied_ovr_indices))

    return lowest_cost


# Tests
assert get_lowest_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]) == 5
