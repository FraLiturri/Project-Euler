import math # Status: done ✅

limit = 10**1
integers = [i for i in range(1, limit)]
int_copy = set(integers)

total = 0
counter = 0

def sum_calc(n):
    sum = 0
    for digit in str(n):
        sum += int(digit) ** 2

    return sum


def reducer(n):
    global total 
    input = n
    counter = 0

    while True:
        if n < limit and n in int_copy:
            int_copy.discard(n)

        n = sum_calc(n)
        counter += 1

        if n == 1 or n == 89:
            if n == 89:
                total += counter

            break

i = 0
while i < len(list(int_copy)):
    reducer(i) 
    i+=1
    
print(total)


