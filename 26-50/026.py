import numpy as np # Status: work in progress
from decimal import Decimal, getcontext

getcontext().prec = 100


print(1/11, 1/12, 1/13, 1/14, 1/843)
print(Decimal(1)/Decimal(843))

print(divmod(1, 843))