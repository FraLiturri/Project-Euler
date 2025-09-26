import numpy as np # Status: done ✅


def digit_sorter(n):
    n = "".join(sorted(str(n)))
    return n


n = 8400 # upper limit has to be increased gradually 
         # since there might be permutations-cube with 
         # more than five combinations, triggering
         # line 27; n = 8400 is good.

candidates = []
counters = [1] * n
found = False

for i in reversed(range(1, n)):
    power = i**3
    sorted_i = digit_sorter(power)

    if sorted_i in candidates:
        candidates.append(0)
        index = candidates.index(sorted_i)
        counters[index] += 1

        if counters[index] == 5:
            print("The smallest cube is:", power)
            found = True
            break
    else:
        candidates.append(sorted_i)

    if found:
        break

