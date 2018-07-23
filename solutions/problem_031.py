def get_edit_distance(s1, s2):
    if s1 == s2:
        return 0
    elif not s1:
        return len(s2)
    elif not s2:
        return len(s1)

    if s1[0] == s2[0]:
        return get_edit_distance(s1[1:], s2[1:])

    return 1 + min(
        get_edit_distance(s1[1:], s2),      # deletion from s1
        get_edit_distance(s1, s2[1:]),      # addition to s1
        get_edit_distance(s1[1:], s2[1:]))  # modification to s1


assert get_edit_distance("", "") == 0
assert get_edit_distance("a", "b") == 1
assert get_edit_distance("abc", "") == 3
assert get_edit_distance("abc", "abc") == 0
assert get_edit_distance("kitten", "sitting") == 3
