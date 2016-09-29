#!/usr/bin/env python3

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
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


def find_consecutive(nr_cons):
    primes = primes_sieve(10**6)
    consecutive = 0
    for i in range(1, max(primes)):
        pfactors = get_pfactors(i, primes)
        if len(set(pfactors)) == nr_cons:
            consecutive += 1
        else :
            consecutive = 0
        if consecutive == nr_cons:
            return i - nr_cons+1


def test_find_consecutive():
    assert find_consecutive(2) == 14
    assert find_consecutive(3) == 644


print(find_consecutive(4))
