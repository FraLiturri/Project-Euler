import numpy as np  # Status: done ✅


def head_cutter(n):
    stringed = str(n)
    aux = stringed[99:]
    n = aux
    return n


decimal = ""
counter = 1
d = 1
found = 0
chopped = 0

while True:
    decimal = decimal + str(counter)
    if len(decimal) > 99:
        decimal = head_cutter(decimal)
        chopped += 1
        if (
            chopped == 1
            or chopped == 10
            or chopped == 100
            or chopped == 1000
            or chopped == 10000
        ):
            d = d * int(decimal[0])  # a little bit tricky;
            found += 1
        decimal = decimal[1:]
    counter += 1

    if found == 5:
        break

print("The product is:", d)
