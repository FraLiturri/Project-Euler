import numpy as np

counter = 0
b = 1
limit = 20
reached = False
while True:
    for i in range(1, b + 1):
        if i == 1:
            if counter + b > limit:
                reached = True
            else:
                counter += b

        else:
            if counter + b%i +1 > limit:
                reached = True
            else:
                counter += b % i + 1          

            num = b % i + 1
            #print("b", b, "; i", i, num)

    b += 1
    if reached:
        break

print(counter)
print(b)
