import numpy as np  # pyright: ignore
from collections import OrderedDict


def digit_simplifier(n, m):  # doing orecchietta
    n = str(n)
    m = str(m)
    removed = False
    for i in range(0, len(str(m))):
        if i in str(n) and not removed:
            str(m)[i] = ""

            removed = True

    return n, m


for num in range(11, 100):
    for den in range(11, 100):
        red_num, red_den = digit_simplifier(num, den)

        print(num, den, red_num, red_den)
