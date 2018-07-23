def calculate_trapped_water(walls):
    if len(walls) < 3:
        return 0

    total_water_volume = 0

    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0

    while left <= right:
        if walls[left] < walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water_volume += left_max - walls[left]
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water_volume += right_max - walls[right]
            right -= 1

    return total_water_volume


assert calculate_trapped_water([1]) == 0
assert calculate_trapped_water([2, 1]) == 0
assert calculate_trapped_water([2, 1, 2]) == 1
assert calculate_trapped_water([4, 1, 2]) == 1
assert calculate_trapped_water([4, 1, 2, 3]) == 3
assert calculate_trapped_water([3, 0, 1, 3, 0, 5]) == 8
assert calculate_trapped_water([10, 9, 1, 1, 6]) == 10
