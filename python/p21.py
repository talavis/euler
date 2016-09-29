#!/usr/bin/env python3

'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''

import math

def get_divs(value):
    divs = [1]
    for d in range(2, math.ceil(value**0.5)):
        if value % d == 0:
            divs.append(d)
            divs.append(value//d)
    return set(divs)

amic = list()
for i in range(2, 10000) :
    if i in amic :
        continue
    comp1 = sum(get_divs(i))
    comp2 = sum(get_divs(comp1))
    if i == comp2 and comp1 != comp2 :
        amic.append(i)
        amic.append(comp1)

print(sum(amic))
