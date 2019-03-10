# Not sure how a set of arrays provides advantages over a single array
# Regardless, their indices can be combined to act as a single large array


class Queue:
    def __init__(self, arr_size):
        self.flarr = [None for _ in range(arr_size)]
        self.start, self.end = 0, 0
        self.size = 0
        self.max_size = arr_size

    def enqueue(self, val):
        if self.size == self.max_size:
            # No more space
            return

        new_end = (self.end + 1) % self.max_size
        self.flarr[self.end] = val
        self.end = new_end
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            # Nothing to dequeue
            return None

        new_start = (self.start + 1) % self.max_size
        val = self.flarr[self.start]
        self.flarr[self.start] = None
        self.start = new_start
        self.size -= 1

        return val

    def get_size(self):
        return self.size


# Tests
q = Queue(5)
assert not q.dequeue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
assert q.get_size() == 3
assert q.flarr == [1, 2, 3, None, None]

assert q.dequeue() == 1
assert q.dequeue() == 2

q.enqueue(4)
q.enqueue(5)
assert q.get_size() == 3
assert q.flarr == [None, None, 3, 4, 5]

q.enqueue(6)
q.enqueue(7)
assert q.flarr == [6, 7, 3, 4, 5]

q.enqueue(8)
# no new value added
assert q.flarr == [6, 7, 3, 4, 5]
assert q.dequeue() == 3
assert q.dequeue() == 4
assert q.dequeue() == 5
assert q.dequeue() == 6
