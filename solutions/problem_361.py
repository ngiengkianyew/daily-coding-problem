def does_code_match_guess(code, guess, matches):
    count = 0
    for c_char, g_char in zip(code, guess):
        if c_char == g_char:
            count += 1

    return count == matches


def is_valid_code(guess_scores):
    for i in range(1000000):
        code = str(i)
        code = ("0" * (6 - len(code))) + code

        success = True
        for guess, matches in guess_scores.items():
            success = success & does_code_match_guess(
                code, str(guess), matches)

        if success:
            return True

    return False


# Tests
assert is_valid_code({175286: 2, 293416: 3, 654321: 0})
assert not is_valid_code({123456: 4, 345678: 4, 567890: 4})
