import numpy as np  #Status: work in progress

def prime_checker(n):
    isPrime = True
    for i in range(2, n + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


def quadratic(n, a, b):
    return n**2 + a * n + b


run = True
n = 0
current_max = 0
current_a = -1000
current_b = -1000

while run:
    a = 0
    b = 0
    while a < 10:
        while b <= 10:
            if prime_checker(quadratic(n, a, b)):
                a = a + 3
                b = b + 1
            else:
                current_a = a if a > current_a else current_a
                current_b = b if b > current_b else current_b
                run = False
                n = 0
