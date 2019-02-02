from sys import maxsize


def check_string(string, start, end, unique_chars):
    substr = string[start:end]
    if start == end or len(set(substr)) < unique_chars:
        return maxsize

    can_1 = check_string(string, start, end - 1, unique_chars)
    can_2 = check_string(string, start + 1, end, unique_chars)

    return min(len(substr), min(can_1, can_2))


def get_longest_distinct_window(string):
    if not string:
        return 0

    return check_string(string, 0, len(string), len(set(string)))


# Tests
assert get_longest_distinct_window("jiujitsu") == 5
assert get_longest_distinct_window("jiujiuuts") == 6
