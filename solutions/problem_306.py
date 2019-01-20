def sort_k(arr, k):
    arr = sorted(arr[:k]) + arr[k:]
    for i in range(k, len(arr)):
        start, end = i-k+1, i+1
        p, n = arr[:start], arr[end:]
        sub = sorted(arr[start:end])
        arr = p + sub + n
    return arr


# Test
assert sort_k([1, 0, 2, 4, 3], 2) == [0, 1, 2, 3, 4]
