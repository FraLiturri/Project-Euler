import numpy as np # Status: done ✅
from math import factorial

n = 13
fact = factorial(n)

sum = 0
for i in range(0, len(str(fact))): 
    sum += int(str(fact)[i])

print(sum)