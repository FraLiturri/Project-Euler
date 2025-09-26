import numpy as np # Status: done ✅

def digit_counter(n):
    n = str(n)
    sum = 0
    for digit in n: 
        sum += int(digit)
    return sum

max = 0
for a in range(1, 100):
    for b in range(1,100):
        res = digit_counter(a**b)
        if max < res:
            max = res

print("The max value of sum is:", max)
