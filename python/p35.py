#!/usr/bin/env python3

'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''

def primes_sieve(limit):
    s = [True] * limit
    s[0] = False
    s[1] = False
    
    for i in range(len(s)) :
        if s[i] == True :
            for n in range(i*i, limit, i):
                s[n] = False
    return s

LIMIT = 1000000

numcirc = 0

sieve = primes_sieve(LIMIT)

for i in range(2, LIMIT) :
    num = str(i)
    circ = True
    for c in range(len(num)) :
        if sieve[int(num)] == False :
            circ = False
            break
        num = num[-1] + num[:-1]
    if circ :
        numcirc += 1

print(numcirc)
