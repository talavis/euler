#!/usr/bin/env python3
'''Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of 
the square spiral for which the ratio of primes along both diagonals first falls below 10%?'''

def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False
    
    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return [s[0] for s in enumerate(s) if s[1] == True]

def get_pfactors(n, sieve):
    if n < 2:
        return list()
    pfactors = list()
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            pfactors.append(p)
            n //= p
    if n > 1:
        pfactors.append(n)
    return pfactors

# the corners in the spiral are increasing by n-1, where n is the side of the spiral
diag_primes = 3
diag_total = 5

# precalculation
primes = primes_sieve(10**5)

i = 5
current = 9
while diag_primes/diag_total > 0.1:
    for j in range(3): # four sides, one is always non-prime
        current += i-1
        if len(get_pfactors(current, primes)) == 1:
            diag_primes += 1
    current += i-1
    diag_total += 4
    i += 2
print(i-2)
