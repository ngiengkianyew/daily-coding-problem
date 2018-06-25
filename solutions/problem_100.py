def get_distance(current_point, next_point, accumulated_distance):
    x_diff = next_point[0] - current_point[0]
    y_diff = next_point[1] - current_point[1]

    if not x_diff:
        return abs(y_diff) + accumulated_distance
    if not y_diff:
        return abs(x_diff) + accumulated_distance

    updated_current = (current_point[0] + int(x_diff/abs(x_diff)),
                       current_point[1] + int(y_diff/abs(y_diff)))

    return get_distance(updated_current, next_point, accumulated_distance + 1)


def get_min_steps_helper(current_point, remaining_points, steps):
    if not remaining_points:
        return steps

    next_point = remaining_points[0]
    min_distance = get_distance(current_point, next_point, 0)

    return get_min_steps_helper(next_point, remaining_points[1:], steps + min_distance)


def get_min_steps(points):
    if not points:
        return 0

    return get_min_steps_helper(points[0], points[1:], 0)


assert get_min_steps([]) == 0
assert get_min_steps([(0, 0)]) == 0
assert get_min_steps([(0, 0), (1, 1), (1, 2)]) == 2
assert get_min_steps([(0, 0), (1, 1), (1, 2), (3, 4)]) == 4
assert get_min_steps([(0, 0), (1, 1), (1, 2), (3, 6)]) == 6
