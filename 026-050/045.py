import numpy as np  # Status: done ✅


def triangle_gen(n):
    res = n * (n + 1) / 2
    return res


def pentagonal_gen(n):
    res = n * (3 * n - 1) / 2
    return res


def exagon_gen(n):
    res = n * (2 * n - 1)
    return res


found = False
t = 286
p = 165
e = 143
while not found:
    triangular = triangle_gen(t)
    t += 1
    while pentagonal_gen(p) <= triangular:
        p += 1
        if pentagonal_gen(p) == triangle_gen(t):
            while exagon_gen(e) < pentagonal_gen(p):
                e += 1
                if exagon_gen(e) == pentagonal_gen(p):
                    found = True
    if found:
        break


print("The next one is:", triangle_gen(t))
