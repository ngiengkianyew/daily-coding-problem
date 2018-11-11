from random import random

card_distribution = dict()


def generate_card_distribution():
    for i in range(1, 11):
        if i not in card_distribution:
            card_distribution[i] = 0

        if i == 10:
            card_distribution[i] += 4
        else:
            card_distribution[i] += 1
    summed = sum(card_distribution.values())

    prev = 0
    for key in card_distribution:
        card_distribution[key] = prev + (card_distribution[key]/summed)
        prev = card_distribution[key]


def get_next_card_value():
    rand = random()
    lower, upper = 0, None
    for key, value in card_distribution.items():
        upper = value
        if rand >= lower and rand <= upper:
            return key
        lower = upper


def play_turn(scores, dealer):
    if dealer and scores[1] < 16:
        next_card = get_next_card_value()
        scores[1] += next_card
        return True if scores[1] > 21 else False

    if scores[0] < 21:
        next_card = get_next_card_value()
        if scores[0] + next_card < 22:
            scores[0] += next_card

    return False


def play_game():
    scores = [0, 0]
    won = False
    dealer = False

    while not won:
        won = play_turn(scores, dealer)
        dealer = not dealer
        if scores[1] < scores[0]:
            print("Player wins")
            break


# Tests
generate_card_distribution()
play_game()
