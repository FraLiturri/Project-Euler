import math # Status: done ✅


def is_bouncing(n):
    str_n = str(n)
    is_decr = False
    is_incr = False

    for i in range(0, len(str_n) - 1):
        if str_n[i] < str_n[i + 1]:
            is_incr = True
        if str_n[i] > str_n[i + 1]:
            is_decr = True

    if is_decr and is_incr:
        return True

    else:
        return False

counter = 0
ratio = 0
number = 100

while ratio < 99:
    if is_bouncing(number):
        counter +=1
    
    ratio = counter / number * 100
    number += 1

print("The result is:",  number-1)

