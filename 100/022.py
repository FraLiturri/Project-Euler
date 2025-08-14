import numpy as np  # Status: done ✅

tot_value = 0
names = np.loadtxt("./data/names.txt", dtype=str)
names.sort()

letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def value_associator(name, index):
    value = 0
    global tot_value
    for letter in name:
        value += letters.index(letter) + 1

    value = value * (index + 1)
    tot_value += value
    return tot_value


for i in range(0, len(names)):
    value_associator(names[i], i)

print("The total value is:", tot_value)
