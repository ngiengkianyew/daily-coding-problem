import sys

def get_largest_non_adj_sum(array):
    previous, largest = 0, 0
    for amount in array:
        print("amount: {}; previous: {}; largest: {}".format(amount, previous, largest))
        previous, largest = largest, max(largest, previous + amount)
        print("new_previous: {}; new_largest: {}".format(previous, largest))
    return largest

print(get_largest_non_adj_sum([2, 4, 6, 8]))
print(get_largest_non_adj_sum([5, 1, 1, 5]))
