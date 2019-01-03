COLORS = {"R", "G", "B"}


def get_odd_man(col_a, col_b):
    return list(COLORS - set([col_a, col_b]))[0]


def minimize(quixes):
    stack = list()
    for quix in quixes:
        if not stack or stack[-1] == quix:
            stack.append(quix)
            continue

        new = get_odd_man(quix, stack[-1])
        stack.pop()
        stack.append(new)
        while len(stack) > 1 and stack[-1] != stack[-2]:
            a, b = stack.pop(), stack.pop()
            stack.append(get_odd_man(a, b))

    return stack


# Tests
assert minimize(["R", "G", "B", "G", "B"]) == ["R"]
