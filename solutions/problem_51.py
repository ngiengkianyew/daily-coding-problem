# This problem was asked by Facebook.
# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
# It should run in O(N) time.
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

from random import randint

NUM_CARDS = 52


def get_random_number(k):
    return randint(0, k)


def shuffle_card_deck():
    cards = [x for x in range(NUM_CARDS)]

    for old_pos in cards:
        new_pos = old_pos + get_random_number(NUM_CARDS - old_pos - 1)
        temp = cards[new_pos]
        cards[new_pos] = cards[old_pos]
        cards[old_pos] = temp

    return cards


for _ in range(10):
    assert all(x in shuffle_card_deck() for x in range(NUM_CARDS))
