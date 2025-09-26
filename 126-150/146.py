import numpy as np

limit = 10**6
sum = 0

def prime_checker(n):
    isPrime = True
    for i in range(2, int(np.sqrt(n)) + 1):
        r = n % i
        if r == 0:
            isPrime = False
    return isPrime


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


primes = sieve(limit) 

for n in range(2, 10**3):
    if prime_checker(n**2 + 1):
        index = primes.index(n**2 + 1)
        if (
            primes[index + 1] == n**2 + 3
            and primes[index + 3] == n**2 + 7
            and primes[index + 4] == n**2 + 9
            and primes[index + 5] == n**2 + 13
            and primes[index + 6] == n**2 + 27
        ):
            sum += n

print(sum)