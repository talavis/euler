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

def gen_sumways(num):
    '''
    Generate a list of the ways num can be written as a sum of
    positive digits.
    Generates all permutations
    '''
    ways = list()
    if num == 0:
        return [[]]
    if num == 1:
        return [[1]]
    for i in range(num, 0, -1):
        ways += [[i] + comb for comb in gen_sumways(num-i)]

    return ways


def test_gen_sumways():
    '''
    Test count_sumways()
    '''
    expected = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 3], [2, 2, 1],
                [2, 1, 2], [2, 1, 1, 1], [1, 4], [1, 3, 1],
                [1, 2, 2], [1, 2, 1, 1], [1, 1, 3], [1, 1, 2, 1],
                [1, 1, 1, 2], [1, 1, 1, 1, 1]]
    assert gen_sumways(5) == expected


def evaluate(ways):
    '''
    Only keep a single copy of each combination
    Remove the single-number combination
    '''
    ways = [way for way in ways if len(way) > 1]
    return len(set(tuple(sorted(way)) for way in ways))


def test_evaluate():
    '''
    Test evaluate()
    '''
    assert evaluate(gen_sumways(5)) == 6


print(evaluate(gen_sumways(100)))
