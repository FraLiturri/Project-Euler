import numpy as np # Status: done ✅
from math import factorial

#List of factorial from 0 to 9: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def checker(n):
    sum = 0
    isSpecial = False
    for i in range(0, len(str(n))):
        sum += factorial(int(n / 10**i % 10))

    if sum == n:
        isSpecial = True
    return isSpecial

sum = 0
limit = 10**5 #upper limit; 
for i in range(3, limit): 
    if checker(i):
        #print(i)
        sum += i

print("The sum is:", sum)