#!/usr/bin/env python3

'''
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100100 is almost 
unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the 
digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

highest = 0
for a in range(1, 100):
    for b in range(1,100):
        tmp = sum([int(d) for d in str(a**b)])
        if tmp > highest:
            highest = tmp

print(highest)
