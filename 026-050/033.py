import numpy as np  # Status: work in progress


def simplifier(num, den):
    if den % 10 != 0:
        for num_dig in str(num):
            num_aux = list(str(num))
            den_aux = list(str(den))

            if num_dig in str(den):
                num_aux.remove(num_dig)
                den_aux.remove(num_dig)
    return [num_aux, den_aux]


print(simplifier(22, 32))
