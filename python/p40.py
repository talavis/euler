#!/usr/bin/env python3

'''An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000'''

MAXLEN = 1000000
num = '0.'
i = 1

# d_1 has pos 2.
while len(num) < MAXLEN + 2 :
    num += str(i)
    i += 1

answer = 1
for i in range(7) :
    answer *= int(num[10**i + 1])
print(answer)
