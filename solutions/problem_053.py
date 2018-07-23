class Queue:
    def __init__(self):
        self.main_stack = list()
        self.aux_stack = list()

    def __repr__(self):
        return str(self.main_stack)

    def enqueue(self, val):
        self.main_stack.append(val)

    def dequeue(self):
        if not self.main_stack:
            return None

        while self.main_stack:
            self.aux_stack.append(self.main_stack.pop())
        val = self.aux_stack.pop()
        while self.aux_stack:
            self.main_stack.append(self.aux_stack.pop())
        return val


q = Queue()
q.enqueue(1)
assert q.main_stack == [1]
q.enqueue(2)
assert q.main_stack == [1, 2]
q.enqueue(3)
assert q.main_stack == [1, 2, 3]
val = q.dequeue()
assert val == 1
assert q.main_stack == [2, 3]
val = q.dequeue()
assert val == 2
assert q.main_stack == [3]
