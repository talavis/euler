#!/usr/bin/env python3

'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1			1	2
3	1,2			2	1.5
4	1,3			2	2
5	1,2,3,4			4	1.25
6	1,5			2	3
7	1,2,3,4,5,6		6	1.1666...
8	1,3,5,7			4	2
9	1,2,4,5,7,8		6	1.5
10	1,3,7,9			4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False
    
    for i in range(len(s)):
        if s[i] is True :
            for n in range(i*i, limit, i):
                s[n] = False
    return [s[0] for s in enumerate(s) if s[1] == True]


def find_best_nphi(limit = 10**6):    
    # The ratio n / phi will always be the greatest when as many numbers i
    # i <= n are divisible by the same factors as n
    # Thus the greatest ratio for n <= 100000 should be the greatest product
    # < 1000000 of unique primes.
    primes = primes_sieve(int(limit**0.5)+1)
    prime_product = 1
    p = 0
    while prime_product * primes[p] < limit:
        prime_product *= primes[p]
        p += 1
    return(prime_product)


if __name__ == '__main__':
    result = find_best_nphi()
    print(result)
