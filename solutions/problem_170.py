import sys

chars = set("abcdefghijklmnopqrstuvwxyz")


def transition_helper(start, end, dictionary, changes, seen):
    if start == end:
        return changes

    candidates = list()
    for index, _ in enumerate(start):
        for char in chars:
            candidate = start[:index] + char + start[index + 1:]
            if candidate in dictionary and candidate not in seen:
                candidates.append(candidate)

    min_results = list()
    min_len = sys.maxsize
    for candidate in candidates:
        new_seen = seen.copy()
        new_seen.add(candidate)
        result_changes = transition_helper(
            candidate, end, dictionary, changes + [candidate], new_seen)
        if result_changes and len(result_changes) < min_len:
            min_len = len(result_changes)
            min_results = result_changes

    return min_results


def get_transition(start, end, dictionary):
    result = transition_helper(start, end, dictionary, [start], {start})
    return result


# Tests
assert get_transition("dog", "cat", {"dot", "dop", "dat", "cat"}) == \
    ["dog", "dot", "dat", "cat"]
assert not get_transition("dog", "cat", {"dot", "tod", "dat", "dar"})
