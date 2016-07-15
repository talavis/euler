#!/usr/bin/env python3

'''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''

import math

def is_abundant(number) :
    divs = [1]

    root = int(math.sqrt(number))
    for i in range(2, root + 1) :
        if number % i == 0 :
            divs.append(i)
            divs.append(number//i)
    divs = set(divs)
        
    return sum(divs) > number 

an = [12] # 12 is the smallest abundant number

MAX = 28124

for i in range(13, MAX) :
    if is_abundant(i) :
        an.append(i)

ans = set(an)
non_sum = 0

for i in range(1, MAX) :
    non = True
    half = i//2+1 # if no hits before half -> not a sum
    for j in range(0, len(an)) :
        if an[j] >= half :
            break
        if i - an[j] in ans :
            non = False
            break
        
    if non :
        non_sum += i

print(non_sum)
