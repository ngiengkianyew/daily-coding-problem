def cons(a, b):
    return lambda f: f(a, b)

def car(f):
    z = lambda x, y: x
    return f(z)

def cdr(f):
    z = lambda x, y: y
    return f(z)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
