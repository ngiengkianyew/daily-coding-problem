def find_peak(arr):
    if not arr:
        return None

    mid = len(arr) // 2

    if mid > 0 and arr[mid] > arr[mid - 1] and \
            mid < len(arr) and arr[mid] > arr[mid + 1]:
        return arr[mid]

    if mid > 0 and arr[mid] > arr[mid - 1]:
        return find_peak(arr[:mid])

    return find_peak(arr[mid + 1:])


# Tests
assert find_peak([0, 2, 4, 5, 3, 1]) == 5
