# assuming only integers > 0 are allowed


def reaches_last_helper(arr, start_index, target_index):
    if start_index == target_index:
        return True

    hop = arr[start_index]
    if not hop or (start_index + hop > target_index):
        return False

    return reaches_last_helper(arr, start_index + hop, target_index)


def reaches_last(arr):
    return reaches_last_helper(arr, 0, len(arr) - 1)


assert reaches_last([2, 0, 1, 0])
assert not reaches_last([1, 1, 0, 1])
assert not reaches_last([2, 1])
