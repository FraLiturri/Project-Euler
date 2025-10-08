import numpy as np  # Status: work in progress
import math


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def is_square(n):
    root = math.sqrt(n)
    root = int(root)

    if root**2 == n:
        return True
    else:
        return False


primes = set(sieve(10**8))

ratio = 100
n = 3
counter = 1
numbers = [1, 3]
step = 3

while ratio >= 10:
    increser = n - 1
    step += increser

    numbers.append(step)

    if step in primes:
        counter += 1

    if is_square(step):
        ratio = counter / len(numbers) * 100
        print(n, counter, len(numbers), ratio)
        n += 2


print(n - 2)
