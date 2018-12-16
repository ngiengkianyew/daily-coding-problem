def perm_counter(num_dice, face_range, total):
    if num_dice < 1 or total < 1:
        return 0
    elif num_dice == 1 and total in face_range:
        return 1

    return sum([perm_counter(num_dice - 1, face_range, total - x) for x in face_range])


def throw_dice(num_dice, faces, total):
    return perm_counter(num_dice, range(1, faces + 1), total)


# Tests
assert throw_dice(3, 6, 7) == 15
