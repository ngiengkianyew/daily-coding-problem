import sys


def get_pairwise_products(arr):
    pairwise_products = list()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                pairwise_products.append([set([i, j]), arr[i] * arr[j]])

    return pairwise_products


def get_largest_product(arr):
    pairwise_products = get_pairwise_products(arr)
    max_triple = -1 * sys.maxsize
    for i in range(len(arr)):
        for prev_indices, product in pairwise_products:
            if i not in prev_indices:
                triple_prod = arr[i] * product
                if triple_prod > max_triple:
                    max_triple = triple_prod

    return max_triple


assert get_largest_product([-10, -10, 5, 2]) == 500
assert get_largest_product([-10, 10, 5, 2]) == 100
