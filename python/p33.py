#!/usr/bin/env python3

'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.'''

def get_gcd(n1, n2, sieve):
    gcd = 1
    for p in sieve:
        if p*p > min(n1, n2):
            break
        while n1 % p == 0 and n2 % p == 0:
            gcd *= p
            n1 //= p
            n2 //= p
    if n2 % n1 == 0:
        gcd *= n1
    if n1 % n2 == 0:
        gcd *= n2
    return gcd

def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False

    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return [s[0] for s in enumerate(s) if s[1] == True]

n_prod = 1
d_prod = 1

for d in range(10, 100):
    dstr = str(d)
    for n in range(10, d):
        nstr = str(n)
        if '0' not in nstr:
            # should never happen, but...
            if nstr[0] in dstr:
                match = int(not dstr.index(nstr[0]))
                try:
                    if int(nstr[1])/int(dstr[match]) == n/d:
                        n_prod *= n
                        d_prod *= d
                except:
                    pass
            elif nstr[1] in dstr:
                match = int(not dstr.index(nstr[1]))
                try:
                    if int(nstr[0])/int(dstr[match]) == n/d:
                        n_prod *= n
                        d_prod *= d
                except:
                    pass

sieve = primes_sieve(int(max(n_prod, d_prod)**0.5))

common = get_gcd(n_prod, d_prod, sieve)
# n is not needed, but calculating anyway
final_n = n_prod//common
final_d = d_prod//common

print(final_n, final_d)
