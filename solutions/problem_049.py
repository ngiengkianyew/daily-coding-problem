def get_max_subarray(arr):
    if not arr or max(arr) < 0:
        return 0

    current_max_sum = arr[0]
    overall_max_sum = arr[0]

    for num in arr[1:]:
        current_max_sum = max(num, current_max_sum + num)
        overall_max_sum = max(overall_max_sum, current_max_sum)

    return overall_max_sum


assert get_max_subarray([34, -50, 42, 14, -5, 86]) == 137
assert get_max_subarray([-5, -1, -8, -9]) == 0
assert get_max_subarray([44, -5, 42, 14, -150, 86]) == 95
