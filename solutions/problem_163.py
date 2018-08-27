OPERATORS = {'+', '*', '/', '-'}


def evaluate_expression(exp_list):
    stack = list()

    for exp in exp_list:
        if exp in OPERATORS:
            op2 = stack.pop()
            op1 = stack.pop()
            ans = eval(str(op1) + exp + str(op2))
            stack.append(ans)
        else:
            stack.append(exp)

    return stack[0]


# Tests
assert evaluate_expression([5, 3, '+']) == 8
assert evaluate_expression(
    [15, 7, 1, 1, '+', '-', '/', 3, '*',
     2, 1, 1, '+', '+', '-']) == 5
