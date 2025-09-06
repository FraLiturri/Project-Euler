import numpy as np  # Status: done ✅

primes = []  # here are collected with sign: if p is prime, -p is prime too;


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


def prime_gen(n):
    for i in range(2, n + 1):
        if prime_checker(i):
            primes.append(i)
            primes.append(-i)


def quadratic(n, a, b):
    res = int(n**2 + a * n + b)
    return res


prime_gen(1000)

current_max = 0
a = -999
good_a = 1
good_b = 1

while a < 1000:
    for prime in primes:
        counter = 0
        n = 0
        while True:
            if prime_checker(quadratic(n, a, prime)):
                counter += 1
                n += 1
            else:
                break
        if current_max < counter:
            current_max = counter
            good_a = a
            good_b = prime

    a += 1


print(current_max)
print(good_a, good_b, good_b * good_a)
