import numpy as np  # pyright: ignore

counter = 0
n = 2
current_prime = 1

while counter < 10001:
    auxiliar = 2
    prime = False
    run = True
    while run:
        if n % auxiliar == 0:
            prime = False if auxiliar < n else True
            run = False
        auxiliar += 1
    if prime:
        counter += 1
        current_prime = n
    n = n + 1

print(current_prime)