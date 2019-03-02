def lex_mod(string, k):
    if k > 1:
        return "".join(sorted(string))

    min_ch = min(string)
    joined = string + string
    for i, ch in enumerate(joined):
        if ch == min_ch:
            return joined[i:i + len(string)]


# Tests
assert lex_mod("daily", 2) == "adily"
assert lex_mod("daily", 1) == "ailyd"
