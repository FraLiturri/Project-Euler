import numpy as np  # pyright: ignore


def Fibonacci(n):
    prev = 1
    two_prev = 1
    F_n = 1
    for i in range(0, n + 1):
        F_n = prev + two_prev if i > 1 else 1
        two_prev = prev if i > 0 else 1
        prev = F_n
    return F_n


i = 1
special_index = 0
sum = 1 #initial term has to be considered
while i > 0:
    if Fibonacci(i) < 4 * 10**6:
        if Fibonacci(i) % 2 == 1: 
            sum += Fibonacci(i)
        i = i+1

    elif Fibonacci(i) > 4*10**6: 
        break
 
print(sum)