#!/usr/bin/env python3

'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

cubes = [0]*10000

for i in range(1, 10000):
    cubes[i] = i**3

cube_digits = [sorted(tuple((str(c)))) for c in cubes]

for i in range(len(cube_digits)):
    if cube_digits.count(cube_digits[i]) == 5:
        print(cubes[i])
        break
