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
for k in range(10**10, 10**10 + 10**7):
    if is_bouncing(k):
        counter +=1

print(counter)

