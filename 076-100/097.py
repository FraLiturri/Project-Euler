import numpy as np  # Status: done ✅


max_n = 10


def head_cutter(n):
    stringed = str(n)
    aux = stringed[len(stringed) - max_n :]
    n = aux
    return n


n = 1
for k in range(1, 7830457 + 1):
    n = n * 2

    if len(str(n)) > 10:
        n = int(head_cutter(n))


n = 28433 * n + 1
print(head_cutter(n))
