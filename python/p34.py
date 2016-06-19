#!/usr/bin/env python3

'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''

import math

totalsum = 0

for i in range(10, 2999999) : # can't be greater
    tmp = str(i)
    tmpsum = 0
    for d in tmp :
        tmpsum += math.factorial(int(d))
    if tmpsum == i :
        totalsum += tmpsum

print(totalsum)
