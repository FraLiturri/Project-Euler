import numpy as np  # Status: work in progress

def prime_checker(n):
    isPrime = True
    for i in range(2, n + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime

def square_checker(n): 
    isRoot = False
    root = np.sqrt(n)
    if n / round(root) == round(root): 
        isRoot = True
    #print(isRoot)
    return isRoot

counter = 0
for a in range(2, 101):
    if prime_checker(a):
        counter += 1
    if square_checker(a): 
        counter+=1

print(counter)
print(99*34)
