import numpy as np
import math

squares = []
minimal_sol = []
limit = 66
test = []


def squares_god(n):
    for k in range(1, n + 1):
        squares.append(k**2)
    return squares

squares_god(10**8)
squares = set(squares)

for D in range(2, limit):
    if D not in squares:
        y = 1
        while True:
            if 1 + D * y**2 in squares:
                print(y)
                minimal_sol.append(1 + D * y**2)
                break

            y += 1
            

print(test)