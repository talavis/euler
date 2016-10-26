#!/usr/bin/env python3

'''
Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 cong. 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 <= a <= 1000, find the sum rmax.
'''


def find_rmax(a):
    n = 1
    div = a**2
    r = 2
    remains = []
    while r not in remains:
        remains.append(r)
        num = (a-1)**n + (a+1)**n
        r = num % div
        # n % 2 ? 0 will always give remainder 2
        n += 2
    return max(remains)


def test_find_rmax():
    assert find_rmax(3) == 6
    assert find_rmax(7) == 42


if __name__ == '__main__':
    total = 0
    for a in range(3, 1001):
        total += find_rmax(a)
        if a % 10 == 0:
            print(a)

    print(total)
