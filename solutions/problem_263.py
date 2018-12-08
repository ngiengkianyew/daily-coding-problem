SEPARATORS = {',', ';', ':'}
TERM_MARKS = {'.', '?', '!'}


def is_valid(context, char, next_chars):
    curr_valid = True

    if not context and not char.istitle():
        return False

    if len(context) == 1:
        if char == ' ' or not char.istitle():
            pass
        else:
            return False

    if char in TERM_MARKS:
        return context[-1] not in (SEPARATORS | TERM_MARKS)

    if not next_chars:
        return char in TERM_MARKS and curr_valid

    return is_valid(context + char, next_chars[0], next_chars[1:]) if curr_valid else False


def is_valid_sentence(sentence):
    return is_valid("", sentence[0], sentence[1:])


# Test
assert is_valid_sentence("Valid sentence.")
assert not is_valid_sentence("Invalid sentence")
assert not is_valid_sentence("INvalid sentence.")
assert is_valid_sentence("A valid sentence.")
