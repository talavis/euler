#!/usr/bin/env python3

'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

end89 = 0
known1 = {1}
known89 = {89}
for i in range(2,10**7):
    tmp = i
    known = False
    while tmp not in (1,89):
        tmp2 = sum([int(d)**2 for d in list(str(tmp))])
        if tmp2 in known89:
            known89.add(tmp)
            break
        elif tmp2 in known1:
            known1.add(tmp)
            break

        tmp = tmp2

    if tmp in known89:
        end89 += 1
        known89.add(i)

    else:
        known1.add(i)
        
print(end89)
