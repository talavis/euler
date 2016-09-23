#!/usr/bin/env python3

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n 
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include 
it once in your sum.
'''

def is_pandigital(text) :
    '''
    Test if the supplied string contains the digits 1-9
    exactly once
    '''
    
    if set(text) == set('123456789'):
        return True
    return False

pansum = 0
known = set()
# values i, j are not greater than 1000; 9999*1=9999
for i in range(1, 10000):
    for j in range(1, 10000):
        if len('{}{}{}'.format(i, j, i*j)) > 9:
               break
        if is_pandigital('{}{}{}'.format(i, j, i*j)) and i*j not in known:
            pansum += i*j
            known.add(i*j)
print(pansum)
