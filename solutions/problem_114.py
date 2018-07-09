def reverse_words(string, delimiters):
    words = list()
    delims = list()
    delim_indices = list()

    start = 0
    i = 0
    while i < len(string):
        char = string[i]

        if char in delimiters:
            word = string[start:i]
            if i - start > 1:
                words.append(word)
            delims.append(char)
            delim_indices.append(len(words) + len(delims) - 1)
            start = i + 1

        i += 1

    if i - start > 1:
        words.append(string[start:i])

    words.reverse()

    reversed_order = list()
    wi = 0
    di = 0
    for i in range(len(words) + len(delims)):
        if di < len(delim_indices) and delim_indices[di] == i:
            reversed_order.append(delims[di])
            di += 1
        else:
            reversed_order.append(words[wi])
            wi += 1

    reversed_string = "".join(reversed_order)

    return reversed_string


assert reverse_words("hello/world:here/",
                     set([':', '/'])) == "here/world:hello/"
assert reverse_words(":hello//world:here/",
                     set([':', '/'])) == ":here//world:hello/"
assert reverse_words("hello//world:here",
                     set([':', '/'])) == "here//world:hello"
assert reverse_words("hello/world:here",
                     set([':', '/'])) == "here/world:hello"
