import numpy as np # Status: work in progress

n = 5
numbers = []
s = 0


def prime_checker(n):
    isPrime = True
    if n < 0:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        r = n % i
        if r == 0:
            if i != n:
                isPrime = False
    return isPrime


for i in range(0, n**2 + 1):
    numbers.append(i)

j = 1
k = 2
sum = 0
ratio = 0
counter = 0
found = False

while not found:
    while j + k < len(numbers):
        sum += numbers[j]
        if numbers[j] == (k + 1) ** 2:
            k += 2
            if prime_checker(numbers[j]):
                counteer += 1
        j = j + k
        ratio = counter * 100 / (n + n + 1)

        if ratio <= 10:
            print(n)
            found = True
            break
        else:
            n += 1
    if found:
        break


