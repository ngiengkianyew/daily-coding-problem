BOAT_LIMIT = 200


def get_min_boats_helper(people, boats_used):
    if len(people) < 2:
        return boats_used + len(people)

    first = people[0]
    remaining = people[1:]
    if first == BOAT_LIMIT:
        return get_min_boats_helper(remaining, boats_used + 1)

    allowed = BOAT_LIMIT - first
    second_index = len(remaining) - 1
    while allowed >= people[second_index]:
        second_index -= 1

    if second_index == len(remaining):
        return get_min_boats_helper(remaining, boats_used + 1)

    return get_min_boats_helper(remaining[:second_index] + remaining[second_index + 1:], boats_used + 1)


def get_min_boats(people):
    return get_min_boats_helper(sorted(people, reverse=True), 0)


# Tests
assert get_min_boats([100, 200, 150, 80]) == 3
