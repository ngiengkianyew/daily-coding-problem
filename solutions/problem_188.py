# Unchanged code prints 3, 3, 3
# To make it print 1, 2, 3, use the following version


def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(i):
            print(i)
        flist.append((print_i, i))

    return flist


functions = make_functions()
for f, i in functions:
    f(i)
