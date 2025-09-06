import numpy as np
from collections import OrderedDict  # 6.7 sec


triples = []
L = int(1.5 * 10**6)
sum = [0] * L


def pyth_triple_gen(limit):
    found = False
    m = 2
    while not found:
        n = 1
        while n < m:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            k = 1
            while (a + b + c) * k <= limit:
                triples.append([a * k, b * k, c * k])
                k += 1
            if a + b + c > limit:
                found = True
            n += 1
        m += 1
        if found:
            break


pyth_triple_gen(120)
triples = list(OrderedDict.fromkeys(triples))
total = 0
print(triples)

