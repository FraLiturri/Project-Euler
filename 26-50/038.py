import numpy as np # Status: done ✅
import itertools

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
comb = list(itertools.permutations(digits, 9))

limit = len(comb)

for i in range(0, limit):
    current = comb[len(comb) - i - 1]  # (9,8,7,6,5,4,3,2,1)

    second = (
        current[4] * 10**4
        + current[5] * 10**3
        + current[6] * 10**2
        + current[7] * 10
        + current[8]
    )
    first = current[0] * 1000 + current[1] * 100 + current[2] * 10 + current[3]

    q1, r1 = divmod(second, first)

    if r1 == 0:
        if q1 == 2:
            print("The greatest pandigital with this property is:", current)
            break
