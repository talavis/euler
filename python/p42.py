#!/usr/bin/env python3

'''The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?'''

trinum = list()
for i in range(1,100) : # covers way more than needed but cheap calculation
    trinum.append(int(0.5*i*(i+1)))

trinum = set(trinum)
    
BASE = 64 # start of capital letters in ascii
triwords = 0
for word in open('p042_words.txt').read().replace('"', '').split(',') :
    charsum = 0
    for c in word :
        charsum += ord(c) - BASE
    if charsum in trinum :
        triwords += 1

print(triwords)
