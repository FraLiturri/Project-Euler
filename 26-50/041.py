import numpy as np  # Status: done ✅
import itertools

digits = [1, 2, 3, 4, 5, 6, 7]  # the number can be only 7-digital (except 4-digital);
comb = list(itertools.permutations(digits, 7))
max_prime = 1


def prime_checker(n):
    isPrime = True
    for i in range(2, n + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


for k in range(0, len(comb)):
    combination = comb[len(comb) - k - 1]
    if combination[6] % 2 != 0 and combination[6] % 5 != 0:
        number = (
            str(combination[0])
            + str(combination[1])
            + str(combination[2])
            + str(combination[3])
            + str(combination[4])
            + str(combination[5])
            + str(combination[6])
        )
        number = int(number)
    if prime_checker(number):
        print("The biggest number is:", number)
        found = True
        break
