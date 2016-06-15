#!/usr/bin/env python3

'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?'''

import sys

try :
    infile = open('p022_names.txt')
except :
    sys.stderr.write('Get the data file at {}\n'.format('https://projecteuler.net/project/resources/p022_names.txt'))
    sys.exit(1)

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
data = sorted(infile.read().replace('"', '').split(','))

for i in range(len(data)) :
    alphasum = 0
    for c in data[i] :
        alphasum += ALPHA.index(c)+1
    alphasum *= i+1
    total += alphasum

print(total)
