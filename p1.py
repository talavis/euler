#!/usr/bin/env python3

total = 0
for i in range(3,1000, 3) :
    total += i

for i in range(5,1000, 5) :
    if i % 3 != 0 :
        total += i

print(total)
