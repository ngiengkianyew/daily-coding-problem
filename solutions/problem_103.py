from queue import Queue


def get_min_string(string, charset):
    curr_queue = list()
    ind_queue = list()
    curr_seen = set()

    candidate = None
    i = 0
    while i < len(string):
        if string[i] in charset:
            curr_queue.append(string[i])
            ind_queue.append(i)
            curr_seen.add(string[i])

        shift = 0
        for k in range(len(curr_queue)//2):
            if curr_queue[k] == curr_queue[-k-1]:
                shift += 1
        curr_queue = curr_queue[shift:]
        ind_queue = ind_queue[shift:]

        if len(curr_seen) == len(charset):
            if not candidate or len(candidate) > (ind_queue[-1] - ind_queue[0] + 1):
                candidate = string[ind_queue[0]:ind_queue[-1]+1]

        i += 1

    return candidate


assert not get_min_string("abcdedbc", {'g', 'f'})
assert get_min_string("abccbbbccbcb", {'a', 'b', 'c'}) == "abc"
assert get_min_string("figehaeci", {'a', 'e', 'i'}) == "aeci"
assert get_min_string("abcdedbc", {'d', 'b', 'b'}) == "db"
assert get_min_string("abcdedbc", {'b', 'c'}) == "bc"
assert get_min_string("abcdecdb", {'b', 'c'}) == "bc"
assert get_min_string("abcdecdb", {'b', 'c', 'e'}) == "bcde"
