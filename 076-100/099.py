import numpy as np  # Status: done ✅

base, exp = np.loadtxt("./data/0099_base_exp.txt", delimiter=",", unpack=True)

saved_index = 0

for i in range(0, len(base)):
    r = exp[i] / exp[saved_index]
    if pow(base[i], r) >= base[saved_index]:
        saved_index = i

print("The searched line is", saved_index + 1)  # +1 for humans;
