#!/usr/bin/env python3

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import sys

def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False
    
    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return (s[0] for s in enumerate(s) if s[1] == True)


# 4-digit numbers -> only need primes below 10000
primes = primes_sieve(10000)

# only 4-digit ones matter
primes = [prime for prime in primes if prime >= 1000]

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        diff = primes[j] - primes[i]
        if primes[j] + diff in primes:
            # contains same digits
            if set(str(primes[i])) == set(str(primes[j])) and set(str(primes[i])) == set(str(primes[j] + diff)):
                all_digits = str(primes[i]) + str(primes[j]) + str(primes[j] + diff)
                if all_digits != '148748178147':
                    print(all_digits)
                    sys.exit(0)
        if primes[j] + diff > max(primes):
            break
        
