#!/usr/bin/env python3

'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

import math

primes = [2]

i = 1
while len(primes) < 10001 :
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
        
print(primes[-1])
