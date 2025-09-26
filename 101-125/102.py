import numpy as np # Status: work in progress

x_A, y_A, x_B, y_B, x_C, y_C = np.loadtxt(
    "./data/0102_triangles.txt", unpack=True, delimiter=","
)


def inter_finder(x1, y1, x2, y2):
    inter = []
    m = (y2 - y1) / (x2 - x1)
    q = (x2 * y1 - x1 * y2) / (x2 - x1)

    x_bar = -q / m
    y_bar = q

    inter.append(x_bar)
    inter.append(y_bar)
    return inter


counter = 0
for i in range(0, len(x_A)):
    if x_A[i] != x_B[i] and y_A[i] != y_B[i] and x_A[i] != x_C[i] and y_A[i] != y_C[i]:
        inter1 = inter_finder(x_A[i], y_A[i], x_B[i], y_B[i])
        inter2 = inter_finder(x_C[i], y_C[i], x_A[i], y_A[i])

        if np.sign(inter1[1]) == -np.sign(inter2[1]) and np.sign(inter1[0]) == -np.sign(
            inter2[0]
        ):
            counter += 1

print(counter)
