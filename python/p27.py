#!/usr/bin/env python3
'''Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.'''

def primes_sieve(limit):
    s = [0] * limit
    s[0] = 3
    s[1] = 3
    
    for i in range(len(s)) :
        if s[i] == 0 :
            for n in range(i*i, limit, i):
                s[n] += 1
    return s

MAX = 10**6

sieve = primes_sieve(MAX)
primes = set(i for i in range(len(sieve)) if sieve[i] == 0)

best = [0,0]
longest = 0
for a in range(-999, 1000) :
    for b in range(-999, 1000) :
        i = 0
        while i**2 + a*i + b in primes :
            i += 1
        if i > longest :
            longest = i
            best = [a, b]

print(best[0]*best[1])
