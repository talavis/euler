#!/usr/bin/env python3

import sys

'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

highest = 0

for i in range(999,100, -1) :
    for j in range(999,100, -1) :
        s = i*j
        if str(s) == str(s)[::-1] :
            if s > highest :
                highest = s

print(highest)
