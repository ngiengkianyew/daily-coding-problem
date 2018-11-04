from collections import Counter
from queue import Queue


def rearrange(string):
    c = Counter(string)
    sitems = sorted(c.items(), key=lambda x: x[1], reverse=True)

    strlen = len(string)
    if strlen % 2:
        if sitems[0][1] > (strlen // 2) + 1:
            return None
    else:
        if sitems[0][1] > (strlen // 2):
            return None

    q = Queue()
    for item in sitems:
        q.put(item)

    new_str = ""
    while not q.empty():
        item = q.get()
        new_str += item[0]
        item = (item[0], item[1] - 1)
        if item[1]:
            q.put(item)

    return new_str


# Tests
assert rearrange("aaabbc") == "abcaba"
assert rearrange("aaab") == None
