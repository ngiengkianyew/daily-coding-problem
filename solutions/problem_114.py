def reverse_words(string, delimiters):
    words = list()
    delims = list()
    delim_positions = list()  # stores positions of the delimiters seen

    start = 0
    i = 0
    while i < len(string):
        char = string[i]

        if char in delimiters:
            word = string[start:i]
            if i - start > 1:
                words.append(word)
            delims.append(char)
            delim_positions.append(len(words) + len(delims) - 1)
            start = i + 1

        i += 1

    # get last word if present
    if i - start > 1:
        words.append(string[start:i])

    words.reverse()  # reverse just the words

    reversed_order = list()
    word_index = 0
    delim_index = 0

    # merging the reversed words and the delimiters
    for i in range(len(words) + len(delims)):
        if delim_index < len(delim_positions) and delim_positions[delim_index] == i:
            # insert next delimiter if the position is saved for a delimiter
            reversed_order.append(delims[delim_index])
            delim_index += 1
        else:
            reversed_order.append(words[word_index])
            word_index += 1

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
