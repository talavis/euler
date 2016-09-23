#!/usr/bin/env python3

'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

def make_combinations(target, currencies):
    '''
    Generate all currency combinations.
    currencies[0] is the current one.
    '''
    total = 0
    for i in range(target, -1, -currencies[0]):
        if len(currencies) > 1 :
            total += make_combinations(i, currencies[1:])
        else :
            return 1
    return total
        
CURRENCIES = (200, 100, 50, 20, 10, 5, 2, 1)
TARGET = 200

print(make_combinations(TARGET, CURRENCIES))
