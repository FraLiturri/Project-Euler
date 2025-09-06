import numpy as np  # Status: done ✅


def palindrome_checker(n):
    isPalindrome = True
    n = str(n)
    for digit in range(0, len(n)):
        if n[digit] == n[len(n) - digit - 1]:
            continue
        else:
            isPalindrome = False
    return isPalindrome


def binary_converter(n):
    n = str(bin(n))
    n = n[2:]
    return n


sum = 0
for i in range(0, 10**6):
    if palindrome_checker(i):
        if palindrome_checker(int(binary_converter(i))):
            sum += i

print(sum)
