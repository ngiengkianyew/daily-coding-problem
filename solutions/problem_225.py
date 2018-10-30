def last_exec(n, k):
    last_exec = None
    next_exec_index = 0

    prisoners = list(range(1, n + 1))

    while prisoners:
        next_exec_index = (next_exec_index + k - 1) % len(prisoners)
        last_exec = prisoners[next_exec_index]
        prisoners = prisoners[:next_exec_index] + \
            prisoners[next_exec_index + 1:]

    return last_exec


# Tests
assert last_exec(5, 2) == 3
assert last_exec(3, 2) == 3
assert last_exec(5, 3) == 4
