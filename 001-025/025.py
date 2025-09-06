import numpy as np # Status: done ✅

def Fibonacci(n):
    prev = 1
    two_prev = 1
    F_n = 1
    for i in range(0, n + 1):
        F_n = prev + two_prev if i > 1 else 1
        two_prev = prev if i > 0 else 1
        prev = F_n
    return F_n

found = False
n = 1
while not found:
    if len(str(Fibonacci(n))) < 10**3:
        n = n+1
    else:
        found = True
        print("The first term is the:", n + 1) 

