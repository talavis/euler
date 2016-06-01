#!/usr/bin/env python3

'''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

# the sum is 101*50 = 5050

sqsum = 0
for i in range(1, 101) :
    sqsum += i**2

print(5050**2-sqsum)
