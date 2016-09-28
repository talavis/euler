#!/usr/bin/env python3

'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

def test_numbers(digpos, digits, fullnum):
    pansum = 0
    
    for d in digits:
        if digpos == 1:
            if d == '0':
                continue
        elif digpos == 4:
            if int(d) % 2 != 0:
                continue
        elif digpos == 5:
            if int(fullnum[-2:] + d) % 3 != 0:
                continue
        elif digpos == 6:
            if int(d) % 5 != 0:
                continue
        elif digpos == 7:
            if int(fullnum[-2:] + d) % 7 != 0:
                continue
        elif digpos == 8:
            if int(fullnum[-2:] + d) % 11 != 0:
                continue
        elif digpos == 9:
            if int(fullnum[-2:] + d) % 13 != 0:
                continue
        elif digpos == 10:
            if int(fullnum[-2:] + d) % 17 == 0:
                pansum += int(fullnum + d)

        if digpos != 10:
            pansum += test_numbers(digpos + 1, digits[:digits.index(d)] + digits[digits.index(d)+1:], fullnum+d)
    return pansum       

DIGITS = '0123456789'
DIGITS_SET = set(DIGITS)

print(test_numbers(1, DIGITS, ''))
