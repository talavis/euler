#!/usr/bin/env python3

'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

# p, value
best = (0, 0)

for p in range(1, 1001):
    solutions = list()
    # the sum of the two sides is never less than the hypotenuse
    for h in range((p)//2, p//3, -1):
        for s1 in range(1, (p-h-1)//2):
            s2 = p-h-s1
            if s1**2 + s2**2 == h**2:
                solutions.append((s1, s2, h))
    if len(solutions) > best[1]:
        best = (p, len(solutions))

print(best[0])
