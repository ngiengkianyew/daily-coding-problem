NOT_SYMBOL = "¬"
OR_SYMBOL = "OR"
AND_SYMBOL = "AND"


def get_solution(string, symbols):
    power = len(symbols)
    count_sol = 2 ** power

    sol = None
    for solution in range(count_sol):
        bin_rep = format(solution, '0' + str(power) + 'b')

        new_str = string[:]
        for i in range(power):
            val = str(bool(int(bin_rep[i])))
            new_str = new_str.replace(symbols[i], val)
            new_str = new_str.replace(NOT_SYMBOL, "not ")
            new_str = new_str.replace(OR_SYMBOL, "or")
            new_str = new_str.replace(AND_SYMBOL, "and ")

        if eval(new_str) == True:
            sol = bin_rep
            break

    if not sol:
        return None

    solution_map = dict()
    for i in range(power):
        solution_map[symbols[i]] = bool(int(sol[i]))
    return solution_map


# Tests
assert get_solution(
    "(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)",
    ['a', 'b', 'c']
) == {'a': False, 'b': True, 'c': True}
