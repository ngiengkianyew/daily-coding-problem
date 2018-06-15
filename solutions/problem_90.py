from random import randint


def generate_random_num(n, excluded_nums):
    rand = randint(0, n-1)
    if rand in excluded_nums:
        return generate_random_num(n, excluded_nums)

    return rand


def run_experiment(num_samples, n, l):
    error_tolerance = 0.01
    results = dict()
    excluded_nums = set(l)

    for num in range(n):
        results[num] = 0

    for _ in range(num_samples):
        rand = generate_random_num(n, excluded_nums)
        results[rand] += 1
    expected_prob = 1/(n - len(excluded_nums))

    for num in results:
        results[num] /= num_samples
        if num in excluded_nums:
            assert not results[num]
        else:
            assert results[num] > expected_prob - error_tolerance or \
                results[num] < expected_prob + error_tolerance


run_experiment(100000, 6, [])
run_experiment(100000, 6, [1, 5])
run_experiment(100000, 6, [1, 3, 5])
