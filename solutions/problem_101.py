def is_prime(num, primes):
    for prime in primes:
        if prime == num:
            return True
        if not num % prime:
            return False
    return True


def get_primes(num):
    limit = (num // 2) + 1

    candidates = list()
    primes = list()
    for i in range(2, limit):
        if is_prime(i, primes):
            primes.append(i)
            candidates.append((i, num - i))

    new_candidates = list()
    for first, second in candidates[::-1]:
        if is_prime(second, primes):
            primes.append(second)
            new_candidates.append((first, second))

    return new_candidates[-1]


assert get_primes(4) == (2, 2)
assert get_primes(10) == (3, 7)
assert get_primes(100) == (3, 97)
