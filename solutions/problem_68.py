def add_new_bishop(location, attack_positions, board_size):
    # count how many times existing bishops can attack
    count = 0
    if location in attack_positions:
        count += 1

    # add new attack positions for future bishops
    new_attack_positions = list()

    i, j = location
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        new_attack_positions.append((i, j))
    i, j = location
    while i > 0 and j < board_size - 1:
        i -= 1
        j += 1
        new_attack_positions.append((i, j))
    i, j = location
    while i < board_size - 1 and j > 0:
        i += 1
        j -= 1
        new_attack_positions.append((i, j))
    i, j = location
    while i < board_size - 1 and j < board_size - 1:
        i += 1
        j += 1
        new_attack_positions.append((i, j))

    attack_positions.extend(new_attack_positions)

    return count, attack_positions


def get_attack_vectors(bishop_locations, board_size):
    attack_positions = list()
    total_count = 0
    for location in bishop_locations:
        count, attack_positions = add_new_bishop(
            location, attack_positions, board_size)
        total_count += count

    return total_count


assert get_attack_vectors([(0, 0), (1, 2), (2, 2), (4, 0)], 5) == 2
assert get_attack_vectors([(0, 0), (1, 2), (2, 2)], 5) == 1
