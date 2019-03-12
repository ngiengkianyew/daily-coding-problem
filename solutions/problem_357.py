def get_continuous_count(string, char):
    count, max_count = 1, 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count - 1


def get_tree_depth(string):
    c1 = get_continuous_count(string, "(")
    c2 = get_continuous_count(string, ")")
    return max(c1, c2)


# Tests
assert get_tree_depth("(00)") == 0
assert get_tree_depth("((00)(00))") == 1
assert get_tree_depth("((((00)0)0)0)") == 3
