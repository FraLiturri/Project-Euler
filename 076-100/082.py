import numpy as np  # Status: work in progress

with open("./data/0082_matrix.txt", "r") as f:
    righe = f.readlines()

data = [list(map(int, riga.strip().split(","))) for riga in righe]

data = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


def updater(i, j):  # i = row, j = col
    if i == 0:
        if j == 0:
            data[i][j] += data[i + 1][j]
        else:
            first = data[i][j - 1]
            second = data[i + 1][j]
            data[i][j] += min(first, second)
    if i > 0 and j == 0:
        if i == len(data) - 1:
            data[i][j] += data[i - 1][j]
        else:
            first = data[i - 1][j]
            second = data[i + 1][j]
            data[i][j] += min(first, second)

    if i > 0 and j > 0:
        first = data[i][j - 1]
        second = data[i - 1][j]
        if i == len(data[0]) - 1:
            first = data[i][j - 1]
            second = data[i - 1][j]
            data[i][j] += min(first, second)
        else:
            first = data[i][j - 1]
            second = data[i - 1][j]
            third = data[i + 1][j]
            data[i][j] += min(first, second, third)


for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        updater(i, j)

print(data)
