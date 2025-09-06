import numpy as np  # Status: done ✅

amicable_sum = 0
limit = 10**4
d2 = 0


def prop_div_finder(n):
    d = 0
    for i in range(1, n):
        if n % i == 0:
            d += i
    return d


def amicable_checker(n):
    areAmicable = False
    global amicable_sum
    global d2
    d1 = prop_div_finder(n)
    d2 = prop_div_finder(d1)
    if d2 == n and d1 != n:
        amicable_sum += n
        areAmicable = True
    return areAmicable


flag = [1] * limit
flag[0] = 0

for i in range(1, limit):
    if flag[i] == 1: 
        if amicable_checker(i):
            flag[d2] = 0


print("The sum of all the amicable is:", amicable_sum)
