# no idea how to implement it using 3 stacks
# the time complexity constraints can be satisfied
# using a deque instead

from collections import deque

# Tests
dq = deque()
dq.appendleft(1)
dq.appendleft(2)
dq.appendleft(3)
dq.appendleft(4)
dq.appendleft(5)
assert dq.pop() == 1
assert dq.popleft() == 5
