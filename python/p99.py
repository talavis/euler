#!/usr/bin/env python3

'''
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.
'''

import math


def calc(num, exponent):
    # log_a(num^exponent) = exponent * log_a(num)
    log_num = math.log(num)
    value = exponent * log_num
    return [value, num, exponent]


def compare(num, exponent, curr_best):
    curr = calc(num, exponent)
    if curr[0] > curr_best[0]:
        return curr
    else:
        return curr_best


def get_data():
    import requests

    req = requests.get('https://projecteuler.net/project/resources/p099_base_exp.txt')
    return req.text


def test_compare():
    first = calc(632382, 518061)
    second = calc(519432, 525806)

    assert compare(519432, 525806, first) == first
    assert compare(632382, 518061, second) == first


if __name__ == '__main__':
    raw = get_data()
    best = [0, 0, 0]
    best_i = 0
    i = 1
    for line in raw.split('\n'):
        number, expo = [int(i) for i in line.split(',')]
        best_tmp = best
        best = compare(number, expo, best)
        if best_tmp != best:
            best_i = i
        i += 1
    print(best_i)
