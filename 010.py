import numpy as np  # pyright:ignore


limit = 2 * 10**6
s = limit * (limit + 1) / 2
x = 0
not_prime = []


def multi_finder(n, max):
    i = 2
    while i <= int(max / n):
        not_prime.append(n * i)
        i = i + 1
    return not_prime


for i in range(2, limit):
    multi_finder(i, limit)

not_prime = list(dict.fromkeys(not_prime))

for i in range(0, len(not_prime)):
    x = x + not_prime[i]

print(s - x - 1)
