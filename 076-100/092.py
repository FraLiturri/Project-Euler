import numpy as np # Status: done ✅

counter = 0
limit = 10**7
flag = [0] * limit
flag_89 = [0] * limit


def function(n):
    sum = 0
    for digit in str(n):
        sum += int(digit) ** 2

    return sum


def reducer(n):
    seen_num = []
    while True:
        n = function(n)
        seen_num.append(n)
        if n == 1 or n == 89:
            break

    for num in seen_num:
        flag[num] = 1
        if n == 89:
            flag_89[num] = 1


for k in reversed(range(1, limit)):
    if flag[k] == 0:
        reducer(k)

print(np.sum(flag_89))
