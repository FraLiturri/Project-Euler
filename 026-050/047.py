import numpy as np  # Status: done ✅


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


candidates = []
primes = sieve(10**3)


def factors_finder(input):
    factors = []
    global candidates
    n = input
    for prime in primes:
        counter = 1
        if n % prime == 0:
            n = n // prime
            while n % prime == 0:
                counter += 1
                n = n // prime
            factors.append(prime**counter)

        if prime > n:
            break
    return factors


for k in range(10**5, 10**6):  #adjusted manually;
    if (
        len(factors_finder(k))
        == len(factors_finder(k + 1))
        == len(factors_finder(k + 2))
        == len(factors_finder(k + 3))
        == 4
    ):
        if (
            list(set(factors_finder(k)) & set(factors_finder(k + 1))) == []
            and list(set(factors_finder(k + 1)) & set(factors_finder(k + 2))) == []
            and list(set(factors_finder(k + 2)) & set(factors_finder(k + 3))) == []
        ):
            print(k)
            break
