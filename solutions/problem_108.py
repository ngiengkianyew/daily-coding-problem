def can_shift(target, string):
    return len(target) == len(string) and string in target * 2


assert can_shift("abcde", "cdeab")
assert not can_shift("abc", "acb")
