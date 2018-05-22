# assume HEADS = 1 and TAILS = 0 or vice-versa

from random import random


def get_biased_flip():
    rand = random()
    return 0 if rand < 0.7 else 1


num_experiments = 1000000
results_biased = {1: 0, 0: 0}
results_unbiased = {1: 0, 0: 0}
for i in range(num_experiments):
    flip = get_biased_flip()
    results_biased[flip] += 1
    flip = not flip if i % 2 == 0 else flip
    results_unbiased[flip] += 1

for key in results_biased:
    results_biased[key] /= num_experiments
    results_biased[key] = round(results_biased[key], 2)
for key in results_unbiased:
    results_unbiased[key] /= num_experiments
    results_unbiased[key] = round(results_unbiased[key], 2)

assert results_biased[0] == 0.7
assert results_biased[1] == 0.3
assert results_unbiased[0] == 0.5
assert results_unbiased[1] == 0.5
