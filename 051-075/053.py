import numpy as np # Status: done ✅
from math import comb

counter = 0
n_max = 100

for n in range(1, n_max + 1):
    r = 0
    while r <= n:
        bin = comb(n, r)

        if bin > 10**6:
            counter += 1
        r += 1

print("The result is:", counter)
