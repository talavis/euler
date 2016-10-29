#!/usr/bin/env python3

palis = list()

pali_sum = 0
found = 0

i = 2
while found < 5:
    # tuned after testing
    for j in range(2,800):
        numstr = str(i**2 + j**3)
        if numstr == numstr[::-1]:
            num.append(int(numstr))
            if num.count(int(numstr)) == 4:
                found += 1
                pali_sum += int(numstr)
            elif num.count(int(numstr)) == 5:
                found -= 1
                pali_sum -= int(numstr)
    i += 1
    
print(pali_sum)
