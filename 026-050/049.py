import numpy as np
import itertools


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def digits_summer(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


def list_to_num(list):
    number = ""
    for element in list:
        number += element
    return int(number)


primes = sieve(10**4)
primes_archive = set(sieve(10**4))
candidates = []

for k in range(0, len(primes)):
    if primes[k] > 10**3:
        i = k + 1
        digits = ()
        while i < len(primes):
            next = primes[i] + primes[i] - primes[k]
            if next in primes_archive and digits_summer(primes[k]) == digits_summer(
                primes[i]
            ) == digits_summer(next):
                candidates.append([primes[k], primes[i], next])
            i += 1

for candidate in candidates:
    cand = sorted(str(candidate[0]))
    cand = list_to_num(cand)
    if (
        cand - list_to_num(sorted(str(candidate[1])))
        == cand - list_to_num(sorted(str(candidate[2])))
        == 0
    ):
        print(candidate)
