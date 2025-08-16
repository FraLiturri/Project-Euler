import numpy as np # Status: done ✅


def prime_checker(n):
    isPrime = True
    for i in range(2, int(np.sqrt(n) + 1)):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


def cycler_and_checker(n):
    isPrime = True
    n = str(n)
    if "2" in n or "5" in n or "0" in n or "4" in n or "8" in n or "6" in n:
        isPrime = False
    else:
        if prime_checker(int(n)):
            for i in range(1, len(n)):
                n = n[1:] + n[0]
                if not prime_checker(int(n)):
                    return False
                else:
                    isPrime = True
        else:
            isPrime = False
    return isPrime


counter = 0
for i in range(2, 10**6):
    if cycler_and_checker(i):
        counter += 1

print(counter + 2)
