import numpy as np # Status: done ✅
from decimal import Decimal, getcontext

getcontext().prec = 150

def decimal_counter(n):
    n = str(n)

    sum = int(n[0])
    for k in range(2, 101):
        sum += int(n[k])

    return sum


def is_perf_square(n):
    root = np.sqrt(n)
    root = np.floor(root)

    if root**2 == n:
        return True
    else:
        return False


n = 1
sum = 0

while n < 100:
    if not is_perf_square(n):
        root = Decimal(n).sqrt()
        sum += decimal_counter(root)
    n += 1

print("The result is:", sum)
