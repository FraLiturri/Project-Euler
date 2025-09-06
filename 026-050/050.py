import numpy as np  # Status: work in progress


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def prime_checker(n):
    isPrime = True
    if n < 0:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


primes = sieve(10**2)
prime_sum = np.sum(primes)



print(max)
