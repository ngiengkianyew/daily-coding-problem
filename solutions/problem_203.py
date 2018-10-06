def get_smallest(arr, start, end):
    mid = start + ((end - start) // 2)

    if arr[start] <= arr[mid]:
        if arr[end] < arr[mid]:
            return get_smallest(arr, mid + 1, end)
        else:
            return arr[start]
    elif arr[start] >= arr[mid]:
        if arr[end] > arr[mid]:
            return get_smallest(arr, start, end)
        else:
            return arr[end]


def get_smallest_helper(arr):
    smallest = get_smallest(arr, 0, len(arr) - 1)
    return smallest


# Tests
assert get_smallest_helper([5, 7, 10, 3, 4]) == 3
assert get_smallest_helper([4, 5, 7, 10, 3]) == 3
assert get_smallest_helper([3, 4, 5, 7, 10]) == 3
