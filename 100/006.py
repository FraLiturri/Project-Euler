import numpy as np # Status: done ✅

square_sum = 0
sum_square = (100*101/2)**2

for i in range(1,101): 
    square_sum += i**2

print(sum_square - square_sum)

