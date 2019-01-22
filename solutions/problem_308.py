SYMBOLS = {'|', '&', '^'}


class Boolean:
    def __init__(self, exp, val, fe, se):
        self.exp = exp
        self.val = val
        self.fe = fe
        self.se = se


def evaluator(arr):
    expr = "".join(arr)
    if len(arr) == 1 or len(arr) == 3:
        return [Boolean(expr, eval(expr), arr[0], arr[2] if len(arr) > 2 else None)]

    groupings = list()
    for i in range(len(arr) // 2):
        pivot = i*2 + 1
        first = arr[:pivot]
        second = arr[pivot + 1:]

        for fe in evaluator(first):
            for se in evaluator(second):
                new_exp = str(fe.val) + arr[pivot] + str(se.val)
                groupings.append(Boolean(
                    new_exp, eval(new_exp), fe, se))

    return groupings


def get_groupings(arr):
    if not arr:
        return []

    for ind in range(len(arr)):
        if arr[ind] == 'F':
            arr[ind] = 'False'
        elif arr[ind] == 'T':
            arr[ind] = 'True'
    groupings = evaluator(arr)
    return groupings


# Tests
assert len(get_groupings(['F', '|', 'T', '&', 'T'])) == 2
assert len(get_groupings(['F', '|', 'T', '&', 'T', '^', 'F'])) == 5
