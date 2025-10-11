import numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 50

inf = 10**12 + 10**4
limit = 10**12 + 10**6

for i in range(inf, limit):

    candidate = Decimal(1 + np.sqrt(1 + 4 * i * (i - 1) / (2))) / Decimal(2)

    if round(candidate - 10**12) + 1.0 == candidate - 10**12 + 1 and candidate * (candidate - 1) / (i * (i - 1)) == 0.5:

        print("The searched number of blue disks is:", candidate)
        print(i - 10**12, candidate * (candidate - 1) / (i * (i - 1)))

