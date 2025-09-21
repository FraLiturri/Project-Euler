import numpy as np  # Status: done ✅


def is_perf_square(n):
    root = np.sqrt(n)
    root = np.floor(root)
    if root**2 == n:
        return True
    else:
        return False


b = 1
limit = 10**3
counters = [0] * (limit + 1)

while b + 2 < limit + 1:
    a = 0
    p = 0

    while a < b:
        a += 1
        if is_perf_square(a**2 + b**2):
            c = int(np.sqrt(a**2 + b**2))

            if a + b + c < limit + 1:
                counters[a + b + c] += 1
            else:
                break
    b += 1

print("The value of p is:", counters.index(np.max(counters)))
print("The max number of solutions is:", np.max(counters))
