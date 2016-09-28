#!/usr/bin/env python3

'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

DIGITS = set('123456789')

best = 0
# n=2, i=9999 -> 9 digits; n=2,i=10000 -> 10 digits
for i in range(1,9999):
    total = str(i)
    for n in range(2,9):
        total += str(i * n)
        if len(total) == 9:
            if int(total) > best and set(total) == DIGITS:
                best = int(total)
        elif len(total) > 9:
            break

print(best)
