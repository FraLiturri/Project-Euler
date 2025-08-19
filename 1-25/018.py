import numpy as np # Status: done ✅
 
with open("./data/0018_triangle.txt") as f:
    data = [list(map(int, r.split())) for r in f]

sum = data[0]


for i in range(1, len(data)):
    aux1 = sum + [0]
    aux2 = [0] + sum

    sum1 = [x + y for x, y in zip(aux1, data[i])]
    sum2 = [x + y for x, y in zip(aux2, data[i])]

    sum = [max(x, y) for x, y in zip(sum1, sum2)]

sum = np.array(sum)
print(sum.max())
