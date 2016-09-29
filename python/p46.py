#!/usr/bin/env python3

'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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


def main():
    primes = set(primes_sieve(10**4))
    max_prime = max(primes)
    
    i = 35
    while True:
        if i not in primes:
            goldbach = False
            j = 1
            while 2*j**2 < i:
                if i - 2*j**2 in primes:
                    goldbach = True
                    break
                j += 1
                
            if goldbach is False:
                print(i)
                break
        
        i += 2


main()
