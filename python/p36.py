#!/usr/bin/env python3

'''
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

total = 0
for i in range(1000000):
    decimal = str(i)
    if decimal[-1] == '0' :
        continue
    binary = '{:b}'.format(i)
    if binary[0] == '0' or binary[-1] == '0' :
        continue
    if decimal == decimal[::-1] and binary == binary[::-1]:
        total += i
        
print(total)
