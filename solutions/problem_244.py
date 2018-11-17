import time


def get_next_prime(primes_seen):
    num = primes_seen[-1] + 1
    while True:
        if all([num % x for x in primes_seen]):
            time.sleep(0.1)
            yield num
        num += 1


def print_primes():
    first_prime = 2
    primes_seen = [first_prime]
    print(first_prime)
    for next_prime in get_next_prime(primes_seen):
        primes_seen.append(next_prime)
        print(next_prime)


print_primes()
