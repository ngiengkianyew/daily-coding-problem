def get_intersections(parr, qarr):
    segments = list(zip(parr, qarr))

    count = 0
    for i in range(len(segments)):
        for k in range(i):
            p1, p2 = segments[i], segments[k]
            if (p1[0] < p2[0] and p1[1] > p2[1]) or \
                    (p1[0] > p2[0] and p1[1] < p2[1]):
                count += 1

    return count


# Tests
assert get_intersections([1, 4, 5], [4, 2, 3]) == 2
assert get_intersections([1, 4, 5], [2, 3, 4]) == 0
