def look_and_say(seq_count, num_str="1"):
    if seq_count == 1:
        return num_str

    tuples = [(0, num_str[0])]
    for char in num_str:
        prev_count, prev_char = tuples.pop()
        if char == prev_char:
            tuples.append((prev_count + 1, char))
        else:
            tuples.append((prev_count, prev_char))
            tuples.append((1, char))

    flat_list = [str(x) for tup in tuples for x in tup]
    new_num_str = "".join(flat_list)

    return look_and_say(seq_count - 1, new_num_str)


# Test
assert look_and_say(1) == "1"
assert look_and_say(5) == "111221"
assert look_and_say(6) == "312211"
