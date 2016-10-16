#!/usr/bin/env python3

'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''


def get_pfactors(n, primes):
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


def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False

    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return [s[0] for s in enumerate(s) if s[1] is True]


def reduced(n, d, primes):
    n_fac = get_pfactors(n, primes)
    for i in range(len(n_fac)):
        if d % n_fac[i] == 0:
            n = n // n_fac[i]
            d = d // n_fac[i]
    return (n, d)


def test_reduced():
    primes = primes_sieve(100)
    assert reduced(50,100, primes) == (1, 2)
    assert reduced(37,111, primes) == (1, 3)
    assert reduced(24,120, primes) == (1, 5)


best = (0,0,0)
REF = 3/7
for d in range(7, 10**6+1):
    start = int(d * 3/7)
    for n in range(int(d*3/7), int(d*4/7)):
        if n/d >= REF:
            break
        if n/d > best[2]:
            best = (n, d, n/d)

primes = primes_sieve(d)
print(reduced(best[0], best[1], primes))
