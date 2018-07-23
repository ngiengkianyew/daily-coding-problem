def is_match(regex, string):

    # if no pattern and no text, return True
    if not regex:
        return not string

    # first character will not be a Kleene star
    first_match = bool(string) and regex[0] in {string[0], '.'}

    if len(regex) >= 2 and regex[1] == '*':
        # regex[0] consumes no characters or
        # regex[0] consumes one character
        return is_match(regex[2:], string) or \
            (first_match and is_match(regex, string[1:]))
    else:
        # regex[0] consumes one character
        return first_match and is_match(regex[1:], string[1:])


assert is_match("ra.", "ray")
assert not is_match("ra.", "raymond")
assert is_match(".*at", "chat")
assert not is_match(".*at", "chats")
