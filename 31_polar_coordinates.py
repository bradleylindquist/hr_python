# r = first
# t = last

import cmath

first = '1+2j'
# first = '-80+25j'
# first = '-1-5j'

x = list(first)

sign = 0
index = len(x) - 1
while index > 0:
  if (x[index] == '+' or x[index] == '-'):
    sign = index
    break
  index -=1

r = float(first[slice(sign)])
t = float(first[slice(sign, -1)])

print(abs(complex(r, t)))
print(cmath.phase(complex(r, t)))