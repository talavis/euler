#!/usr/bin/env python3

'''
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''

# have to test from 1010101010 to 1389026623
# 0 at end -> only test every ten
# digit [-3] == 9 -> only numbers ending with 30 and 70 are worth testing

for i in range(1010101030, 1389026623, 20):
    if i % 100 not in (30, 70):
        continue
    square = str(i**2)
    matches = True
    for j in range(0,9):
        if square[j*2] != str(j+1):
            matches = False
    if matches:
        print(i)

