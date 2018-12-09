def get_segments(arr):
    asc = arr[1] > arr[0]
    prev = arr[0]
    start = 0
    segments = []
    for i, num in enumerate(arr[1:]):
        if (asc and num < prev) or (not asc and num > prev):
            segments.append((asc, i - start + 1))
            start = i + 1
            asc = not asc

        prev = num

    segments.append((asc, len(arr) - start))

    return segments


def get_bonuses(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return [1]

    segments = get_segments(arr)
    bonuses = list()
    for segment in segments:
        asc, length = segment
        seg_bonuses = list(range(length))
        if not asc:
            seg_bonuses.reverse()
        bonuses.extend(seg_bonuses)

    bonuses = [x + 1 for x in bonuses]

    return bonuses


# Tests
assert get_bonuses([1000]) == [1]
assert get_bonuses([10, 40, 200, 1000, 60, 30]) == [1, 2, 3, 4, 2, 1]
assert get_bonuses([10, 40, 200, 1000, 900, 800, 30]) == [1, 2, 3, 4, 3, 2, 1]
