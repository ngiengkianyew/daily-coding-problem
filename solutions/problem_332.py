def get_variables(m, n):
    candidates = list()
    for a in range(m // 2 + 1):
        b = m - a
        if a ^ b == n:
            candidates.append((a, b))

    return candidates


# Tests
assert get_variables(100, 4) == [(48, 52)]
