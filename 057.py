import numpy as np  # pyright:ignore ✅


def infinite_fraction(n): 
    previous = 0
    for i in range(1, n + 1):
        aux = 1 if i == 0 else 1 / (2 + previous)
        term = 1 + aux

        previous = aux
    return term


def terms_finder(n): #finds the number of fractions with #num > #den; here we find "x" in sqrt(2) = 1 + x
    counter = 0
    for i in range(1, n + 1):
        if i == 1:
            num = 1
            den = 2

        else:
            num = next_num
            den = next_den

        next_num = den
        next_den = 2 * den + num

        if len(str(num + den)) > len(str(den)):
            counter += 1
    return counter


print(terms_finder(1000))

