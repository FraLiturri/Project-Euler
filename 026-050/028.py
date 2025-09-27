import numpy as np  # Status: done ✅

n = 1001
numbers = []
s = 0

for i in range(0, n**2 + 1):
    numbers.append(i)

j = 1
k = 2
sum = 0

while j + k < len(numbers):
    sum += numbers[j]
    if numbers[j] == (k + 1) ** 2:
        k += 2
    j = j + k


print("The sum is:", sum + (k + 1) ** 2)
