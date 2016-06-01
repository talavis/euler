#!/usr/bin/env python3

'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?'''

import math

NUMBER = 600851475143

current = NUMBER
primes = [3]
i = 5

highest = 1

while i <= current :
    prime = True
    relevant = math.sqrt(i)
    for p in range(len(primes)) :
        if primes[p] > relevant :
            break
        if i % primes[p] == 0 :
            prime = False
            break
    if prime == True :
        primes.append(i)
        if current % i == 0 :
            current = current / i
            highest = i
    i += 2
    
print(highest)
