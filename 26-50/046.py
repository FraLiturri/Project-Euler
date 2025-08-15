import numpy as np  # Status: done ✅ (can be improved, it's too much orecchietta)

squares = []
primes = []
golbach_odds = []


def square_gen(n):
    for i in range(0, n):
        squares.append(i**2)


def prime_gen(n):
    for j in range(2, n + 1):
        isPrime = True
        for i in range(2, int(np.sqrt(j)) + 1):
            r = j % i
            if r == 0:
                isPrime = False
        if isPrime:
            primes.append(j)
    return isPrime


prime_gen(10000)
square_gen(100)

for prime in primes:
    for square in squares:
        num = prime + 2 * square
        golbach_odds.append(num)

golbach_odds.sort()
golbach_odds = list(dict.fromkeys(golbach_odds))

prev_num = golbach_odds[0]
for i in range(1, len(golbach_odds)):
    if (
        golbach_odds[i] % 2 == 1
        and prev_num % 2 == 1
        and golbach_odds[i] - prev_num != 2
        and golbach_odds[i] < 10**4
    ):
        print("found", golbach_odds[i] - 2)
        break
    prev_num = golbach_odds[i]
