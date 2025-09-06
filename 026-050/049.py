import numpy as np
import itertools

primes = []  # primes between 10**3 and 10**4;


def prime_gen(n):
    for j in range(2, n + 1):
        isPrime = True
        for i in range(2, int(np.sqrt(j)) + 1):
            r = j % i
            if r == 0:
                isPrime = False
        if isPrime and j > 10**3:
            primes.append(j)
    return isPrime


def prime_checker(n):
    isPrime = True
    for i in range(2, int(np.sqrt(n)) + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


def permutator(n):
    n = str(n)
    digits = []
    for digit in n:
        digits.append(digit)
    comb = list(itertools.permutations(digits, 4))
    return comb


def converter(n):

    m = str(n[0]) + str(n[1]) + str(n[2]) + str(n[3])
    m = int(m)
    return m


prime_gen(10**4)


found = False
for i in range(10**3, 10**4):
    candidates = []
    differences = []
    permutations = permutator(i)
    permutations = list(dict.fromkeys(permutations))

    for j in range(0, len(permutations)):
        if prime_checker(converter(permutations[j])):
            candidates.append(converter(permutations[j]))

    if len(candidates) > 3:
        candidates.sort()
        for k in range(0, len(candidates) - 1):
            differences.append(candidates[k + 1] - candidates[k])
        print(candidates, differences)