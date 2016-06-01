#!/usr/bin/env python3

'''Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.'''

def check_bouncy(number) :
    number = str(number)
    inc = False
    dec = False
    for d in range(len(number)-1) :
        if number[d] > number[d+1] :
            dec = True
        if number[d] < number[d+1] :
            inc = True
    if inc and dec :
        return True
    return False

bouncy = 0
total = 100  # first bouncy number is 101

while bouncy / total < 0.99 :
    total += 1
    if check_bouncy(total) :
        bouncy += 1

print(total)
