def get_longest_inc_subsq(arr):
    longest = []
    start = 0
    for i in range(len(arr)):
        if arr[i] < arr[i - 1]:
            start = i
        end = i + 1

        if end - start > len(longest):
            longest = arr[start:end]

    return longest


# Tests
assert get_longest_inc_subsq([1, 2, 3, 5, 4]) == [1, 2, 3, 5]
assert get_longest_inc_subsq([5, 4, 3, 2, 1]) == [5]
