def get_max_path(triangle, index, level, path, path_val):
    if level == len(triangle):
        return path, path_val

    ind_a, ind_b = index, index + 1
    val_a, val_b = triangle[level][ind_a], triangle[level][ind_b]

    path_a, path_val_a = \
        get_max_path(triangle, ind_a, level + 1,
                     path + [val_a], path_val + val_a)
    path_b, path_val_b = \
        get_max_path(triangle, ind_b, level + 1,
                     path + [val_b], path_val + val_b)

    return (path_a, path_val_a) if path_val_a > path_val_b else (path_b, path_val_b)


def get_max_path_helper(triangle):
    return get_max_path(triangle, index=0, level=1,
                        path=[triangle[0][0]], path_val=triangle[0][0])[0]


# Tests
assert get_max_path_helper([[1], [2, 3], [1, 5, 1]]) == [1, 3, 5]
assert get_max_path_helper([[1], [2, 3], [7, 5, 1]]) == [1, 2, 7]
