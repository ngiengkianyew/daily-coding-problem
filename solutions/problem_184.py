SMALLEST_PRIME = 2


def is_prime(cand, primes):
    for prime in primes:
        res = cand / prime
        if not res % 1:
            return False

    return True


def get_possible_primes(num):
    primes = [SMALLEST_PRIME]

    for cand in range(SMALLEST_PRIME + 1, num//2 + 1):
        if is_prime(cand, primes):
            primes.append(cand)

    return primes


def get_factors(num, primes):
    factors = dict()

    pi = 0
    while num > 1:
        if pi >= len(primes):
            break
        if not num % primes[pi]:
            if primes[pi] not in factors:
                factors[primes[pi]] = 0
            factors[primes[pi]] += 1
            num /= primes[pi]
        else:
            pi += 1
    return factors


def get_gcd(nums):
    min_num = min(nums)
    primes = get_possible_primes(min_num)
    base_factors = get_factors(min_num, primes)

    factorized_nums = dict()
    for num in nums:
        factorized_nums[num] = get_factors(num, primes)

    common_factors = dict()
    for base_factor in base_factors:
        common_factors[base_factor] = 0
        num_factors = list()
        for num in nums:
            factors = factorized_nums[num]
            num_factors.append(factors[base_factor])
        common_factors[base_factor] = min(num_factors)

    gcd = 1
    for factor in common_factors:
        gcd *= factor ** common_factors[factor]

    return gcd


# Tests
assert get_gcd([42, 56, 14]) == 14
assert get_gcd([3, 5]) == 1
assert get_gcd([9, 15]) == 3
