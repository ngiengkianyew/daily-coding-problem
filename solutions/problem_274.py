def eval_string(expr_string):
    return eval(expr_string)


# Tests
assert eval_string("-1 + (2 + 3)") == 4
