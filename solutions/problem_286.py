import sys


def get_max_width(buildings):
    leftmost, rightmost = sys.maxsize, -sys.maxsize
    for start, end, _ in buildings:
        if start < leftmost:
            leftmost = start
        if end > rightmost:
            rightmost = end

    return rightmost - leftmost + 1


def get_skyline(buildings):
    skyline_width = get_max_width(buildings)
    fill_arr = [0 for _ in range(skyline_width)]

    for start, end, height in buildings:
        for col in range(start, end):
            fill_arr[col] = max(fill_arr[col], height)

    skyline = list()
    prev_height = None
    for col, col_height in enumerate(fill_arr):
        if not skyline or prev_height != col_height:
            skyline.append((col, col_height))
        prev_height = col_height

    return skyline


# Tests
assert get_skyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)]) == \
    [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]
