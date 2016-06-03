#!/usr/bin/env python3

'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

import math

primes = [2]

i = 1
while i < 2000000 :
    i += 2
    isPrime = True
    p = 0
    root = math.sqrt(i)
    while primes[p] <= root :
        if i % primes[p] == 0 :
            isPrime = False
            break
        p += 1

    if isPrime :
        primes.append(i)
        
print(sum(primes))
