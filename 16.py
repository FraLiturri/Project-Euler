import numpy as np #pyright: ignore
from decimal import Decimal, getcontext

getcontext().prec = 302

n = 2**1000
sum = 0
for i in range(0, len(str(n))): 

    digit = Decimal(n)/ Decimal(10**i) %10
    digit = int(digit)
    sum += digit

print(sum)