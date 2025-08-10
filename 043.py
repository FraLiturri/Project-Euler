import numpy as np  # pyright: ignore
from collections import OrderedDict

primes = [2, 3, 5, 7, 11, 13, 17]
all = []
pandigitals = []
final = []

for p in primes:
    i = 1
    string = ""
    multi = []
    while i * p < 1000:
        string = "00" + str(p) if p < 10 else "0" + str(p)
        string = "0" + str(p * i) if p * i < 100 else str(p * i)
        multi.append(string)
        i += 1
    all.append(multi)


for two in all[0]:  # making orecchietta;
    aux = ""
    for three in all[1]:
        if int(str(two)[1:]) == int(str(three)[:2]):
            for five in all[2]:
                if int(str(three)[1:]) == int(str(five)[:2]):
                    for seven in all[3]:
                        if int(str(five)[1:]) == int(str(seven)[:2]):
                            for eleven in all[4]:
                                if int(str(seven)[1:]) == int(str(eleven)[:2]):
                                    for tirteen in all[5]:
                                        if int(str(eleven)[1:]) == int(
                                            str(tirteen)[:2]
                                        ):
                                            for seventeen in all[6]:
                                                if int(str(tirteen)[1:]) == int(
                                                    str(seventeen)[:2]
                                                ):

                                                    aux = (
                                                        str(two)
                                                        + str(three)[2:]
                                                        + str(five)[2:]
                                                        + str(seven)[2:]
                                                        + str(eleven)[2:]
                                                        + str(tirteen)[2:]
                                                        + str(seventeen)[2:]
                                                    )
                                                    pandigitals.append(aux)

for pandigital in pandigitals:
    stringed = "".join(OrderedDict.fromkeys(str(pandigital)))

    if len(stringed) == 9:
        sum = 0
        for digit in stringed:
            sum += int(digit)
        missing_digit = int(9 * 10 / 2) - sum
        pandigital = int(str(missing_digit) + pandigital)

        final.append(pandigital)

final = np.array(final)
print(np.sum(final))
