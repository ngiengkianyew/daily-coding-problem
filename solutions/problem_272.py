def throw_dice(num_dice, faces, total):
    if num_dice == 0 or total < 1:
        return 0

    face_range = range(1, faces + 1)
    if num_dice == 1 and total in face_range:
        return 1

    num_perms = 0
    for i in face_range:
        num_perms += throw_dice(num_dice - 1, faces, total - i)

    return num_perms


# Tests
assert throw_dice(3, 6, 7) == 15
