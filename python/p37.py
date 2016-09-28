#!/usr/bin/env python3

'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def test_truncation(number, primes):
    if number not in primes:
        return False
    strnum = str(number)

    for i in range(1, len(strnum)):
        if int(strnum[i:]) not in primes or int(strnum[:-i]) not in primes:
            return False
    return True
        
def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False

    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return [s[0] for s in enumerate(s) if s[1] == True]

sieve = primes_sieve(10**6)

sieve_set = set(sieve)

primesum = 0
# first four are 2,3,5,7; should be skipped
for i in range(4, len(sieve)):
    if test_truncation(sieve[i], sieve_set) :
        primesum += sieve[i]

print(primesum)
