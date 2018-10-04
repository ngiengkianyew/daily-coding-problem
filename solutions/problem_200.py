def get_stab_points(intervals):
    starts, ends = zip(*intervals)
    return (min(ends), max(starts))


# Tests
assert get_stab_points([(1, 4), (4, 5), (7, 9), (9, 12)]) == (4, 9)
assert get_stab_points([(1, 4), (-2, 6), (4, 5), (7, 9), (9, 12)]) == (4, 9)
assert get_stab_points([(1, 4), (-2, 0), (4, 5), (7, 9)]) == (0, 7)
