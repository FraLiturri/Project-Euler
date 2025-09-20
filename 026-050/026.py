import numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 200


def period_finder(n):
    n = str(Decimal(1) / Decimal(n))
    l = len(n)
    candidate = []
    digits = []
    aux = []

    for k in range(2, l):
        digits.append(int(n[k]))
        if int(n[k]) in digits:
            if int(n[k]) in aux:
                j = k
                while int(n[j]) in aux and j + 1 < l:
                    candidate.append(int(n[j]))
                    if (
                        len(candidate) == len(aux)
                        and int(n[j + 1]) in candidate
                    ):
                        break
                    j += 1

            else:
                aux.append(int(n[k]))

            if len(candidate) == len(aux):
                break
        else:
            candidate = []
        if len(candidate) == len(aux):
            break
    return candidate


current_max = 0
current_d = 0

for d in range(2, 10):
    candidate = period_finder(d)

    if current_max < len(candidate):
        current_max = len(candidate)
        current_d = d

print(current_d)
print(Decimal(1)/(current_d))