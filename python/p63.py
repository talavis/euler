#!/usr/bin/env python3

'''
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

matches = 0
# i = 10 will always be to many digits, 9 will have too few digits from 9**22
for n in range(1,22):
    i = 1
    while len(str(i**n)) <= n:
        if len(str(i**n)) == n:
            matches += 1
        i += 1

print(matches)
