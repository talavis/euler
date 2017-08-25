#!/usr/bin/env python3
'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at
least two positive integers?
'''


def calc_ways(num):
    '''
    Calculate the number of ways to write num as a sum of at least
    two positive integers
    '''
    ways = [0]*(num+1)
    ways[0] = 1

    for i in range(1, num):
        for j in range(i, num+1):
            ways[j] += ways[j - i]

    return ways[-1]


def test_calc_ways():
    '''
    Test calc_ways()
    '''
    assert calc_ways(5) == 6
    assert calc_ways(2) == 1
    assert calc_ways(6) == 10


if __name__ == '__main__':
    print(calc_ways(100))
