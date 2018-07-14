import sys


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return "[{}-{}]".format(self.start, self.end)


def get_smallest_stab_set_helper(remaining_intervals, used_points,
                                 remaining_points, num_to_intervals):

    if not remaining_intervals:
        return used_points

    min_len = sys.maxsize
    smallest_stab_set = None
    for current_point in remaining_points:
        if current_point not in num_to_intervals:
            continue

        current_point_intervals = num_to_intervals[current_point]
        new_rem_intervals = remaining_intervals - current_point_intervals

        new_used_points = used_points.copy()
        new_used_points.add(current_point)
        new_rem_points = remaining_points.copy()
        new_rem_points.remove(current_point)

        stab_set = get_smallest_stab_set_helper(
            new_rem_intervals, new_used_points, new_rem_points, num_to_intervals)
        if len(stab_set) < min_len:
            smallest_stab_set = stab_set
            min_len = len(stab_set)

    return smallest_stab_set


def get_smallest_stab_set(interval_tuples):
    intervals = set()
    num_to_intervals = dict()

    endpoints = set()
    for (start, end) in interval_tuples:
        endpoints.add(end)

        interval = Interval(start, end)
        intervals.add(interval)

        for num in range(start, end + 1):
            if num not in num_to_intervals:
                num_to_intervals[num] = set()
            num_to_intervals[num].add(interval)

    smallest_stab_set = get_smallest_stab_set_helper(
        intervals, set(), endpoints, num_to_intervals)

    return smallest_stab_set


assert get_smallest_stab_set([[0, 3]]) == {3}
assert get_smallest_stab_set([[0, 3], [2, 6]]) == {3}
assert get_smallest_stab_set([[0, 3], [2, 6], [3, 4]]) == {3}
assert get_smallest_stab_set([[0, 3], [2, 6], [3, 4], [6, 7]]) == {3, 6}
assert get_smallest_stab_set([[0, 3], [2, 6], [3, 4], [6, 9]]) == {3, 9}
assert get_smallest_stab_set([[0, 3], [2, 6], [3, 4], [6, 100]]) == {3, 100}
