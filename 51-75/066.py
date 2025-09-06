import numpy as np
import math

saved_values = []
limit = 7


def square_checker(n):
    isSquare = False
    root = math.isqrt(n)
    if int(root) ** 2 == n:
        isSquare = True
    else:
        isSquare = False
    return isSquare


for D in range(2, limit + 1):
    print(D)
    if square_checker(D):
        D = D + 1
    else:
        y_square = 2
        while True:
            multi = D * y_square**2
            y_square += 1
            if square_checker(multi + 1):
                saved_values.append(np.sqrt(multi + 1))
                break


print(saved_values)
