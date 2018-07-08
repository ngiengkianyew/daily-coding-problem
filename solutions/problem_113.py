def reverse_words(string):
    return " ".join(reversed(string.split()))


assert reverse_words("hello world here") == "here world hello"
