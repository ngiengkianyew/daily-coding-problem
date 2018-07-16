def is_palindrome(string):
    return bool(string) and string == string[::-1]


def make_palindrome(string, num_delete):
    if is_palindrome(string):
        return True
    if not num_delete:
        return False

    for i, _ in enumerate(string):
        new_string = string[:i] + string[i+1:]
        if make_palindrome(new_string, num_delete - 1):
            return True

    return False


# Tests
assert make_palindrome("a", 0)
assert make_palindrome("aaa", 2)
assert not make_palindrome("add", 0)
assert make_palindrome("waterrfetawx", 2)
assert not make_palindrome("waterrfetawx", 1)
assert make_palindrome("waterrfetawx", 3)
assert make_palindrome("malayalam", 0)
assert make_palindrome("malayalam", 1)
assert make_palindrome("asdf", 5)
assert not make_palindrome("asdf", 2)
