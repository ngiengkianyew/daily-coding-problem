import sys
from random import randint

cache = dict()


def get_collatz_seq(num, prev=list()):
    prev.append(num)

    if num in cache:
        return prev + cache[num]

    if num == 1:
        return prev

    if num % 2 == 0:
        num //= 2
    else:
        num = 3*num + 1

    return get_collatz_seq(num, prev)


# Tests
experiments = 10
for _ in range(experiments):
    num = randint(1, sys.maxsize)
    cs = get_collatz_seq(num)
    assert cs[-1] == 1


def get_longest_collatz(limit):
    longest_cs, length = None, -1
    for num in range(1, limit + 1):
        if num in cache:
            cs = cache[num]
        else:
            cs = get_collatz_seq(num)
            cache[num] = cs
        if len(cs) > length:
            length = len(cs)
            longest_cs = cs

    return longest_cs


print(len(get_longest_collatz(100)))
