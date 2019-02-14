def get_flip_count(string):
    strlen = len(string)

    last_x_pos, first_y_pos = strlen, -1
    for i in range(strlen):
        if string[i] == 'y':
            first_y_pos = i
            break
    for i in range(strlen):
        index = strlen - i - 1
        if string[index] == 'x':
            last_x_pos = index
            break

    x_count, y_count = 0, 0
    for i in range(last_x_pos):
        if string[i] == 'y':
            y_count += 1
    for i in range(first_y_pos + 1, strlen):
        if string[i] == 'x':
            x_count += 1

    return min(x_count, y_count)


# Tests
assert get_flip_count("xyxxxyxyy") == 2
