import numpy as np  # Status: done ✅


def digit_sorter(n):
    n = "".join(sorted(str(n)))
    return int(n)


found = False
x = 10
while not found:
    sorted_x = digit_sorter(x)
    if (
        digit_sorter(2 * x) - sorted_x == 0
        and digit_sorter(3 * x) - sorted_x == 0
        and digit_sorter(4 * x) - sorted_x == 0
        and digit_sorter(5 * x) - sorted_x == 0
        and digit_sorter(6 * x) - sorted_x == 0
    ):
        found = True
        print("The searched number is:", x)
        break
    x += 1
