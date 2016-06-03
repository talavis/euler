#!/usr/bin/env python3

'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

counts = {1: 1}

def collatz(n) :
    count = 0

    while n not in counts :
        if n % 2 == 0 :
            n //= 2
        else :
            n = 3 * n + 1
        count += 1
        if n in counts :
            count += counts[n]
        
    return count

if __name__ == '__main__' :
    for i in range(2, 1000000) :
        counts[i] = collatz(i)

    print(list(counts.keys())[list(counts.values()).index(max(counts.values()))])
