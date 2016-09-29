#!/usr/bin/env python3

'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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


def find_longest(upper_limit):
    primes = primes_sieve(upper_limit)

    longest = 1
    longest_sum = 1

    for i in range(0, len(primes)):
        p_range = [0,longest]
        while True:
            if primes[p_range[0]] > primes[i] // longest:
                break
            tmp = primes[p_range[0]:p_range[1]]
            tmpsum = sum(tmp)
            if tmpsum < primes[i]:
                p_range[1] += 1
            elif tmpsum > primes[i]:
                if len(tmp) < longest:
                    break
                p_range[0] += 1
            elif tmpsum == primes[i]:
                if len(tmp) > longest:
                    longest = len(tmp)
                    longest_sum = tmpsum
                # first hit should be the longest
                break
    return longest_sum

print(find_longest(10**6))

#assert find_longest(10**2) == 41
#assert find_longest(10**3) == 953

