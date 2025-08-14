import numpy as np  # Status: done ✅

digits = []
max = 0


def palindrome_chekcer(n):

    isPalindrome = True
    for i in range(0, len(str(n))):
        digit = (n / 10**i) % 10
        digit = int(digit)
        digits.append(digit)
    for k in range(0, len(digits)):
        if digits[k] != digits[len(digits) - 1 - k]:
            isPalindrome = False
    digits.clear()
    return isPalindrome


for i in range(1, 1000):
    for j in range(1, 1000):
        if palindrome_chekcer(i*j):
            max = i*j if max < i*j else max


print(max)
