import sys
from heapq import heappush, heappop


class Stack:

    def __init__(self):
        self.counter = sys.maxsize
        self.stack = list()

    def push(self, item):
        heappush(self.stack, (self.counter, item))
        self.counter -= 1

    def pop(self):
        if not self.stack:
            return None

        _, item = heappop(self.stack)
        return item


# Tests
stk = Stack()
stk.push(1)
stk.push(7)
stk.push(4)
assert stk.pop() == 4
stk.push(2)
assert stk.pop() == 2
assert stk.pop() == 7
assert stk.pop() == 1
assert not stk.pop()
