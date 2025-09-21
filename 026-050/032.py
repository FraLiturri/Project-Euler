import numpy as np # Status: done ✅

candidates = []
flag_one = [0] * 10**6

def pandigital_checker(n):
    aux = [0] * 10
    aux[0] = 1
    is_pan = True
    for digit in str(n):
        digit = int(digit)
        if aux[digit] == 1:
            is_pan = False
            break
        else:
            aux[digit] = 1
    if np.sum(aux) != 10:
        is_pan = False
    return is_pan


for k1 in range(1, 10):
    for k2 in range(1000, 10000):
        if k1 * k2 > 1000 and k1 * k2 < 10**4 and flag_one[k1 * k2] == 0:
            candidate = k1 * 10**8 + k2 * 10**4 + k1 * k2
            if pandigital_checker(candidate):
                candidates.append(k1*k2)
                flag_one[k1 * k2] = 1

for k1 in range(10, 100):
    for k2 in range(100, 1000):
        if k1 * k2 > 1000 and k1 * k2 < 10**4 and flag_one[k1 * k2] == 0:
            candidate = k1 * 10**7 + k2 * 10**4 + k1 * k2
            if pandigital_checker(candidate):
                candidates.append(k1*k2)
                flag_one[k1 * k2] = 1

print("The sum is:", np.sum(candidates))