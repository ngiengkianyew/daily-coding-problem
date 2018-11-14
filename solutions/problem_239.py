class Dialpad:
    def __init__(self):
        self.nodes = set(range(1, 10))
        self.edges = dict()
        self.edges[1] = {2, 4}
        self.edges[2] = {1, 3, 5}
        self.edges[3] = {2, 6}
        self.edges[4] = {1, 5, 7}
        self.edges[5] = {2, 4, 6, 8}
        self.edges[6] = {3, 5, 9}
        self.edges[7] = {4, 8}
        self.edges[8] = {5, 7, 9}
        self.edges[9] = {6, 8}


def count_code_helper(dp, code_len, curr, seen):
    if code_len == 0:
        return 1

    seen_cp = seen.copy()
    seen_cp.add(curr)

    nodes = dp.edges[curr]
    sub_count = 0
    for node in nodes:
        sub_count += count_code_helper(dp, code_len - 1, node, seen_cp)

    return sub_count


def count_codes(dp, code_len):
    if code_len == 1:
        return len(dp.nodes)

    count = 0
    for node in dp.nodes:
        count += count_code_helper(dp, code_len, node, set())

    return count


# Tests
dp = Dialpad()
assert count_codes(dp, 1) == 9
assert count_codes(dp, 2) == 68
assert count_codes(dp, 3) == 192
