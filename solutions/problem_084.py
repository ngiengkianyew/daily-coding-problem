def add_island(x, y, world_map, visited):
    coord = "{}-{}".format(x, y)

    if coord in visited:
        return 0

    visited.add(coord)

    if x > 0 and world_map[x-1][y]:
        add_island(x-1, y, world_map, visited)
    if x < len(world_map) - 1 and world_map[x+1][y]:
        add_island(x+1, y, world_map, visited)
    if y > 0 and world_map[x][y-1]:
        add_island(x, y-1, world_map, visited)
    if y < len(world_map[0]) - 1 and world_map[x][y+1]:
        add_island(x, y+1, world_map, visited)

    return 1


def count_islands(world_map):
    count = 0
    visited = set()
    for i in range(len(world_map)):
        for k in range(len(world_map[0])):
            if world_map[i][k]:
                count += add_island(i, k, world_map, visited)

    return count


world_map = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
]
assert count_islands(world_map) == 4
