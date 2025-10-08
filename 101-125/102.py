import numpy as np  # Status: done ✅

x_A, y_A, x_B, y_B, x_C, y_C = np.loadtxt(
    "./data/0102_triangles.txt", unpack=True, delimiter=","
)

is_zero = 0
counter = 0

def inter_finder(x1, y1, x2, y2):
    global is_zero
    if x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0:
        is_zero +=1
        
    if y2 == y1 or x2 == x1:
        if y2 == y1 and y2 != 0:
            y_inter.append(y2)
        if x2 == x1 and x2 != 0:
            x_inter.append(x2)

    else:
        m = (y2 - y1) / (x2 - x1)
        q = (x2 * y1 - x1 * y2) / (x2 - x1)

        x_aux = -q / m
        y_aux = q

        if x_aux > min(x1, x2) and x_aux < max(x1, x2):
            x_inter.append(-q / m)
        if y_aux > min(y1, y2) and y_aux < max(y1, y2):
            y_inter.append(q)

for k in range(0, len(x_A)):
    x_inter = []
    y_inter = []

    inter_finder(x_A[k], y_A[k], x_B[k], y_B[k])
    inter_finder(x_B[k], y_B[k], x_C[k], y_C[k])
    inter_finder(x_C[k], y_C[k], x_A[k], y_A[k])

    if len(x_inter) == len(y_inter) == 2:
        if np.sign(x_inter[0]) != np.sign(x_inter[1]):
            if np.sign(y_inter[0]) != np.sign(y_inter[1]):
                counter += 1

print(counter + is_zero//2) # is_zero counts the triangles which have the origin on one of their sides;
                            # has to be divided by two since in lines 37-39 it's counted twice;
