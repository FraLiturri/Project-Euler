import numpy as np #pyright: ignore

def prime_checker(n):
    isPrime = True
    for i in range(2, n + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime

