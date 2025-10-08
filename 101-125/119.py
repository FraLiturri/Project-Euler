import math  # Status: done ✅


def digit_summer(n):
    n = str(n)
    sum = 0
    for digit in n:
        sum += int(digit)

    return sum


counter = 0
results = []

for base in range(2, 100):
    for esp in range(2, 100):
        res = base**esp
        if digit_summer(res) == base:
            counter += 1
            results.append(res)

results = sorted(results)
print("a_30 is:", results[29])
