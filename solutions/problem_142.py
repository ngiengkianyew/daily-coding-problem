def valid_paren(string, stack=list()):

    if not string and not stack:
        return True
    elif not string:
        return False

    cchar = string[0]
    remaining = string[1:]
    if cchar == '*':
        return \
            valid_paren('(' + remaining, stack) or \
            valid_paren(')' + remaining, stack) or \
            valid_paren(remaining, stack)

    cstack = stack.copy()
    if cchar == ')' and not stack:
        return False
    elif cchar == ')':
        cstack.pop()
    else:
        cstack.append(cchar)

    return valid_paren(remaining, cstack)


# Tests
assert valid_paren("(()*")
assert valid_paren("(*)")
assert not valid_paren(")*(")
