def get_min_drops(N, k):
    if N == 0 or N == 1 or k == 1:
        return N

    possibilities = list()
    for i in range(1, N + 1):
        possibilities.append(
            max(get_min_drops(i-1, k-1),
                get_min_drops(N-i, k))
        )

    return min(possibilities) + 1


# Tests
assert get_min_drops(20, 2) == 6
assert get_min_drops(15, 3) == 5
