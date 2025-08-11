import numpy as np  # pyright: ignore

limit = 10**4
isPrime = True
primes = [2, 3]  # we know 2,3 are prime

for i in range(4, limit):
    isPrime = True
    for prime in primes:
        if i % prime == 0:
            isPrime = False
    if isPrime:
        primes.append(i)
        
print(primes)
