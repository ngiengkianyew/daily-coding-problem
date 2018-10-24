def get_max_possible(coins, amount=0, turn=True):
    if not coins:
        return amount

    if turn:
        alt_1 = get_max_possible(coins[1:], amount + coins[0], False)
        alt_2 = get_max_possible(coins[:-1], amount + coins[-1], False)
        return max(alt_1, alt_2)

    first, last = coins[0], coins[-1]
    if first > last:
        coins = coins[1:]
    else:
        coins = coins[:-1]

    return get_max_possible(coins, amount, True)


# Test
assert get_max_possible([1, 2, 3, 4, 5]) == 9
