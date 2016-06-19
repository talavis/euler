#!/usr/bin/env python3

'''A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10**8, have precisely two, not necessarily distinct, prime factors?'''

import math

def primes_sieve(limit):
    s = [0] * limit
    s[0] = 3
    s[1] = 3
    
    for i in range(len(s)) :
        if s[i] == 0 :
            for n in range(i*i, limit, i):
                s[n] += 1
    return s

MAX = 10**8

amount = 0

sieve = primes_sieve(MAX)
primes = list(i for i in range(len(sieve)//2) if sieve[i] == 0)

for i in range(4, MAX) :
    if sieve[i] > 2 or sieve[i] == 0 :
        continue
    p = 0
    tmp = i
    while p < len(primes) and tmp >= primes[p] :
        if tmp % primes[p] == 0 :
            tmp  = tmp // primes[p] 
            if sieve[tmp] == 0 : # the remainder must also be prime if there are two divisors
                amount += 1
                break
            else :
                break
    
        p += 1

print(amount)
