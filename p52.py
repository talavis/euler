#!/usr/bin/env python3

'''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''

counter = 1

while True :
    digits = list(str(counter))
    digits.sort()
    equal = True
    for i in range(2,7) :
        digits_x = list(str(counter * i))
        digits_x.sort()
        if digits != digits_x :
            equal = False
            break
    if equal :
        print(counter)
        break
    counter += 1
