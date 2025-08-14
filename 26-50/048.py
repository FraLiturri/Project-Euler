import numpy as np  # Status: done ✅

max_n = 10
sum = 0


def head_cutter(n):
    stringed = str(n)
    aux = stringed[len(stringed) - max_n :]
    n = aux
    return n


for i in range(1, 1001):  # we know the sum of the first ten terms;
    res = 1
    for k in range(1, i + 1):
        res = res * i
        if len(str(res)) > 10:
            res = int(head_cutter(res))
    sum += res

sum = head_cutter(sum)  # cutting head for the last time
print(
    sum
)  # note: if the result has less than 10 digits, the missing ones (on the left) are all 0;
