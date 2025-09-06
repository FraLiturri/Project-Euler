import numpy as np  # Status: done ✅


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


primes = sieve(5*10**3)
prime_search = set(sieve(10**6)) #worshipping set; 
prime_sum = np.sum(primes)

inf_s = prime_sum
max_count = 0
number = 0

for i in range(-1, len(primes)):
    prev_s = 0
    k = len(primes) - 1
    if i >= 0:
        inf_s = inf_s - primes[i]
    sup_s = inf_s

    while sup_s > 0:
        if sup_s in prime_search and sup_s < 10**6:
            number = sup_s if max_count < k - i else number
            max_count = k - i if max_count < k - i else max_count

        sup_s = sup_s - primes[k]
        k = k - 1

print("The searched number is:", number)
