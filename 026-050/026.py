import numpy as np # Status: work in progress
from decimal import Decimal, getcontext

getcontext().prec = 300


def period_counter(den):
    if den < 10:
        factor = 10
    if den >= 10 and den < 100:
        factor = 100
    if den >= 100:
        factor = 1000

    num = factor
    numerators = [num]

    while True:
        r = num % den
        num = r * factor if num < 100 else r * factor / 10

        if num in numerators:
            break
        else:
            numerators.append(num)

    return len(numerators)


den = 101
print(Decimal(1) / Decimal(den), period_counter(den))

max = 0
d = 0
for n in range(2, 1000):
    if max < period_counter(n):
        d = n
        max = period_counter(n)

print(max, d)
