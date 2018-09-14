from queue import Queue


def interleave_stack(stack, queue, index=1):
    for _ in range(len(stack) - index):
        que.put(stack.pop())

    while que.qsize():
        stk.append(que.get())

    if len(stack) - index > 1:
        interleave_stack(stack, queue, index + 1)


# Tests
stk = [1, 2, 3, 4, 5]
que = Queue()
interleave_stack(stk, que)
assert stk == [1, 5, 2, 4, 3]

stk = [1, 2, 3, 4]
que = Queue()
interleave_stack(stk, que)
assert stk == [1, 4, 2, 3]
