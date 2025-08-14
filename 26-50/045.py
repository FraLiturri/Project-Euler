import numpy as np # Status: work in progress

triangular = np.array([], dtype=int)
pentagonal = np.array([], dtype=int)
exagonal = np.array([], dtype=int)


def triangle_gen(n):
    res = n * (n + 1) / 2
    return res


def pentagonal_gen(n):
    res = n * (3 * n - 1) / 2
    return res


def exagon_gen(n):
    res = n * (2 * n - 1)
    return res


limit = 100
step = 10
initial_value = 50
found = False
extended = False

while not found:
    for n in range(initial_value, limit):
        triangular = np.append(triangular, triangle_gen(n))
        pentagonal = np.append(pentagonal, pentagonal_gen(n))
        exagonal = np.append(exagonal, exagon_gen(n))

    diff1 = triangular - pentagonal
    diff2 = pentagonal - exagonal

    if 0.0 in diff1 and 0.0 in diff2:
        found = True
        print(n)

    if not found and not extended:
        n = n + step
        limit = limit + step
        triangular = np.array([])
        pentagonal = np.array([])
        exagonal = np.array([])
        extended = True
