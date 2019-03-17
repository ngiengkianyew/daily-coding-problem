def add(x, y=1):
    return lambda z: add(x+(y*z), (-1*y)) if z else x


# Tests
assert add(7)(None) == 7
assert add(1)(2)(3)(None) == 0
assert add(-5)(10)(3)(9)(None) == 11
