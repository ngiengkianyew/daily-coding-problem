# pixel is a tuple of (x, y) co-ordinates in the matrix


def get_adj_pixels(pixel, matrix, rows, cols):
    adj_pixels = list()

    # add row above if it exists
    if pixel[0] > 0:
        adj_pixels.append((pixel[0]-1, pixel[1]))
        if pixel[1] > 0:
            adj_pixels.append((pixel[0]-1, pixel[1]-1))
        if pixel[1] < cols - 1:
            adj_pixels.append((pixel[0]-1, pixel[1]+1))

    # add row below if it exists
    if pixel[0] < rows - 1:
        adj_pixels.append((pixel[0]+1, pixel[1]))
        if pixel[1] > 0:
            adj_pixels.append((pixel[0]+1, pixel[1]-1))
        if pixel[1] < cols - 1:
            adj_pixels.append((pixel[0]+1, pixel[1]+1))

    # add left cell if it exists
    if pixel[1] > 0:
        adj_pixels.append((pixel[0], pixel[1]-1))

    # add right cell if it exists
    if pixel[1] < cols - 1:
        adj_pixels.append((pixel[0], pixel[1]+1))

    return adj_pixels


def change_color(pixel, matrix, new_color):
    if not matrix:
        return matrix

    # switch to 0-indexed co-ordinates
    x, y = pixel[0] - 1, pixel[1] - 1

    rows = len(matrix)
    cols = len(matrix[0])
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return matrix

    c = matrix[x][y]
    adj_pixels = get_adj_pixels((x, y), matrix, rows, cols)

    for ap in adj_pixels:
        if matrix[ap[0]][ap[1]] == c:
            matrix[ap[0]][ap[1]] = new_color
    matrix[x][y] = new_color

    return matrix


# Tests
matrix = [['B', 'B', 'W'],
          ['W', 'W', 'W'],
          ['W', 'W', 'W'],
          ['B', 'B', 'B']]
assert change_color((2, 2), matrix, 'G') == \
    [['B', 'B', 'G'],
     ['G', 'G', 'G'],
     ['G', 'G', 'G'],
     ['B', 'B', 'B']]
