from random import random

count_so_far = 0
result = None


def pick_random_element(x):
    global count_so_far, result
    count_so_far += 1

    print(count_so_far)

    if count_so_far == 1:
        result = x
    else:
        random_value = int(count_so_far * random())
        if random_value == count_so_far - 1:
            result = x

    return result


sample_stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, element in enumerate(sample_stream):
    random_element = pick_random_element(element)
    print("Random element of the first {} is {}".format(index + 1, random_element))
