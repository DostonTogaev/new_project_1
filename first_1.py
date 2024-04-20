from decimal import Decimal, getcontext

getcontext().prec = 5

print(Decimal(10.0002) + Decimal(11.02))

from math import floor, ceil

print(floor(Decimal(1.1)))
print(ceil(Decimal(0.1)))

a = Decimal(2.6)
b = Decimal(3.0)
S = a * b
print(S)
