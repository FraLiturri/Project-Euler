import numpy as np  # Status: done ✅

pentagon_numbers = []
limit = 10**7  # Has to be increased if necessary; 10**7 is enough, though;


def pentagon_gen(N):
    P_n = 0
    n = 1
    global pentagon_numbers
    while P_n < N:
        P_n = n * (3 * n - 1) // 2
        pentagon_numbers.append(P_n)
        n += 1


pentagon_gen(limit)
aux = set(pentagon_numbers)

shift = 1
found = False

while not found:
    for k in range(0, len(pentagon_numbers) - shift):
        S = pentagon_numbers[k] + pentagon_numbers[k + shift]
        if S in aux:
            D = pentagon_numbers[k + shift] - pentagon_numbers[k]
            if D in aux:
                found = True
                print("The result is D =", D)
                break
    shift += 1
    if shift >= len(pentagon_numbers):
        print("Not found, increase upper limit.")
        break
