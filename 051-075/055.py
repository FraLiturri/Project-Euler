import numpy as np  # Status: done ✅ (Lycherel's numbers and all the stuff like that = mental fellatio (first axiom of theoretical physics))


def palindrome_chekcer(n):
    digits = []
    isPalindrome = True
    for i in range(0, len(str(n))):
        digit = (n / 10**i) % 10
        digit = int(digit)
        digits.append(digit)

    for k in range(0, len(digits)):
        if digits[k] != digits[len(digits) - 1 - k]:
            isPalindrome = False

    return isPalindrome


def inverter(n):
    n = str(n)
    return n[::-1]


def is_Lychrel(n):
    is_lych = True
    for i in range(0, 50):
        inverse = inverter(n)
        n = n + int(inverse)
        if palindrome_chekcer(n):
            is_lych = False
            break
    
    return is_lych

counter = 0
limit = 10**4

for n in range(1, limit):
    if is_Lychrel(n):
        counter += 1

print(counter)