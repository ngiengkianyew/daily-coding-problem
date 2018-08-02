def get_min_coins(amount, denoms):
    if amount == 0:
        return 0

    denom_to_use, index_cutoff = None, None
    for i, denom in enumerate(denoms):
        if amount >= denom:
            denom_to_use = denom
            index_cutoff = i
            break

    coins_used = amount // denom_to_use

    return coins_used + get_min_coins(amount - (denom_to_use * coins_used),
                                      denoms[index_cutoff + 1:])


# Tests
denoms = [25, 10, 5, 1]
assert get_min_coins(16, denoms) == 3
assert get_min_coins(90, denoms) == 5
assert get_min_coins(100, denoms) == 4
