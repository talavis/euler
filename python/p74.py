#!/usr/bin/env python3

'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''

import math


def fact_sum(number):
    '''
    Calculate the sum of the factorials of the digits of number
    '''
    return sum([math.factorial(int(d)) for d in str(number)])


def test_fact_sum():
    '''
    Test fact_sum()
    '''
    assert fact_sum(145) == 145
    assert fact_sum(871) == 45361
    assert fact_sum(45361) == 871


if __name__ == '__main__':
    nr_60chains = 0
    LIMIT = 10**6
    for i in range(1, LIMIT):
        known = {i}
        current = fact_sum(i)
        while current not in known:
            known.add(current)
            current = fact_sum(current)
        if len(known) == 60:
            nr_60chains += 1

    print(nr_60chains)
