import numpy as np  # Status: done ✅

limit = 10**6
naturals = []
max = 0
searched_n = 1


def Collatz_employer(n):
    counter = 0
    while n > 1:
        n = int(n / 2) if n % 2 == 0 else 3 * n + 1
        counter += 1
    return counter


for i in range(1, limit):
    naturals.append(limit - i)

for n in naturals:
    current = Collatz_employer(n)
    if current > max: 
        max = current
        searched_n = n

print(searched_n)
