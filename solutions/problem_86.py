def get_chars_removed_helper(string, stack, removed):

    if not string and not stack:
        return removed
    elif not string:
        return len(stack) + removed

    if string[0] == ')' and stack and stack[-1] == '(':
        stack.pop()
        return get_chars_removed_helper(string[1:], stack, removed)

    removed_chars_add = get_chars_removed_helper(
        string[1:], stack + [string[0]], removed)
    removed_chars_ignore = get_chars_removed_helper(
        string[1:], stack, removed + 1)

    return min(removed_chars_add, removed_chars_ignore)


def get_chars_removed(string):
    chars_removed = get_chars_removed_helper(string, list(), 0)
    return chars_removed


assert get_chars_removed("()())()") == 1
assert get_chars_removed(")(") == 2
assert get_chars_removed("()(((") == 3
assert get_chars_removed(")()(((") == 4
