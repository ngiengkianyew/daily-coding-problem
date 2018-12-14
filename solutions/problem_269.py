def get_new_orientation_helper(dominos):
    changes = 0
    new_dominos = dominos.copy()

    for i in range(len(dominos)):
        if dominos[i] == 'L' and i > 0 and dominos[i-1] == '.' and dominos[i-2] != 'R':
            new_dominos[i-1] = 'L'
            changes += 1
        elif dominos[i] == 'R' and i < len(dominos) - 1 and dominos[i+1] == '.' and dominos[i+2] != 'L':
            new_dominos[i+1] = 'R'
            changes += 1

    return get_new_orientation_helper(new_dominos) if changes else dominos


def get_new_orientation(dominos):
    arr = list(dominos)
    arr = get_new_orientation_helper(arr)
    return "".join(arr)


# Tests
assert get_new_orientation(".L.R....L") == "LL.RRRLLL"
assert get_new_orientation("..R...L.L") == "..RR.LLLL"
