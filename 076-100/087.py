import numpy as np  # Status: done ✅

squares = []
cubes = []
fourths = []
limit = 50* 10**6


def prime_checker(n):
    isPrime = True
    for i in range(2, int(np.sqrt(n)) + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


def list_filler():
    i = 2
    j = 2
    k = 2
    while i**2 <= limit:
        if prime_checker(i):
            squares.append(i**2)
        i += 1

    while j**3 <= limit:
        if prime_checker(j):
            cubes.append(j**3)
        j += 1

    while k**4 <= limit:
        if prime_checker(k):
            fourths.append(k**4)
        k += 1


list_filler()

counter = 0
flag = [0] * limit

for s in range(0, len(squares)):
    for c in range(0, len(cubes)):
        for f in range(0, len(fourths)):
            sum = squares[s] + cubes[c] + fourths[f]
            if sum > limit:
                break
            if flag[sum] == 0:
                counter += 1
                flag[sum] = 1

print("There are exactly", counter, "numbers.")
