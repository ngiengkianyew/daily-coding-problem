def print_zigzag(string, k):

    string_dict = dict()
    for row in range(k):
        string_dict[row] = ""

    crow = 0
    direction = -1
    for i in range(len(string)):
        for row in range(k):
            if row == crow:
                string_dict[row] += string[i]
            else:
                string_dict[row] += " "

        if crow == k-1 or crow == 0:
            direction *= -1

        crow += direction

    final_string = "\n".join([x for x in string_dict.values()])

    print(final_string)


# Tests
print_zigzag("thisisazigzag", 4)
print_zigzag("thisisazigzag", 5)
