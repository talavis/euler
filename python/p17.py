#!/usr/bin/env python3

'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''

digits = [[0, 3, 3, 5, 4,
          4, 3, 5, 5, 4],
          [0, 3, 6, 6, 5,
           5, 5, 7, 6, 6],
          [0, 10, 10, 12, 11,
           11, 10, 12, 12, 11]]

TENS = [0, 6, 6, 8, 8,
        7, 7, 9, 8, 8] # eleven...
    
total = 0
for i in range(1, 1000) :
    num = str(i)
    current = 0
    for d in range(1, len(num)+1) :
        if d in [1,2] and 10 < int(num[-2:]) < 20 :
            if d == 2 :
                current += TENS[int(num[-1])] # 11-19
        else :
            current += digits[d-1][int(num[-d])]
        if d == 3 and int(num) % 100 != 0 :
            current += 3 # and
    total += current
        
total += 11 # one thousand

print(total)
