class NumRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __hash__(self):
        return hash(self.start, self.end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


def add_number(num, starts, ends):
    if num + 1 in starts and num - 1 in ends:
        num_range_1 = ends[num - 1]
        num_range_2 = starts[num + 1]
        num_range = NumRange(num_range_1.start, num_range_2.end)
        starts[num_range.start] = num_range
        ends[num_range.end] = num_range
        del starts[num_range_2.start]
        del ends[num_range_1.end]
        return
    elif num + 1 in starts:
        num_range = starts[num + 1]
        num_range.start = num
        starts[num] = num_range
        del starts[num + 1]
        return
    elif num - 1 in ends:
        num_range = ends[num - 1]
        num_range.end = num
        ends[num] = num_range
        del ends[num - 1]
        return

    num_range = NumRange(num, num)
    starts[num] = num_range
    ends[num] = num_range


def get_seq_length(arr):
    starts = dict()
    ends = dict()

    for num in arr:
        add_number(num, starts, ends)

    max_len = 0
    for start in starts:
        num_range = starts[start]
        length = num_range.end - num_range.start + 1
        max_len = length if length > max_len else max_len

    return max_len


assert get_seq_length([100, 4, 200, 1]) == 1
assert get_seq_length([100, 4, 200, 1, 3]) == 2
assert get_seq_length([100, 4, 200, 1, 3, 2]) == 4
assert get_seq_length([100, 4, 200, 1, 3, 2, 5]) == 5
