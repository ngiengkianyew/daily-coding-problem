def get_sunset_bldgs(buildings):
    sbs = list()

    for height in buildings:
        if sbs and sbs[-1] < height:
            sbs.pop()
        sbs.append(height)

    return sbs


# Tests
assert get_sunset_bldgs([3, 7, 8, 3, 6, 1]) == [8, 6, 1]
