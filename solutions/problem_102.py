def get_cont_arr(arr, target):
    summed = 0

    start, end = 0, 0
    i = 0
    while i < len(arr):
        if summed == target:
            return arr[start:end]
        elif summed > target:
            summed -= arr[start]
            start += 1
        else:
            summed += arr[i]
            end = i + 1
            i += 1


assert get_cont_arr([1, 2, 3, 4, 5], 0) == []
assert get_cont_arr([1, 2, 3, 4, 5], 1) == [1]
assert get_cont_arr([1, 2, 3, 4, 5], 5) == [2, 3]
assert get_cont_arr([5, 4, 3, 4, 5], 12) == [5, 4, 3]
assert get_cont_arr([5, 4, 3, 4, 5], 11) == [4, 3, 4]
assert get_cont_arr([1, 2, 3, 4, 5], 9) == [2, 3, 4]
assert get_cont_arr([1, 2, 3, 4, 5], 3) == [1, 2]
