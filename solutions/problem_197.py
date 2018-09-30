def rotate_index(arr, k, src_ind, src_num, count=0):
    if count == len(arr):
        return

    des_ind = (src_ind + k) % len(arr)
    des_num = arr[des_ind]

    arr[des_ind] = src_num

    rotate_index(arr, k, des_ind, des_num, count + 1)


def rotate_k(arr, k):
    if k < 1:
        return arr

    start = 0
    rotate_index(arr, k, start, arr[start])


# Tests
arr = [1, 2, 3, 4, 5]
rotate_k(arr, 2)
assert arr == [4, 5, 1, 2, 3]
rotate_k(arr, 2)
assert arr == [2, 3, 4, 5, 1]
rotate_k(arr, 4)
assert arr == [3, 4, 5, 1, 2]
