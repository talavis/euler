#!/usr/bin/env python3

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False

    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return [s[0] for s in enumerate(s) if s[1] is True]

DIGITS='123456789'

# the number should have no more than 7 digits
# any 9 and 8 digit number will be divisible by 3
primes = primes_sieve(7654321)

current_digits = set(DIGITS)

for i in range(1,len(primes)):
    if len(str(primes[-i])) < len(current_digits):
        current_digits = set(DIGITS[:len(str(primes[-i]))])
    if set(str(primes[-i])) == current_digits:
        print(primes[-i])
        break
