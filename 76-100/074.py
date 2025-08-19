import numpy as np
from math import factorial
from collections import OrderedDict  # 6.7 sec

cleaned_naturals = []


def sorter(n):
    for i in range(0, n):
        i = sorted(str(i))
        number = ""
        for element in i:
            number += str(element)
        cleaned_naturals.append(int(number))


def calc(n):
    res = 0
    for number in str(n):
        res += factorial(int(number))
    return res


sorter(101)
cleaned_naturals = list(OrderedDict.fromkeys(cleaned_naturals))


counter = 0
visited = [0] * len(cleaned_naturals)


for element in cleaned_naturals:
    elment = calc(element)


print(len(cleaned_naturals))
print(cleaned_naturals)