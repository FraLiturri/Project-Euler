import numpy as np # Status: done ✅


def is_leap(n):
    if n % 4 == 0 and n != 1900:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


counter = 0
r = 0

for year in range(1900, 2001):
    months = is_leap(year)
    months[0] = months[0] + r

    for k in range(0, 12):
        if year == 1900:
            months[0] = 24
        r = months[k] % 7
        if k < 11:
            months[k + 1] = months[k + 1] + r
        if r == 6:
            counter += 1

print(counter - 2 )  # We are counting from 1900, 
                     # so we need to subtract the 
                     # Sundays that fell on the first 
                     # of the month on that year;
