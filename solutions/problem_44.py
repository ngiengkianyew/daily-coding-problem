def merge(a_with_inv, b_with_inv):
    i, k = 0, 0
    merged = list()
    a, a_inv = a_with_inv
    b, b_inv = b_with_inv
    inversions = a_inv + b_inv

    while i < len(a) and k < len(b):
        if a[i] < b[k]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[k])
            inversions += len(a[i:])
            k += 1

    while i < len(a):
        merged.append(a[i])
        i += 1
    while k < len(b):
        merged.append(b[k])
        k += 1

    return merged, inversions


def merge_sort(arr):
    if not arr or len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    merged_array, inversions = merge(
        merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    return merged_array, inversions


def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions


assert count_inversions([1, 2, 3, 4, 5]) == 0
assert count_inversions([2, 1, 3, 4, 5]) == 1
assert count_inversions([2, 4, 1, 3, 5]) == 3
assert count_inversions([2, 6, 1, 3, 7]) == 3
assert count_inversions([5, 4, 3, 2, 1]) == 10
