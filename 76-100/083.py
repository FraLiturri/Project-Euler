import numpy as np # Status: work in progress

with open("./data/0081_matrix.txt", "r") as f:
    righe = f.readlines()

data = [list(map(int, riga.strip().split(","))) for riga in righe]

n, m = 80, 80  # righe, colonne
aux = [
    [0 for _ in range(m)] for _ in range(n)
]  # auxiliar matrix: helps to remember if we have already been on a site;


def been_there(i, j):
    aux[i][j] = 1


def updater(i, j):  # i = row, j = col
    been_there(i, j)

    if i == 0 and j == 0:
        data[i + 1][j] += data[i][j]
        data[i][j + 1] += data[i][j]

    if i == 0 and j > 0:
        if j < len(data[0]):
            data[i][j + 1] += data[i][j]
            data[i + 1][j] += data[i][j]
        else:
            data[i + 1][j] += data[i][j]

    if i > 0 and j == 0:
        if i < len(data):
            data[i + 1][j] += data[i][j]
            data[i][j + 1] += data[i][j]
        else:
            data[i][j + 1] += data[i][j]

    if i > 0 and j > 0:

        first = data[i][j - 1]
        second = data[i - 1][j]
        data[i][j] += min(first, second)


for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        updater(i, j)

print("The path has minimum sum of:", data[79][79])
