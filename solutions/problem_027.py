brace_map = {
    ")": "(",
    "}": "{",
    "]": "["
}


def is_balanced(s):
    stack = list()
    for char in s:
        if stack and char in brace_map and stack[-1] == brace_map[char]:
            stack.pop()
        else:
            stack.append(char)
    return not stack


assert is_balanced("")
assert is_balanced("{}")
assert is_balanced("([])")
assert is_balanced("([])[]({})")
assert not is_balanced("(")
assert not is_balanced("]")
assert not is_balanced("((()")
assert not is_balanced("([)]")
