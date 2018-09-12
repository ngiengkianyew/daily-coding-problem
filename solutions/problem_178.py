# I would think that there is no difference between either game
# because the `nth` and the `(n-1)th` dice rolls should be
# independent events

from random import randint


def roll_dice(sought_values, index, prev_tosses):
    rand = randint(1, 6)

    if sought_values[index] == rand:
        index += 1

        if index == len(sought_values):
            return prev_tosses + 1

    return roll_dice(sought_values, index, prev_tosses + 1)


def simulate_game(sought_values):
    penalty = roll_dice(sought_values, 0, 0)
    return penalty


# Tests

num_exp = 100000
sought_value_pairs = [[5, 6], [5, 5]]

for sought_values in sought_value_pairs:
    total_penalty = 0
    for _ in range(num_exp):
        total_penalty += simulate_game(sought_values)
    avg_penalty = total_penalty / num_exp

    #  the expected value is approx. 12 on average for a single game
    assert round(avg_penalty) == 12
