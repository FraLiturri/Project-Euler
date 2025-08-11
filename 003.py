import numpy as np  # pyright: ignore ✅

n = 600851475143
root = int(np.sqrt(n))
current_max = 1


def prime_checker(n):
    isPrime = True
    for i in range(2, n + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


for k in range(1, root):
    r = n % k
    if r == 0:
        if prime_checker(k):
            current_max = k if k > current_max else 0

print(current_max)

