def merge_overlaps(intervals):
    interval_starts, interval_ends = set(), set()
    for start, end in intervals:
        interval_starts.add(start)
        interval_ends.add(end)

    min_start = min(interval_starts)
    max_end = max(interval_ends)
    current_active = 0
    instant_statuses = list([current_active])
    merged = list()
    for i in range(min_start, max_end + 1):
        if i in interval_ends:
            current_active -= 1
        if i in interval_starts:
            current_active += 1
        instant_statuses.append(current_active)

    start, end = None, None
    for i in range(len(instant_statuses)):
        if instant_statuses[i] and not instant_statuses[i-1]:
            start = i
        if not instant_statuses[i] and instant_statuses[i-1]:
            end = i
            merged.append((start, end))
            start, end = None, None
    return merged


assert merge_overlaps([(1, 3), (5, 8), (4, 10), (20, 25)]) == [
    (1, 3), (4, 10), (20, 25)]
assert merge_overlaps([(1, 3), (5, 8), (4, 10), (20, 25), (6, 12)]) == [
    (1, 3), (4, 12), (20, 25)]
