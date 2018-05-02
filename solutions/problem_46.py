def is_palindrome(s1):
    return s1 == s1[::-1]


def get_longest_palindrome_substring(s):
    if not s or is_palindrome(s):
        return s

    s1 = get_longest_palindrome_substring(s[1:])
    s2 = get_longest_palindrome_substring(s[:-1])

    return s1 if len(s1) >= len(s2) else s2


assert get_longest_palindrome_substring("aabcdcb") == "bcdcb"
assert get_longest_palindrome_substring("bananas") == "anana"
