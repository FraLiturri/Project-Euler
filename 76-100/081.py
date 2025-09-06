import numpy as np # Status: done ✅

with open("./data/0081_matrix.txt", "r") as f:
    righe = f.readlines()

data = [list(map(int, riga.strip().split(","))) for riga in righe]


def updater(i, j):  # i = row, j = col
    if i == 0 and j > 0:
        data[i][j] += data[i][j - 1]
    if i > 0 and j == 0:
        data[i][j] += data[i - 1][j]
    if i > 0 and j > 0:
        first = data[i][j - 1]
        second = data[i - 1][j]
        data[i][j] += min(first, second)


for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        updater(i, j)

print("The path has minimum sum of:", data[79][79])
