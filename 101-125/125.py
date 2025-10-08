import math # Status: done ✅

limit = 10**8
squares = []
flag = [0] * limit
total = 0


def palindrome_checker(n):
    isPalindrome = True
    n = str(n)

    for digit in range(0, len(n)):
        if n[digit] == n[len(n) - digit - 1]:
            continue
        else:
            isPalindrome = False
    return isPalindrome


def iterator(input_list):
    global total

    for i in range(1, len(input_list) - 1):
        index = i
        sum = input_list[index] + input_list[index + 1]

        while sum < limit:
            if palindrome_checker(sum) and flag[sum] != 1:
                total += sum
                flag[sum] = 1

            if index < len(input_list) - 1:
                index += 1
                sum += input_list[index + 1]
            else:
                break

    return total


for i in range(0, 10**4):
    squares.append(i**2)

iterator(squares)
print("The sum is:", total)