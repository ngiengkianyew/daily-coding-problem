def get_longest_uqsub(arr, seen=set()):
    if not arr:
        return len(seen)

    curr = arr[0]
    if curr in seen:
        return len(seen)

    seen_cp = seen.copy()
    seen_cp.add(curr)

    return max(get_longest_uqsub(arr[1:], seen_cp), 
               get_longest_uqsub(arr[1:]))



# Tests
assert get_longest_uqsub([]) == 0
assert get_longest_uqsub([5, 5, 5]) == 1
assert get_longest_uqsub([5, 1, 3, 5, 2, 3, 4, 1]) == 5
assert get_longest_uqsub([5, 1, 3, 5, 2, 3, 4]) == 4
assert get_longest_uqsub([5, 1, 3, 5, 2, 3]) == 4
