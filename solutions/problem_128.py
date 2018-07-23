def toh_helper(disks, source, inter, target):
    if disks == 1:
        target.append(source.pop())
    else:
        toh_helper(disks - 1, source, target, inter)
        print(source, inter, target)
        target.append(source.pop())
        print(source, inter, target)
        toh_helper(disks - 1, inter, source, target)

    print(source, inter, target)


def towers_of_hanoi(n):
    if not n:
        return

    print("{} Towers of Hanoi".format(n))
    stack_1, stack_2, stack_3 = \
        list(range(1, n + 1))[::-1], list(), list()
    toh_helper(n, stack_1, stack_2, stack_3)


towers_of_hanoi(3)
towers_of_hanoi(4)
towers_of_hanoi(5)
towers_of_hanoi(6)
