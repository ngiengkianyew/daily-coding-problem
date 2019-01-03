# Source: https://en.wikipedia.org/wiki/Nim#Mathematical_theory


def has_forced_win(heaps):
    x = heaps[0]
    for heap in heaps[1:]:
        x ^= heap

    for heap in heaps:
        xa = heap ^ x
        if xa < heap:
            return True

    return False


# Tests
assert has_forced_win((3, 4, 5))
