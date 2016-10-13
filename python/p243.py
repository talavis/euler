#!/usr/bin/env python3

'''A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12.

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11.
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10.

Find the smallest denominator d, having a resilience R(d) < 15499/94744.'''

import sys


def get_pfactors(n, primes):
    if n < 2:
        return set()
    pfactors = set()
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            pfactors.add(p)
            n //= p
    if n > 1:
        pfactors.add(n)
    return pfactors


def resilience(denom, primes):
    factors = get_pfactors(denom, primes)
    nomi = [True] * denom
    nomi[0] = False
    for f in factors:
        for i in range(0, len(nomi), f):
            nomi[i] = False
    num_res = len([n for n in nomi if n == True])
    return num_res/(denom-1)


def test_resilience():
    primes = primes_sieve(6)
    assert resilience(12, primes) == 4/11


def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False

    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return [s[0] for s in enumerate(s) if s[1] is True]


def res_below_limit(limit, primes):
    d = 4
    res = 2/3
    while res >= limit:
        if d > primes[-1]:
            sys.stderr('Out of primes')
            sys.exit(1)
            break
        if d % 1000 == 0:
            print(d)
        d += 1
        res = resilience(d, primes)
    return d


def test_res_below_limit():
    primes = primes_sieve(15)
    assert res_below_limit(4/10, primes) == 12
    

if __name__ == '__main__':
    LIMIT = 15499/94744
    primes = primes_sieve(10**6)
    res_below_limit(LIMIT, primes)
