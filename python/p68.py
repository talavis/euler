#!/usr/bin/env python3

'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
'''

import itertools


def test(nums):
    '''
    Testing whether the permutation is a magic pentagon ring
    '''
    goal = nums[0] + nums[1] + nums[2]
    if goal != nums[3] + nums[2] + nums[4]:
        return False
    if goal != nums[5] + nums[4] + nums[6]:
        return False
    if goal != nums[7] + nums[6] + nums[8]:
        return False
    if goal != nums[9] + nums[8] + nums[1]:
        return False
    return True


best = 0
best_nums = list()
for nums in itertools.permutations(list(range(1,11))):
    if test(nums):
        # put the permutation in the right number order
        numstr = [str(nums[0]) + str(nums[1]) + str(nums[2]),
                  str(nums[3]) + str(nums[2]) + str(nums[4]),
                  str(nums[5]) + str(nums[4]) + str(nums[6]),
                  str(nums[7]) + str(nums[6]) + str(nums[8]),
                  str(nums[9]) + str(nums[8]) + str(nums[1])]
        s_numstr = [0,0,0,0,0]
        extnodes = [nums[0], nums[3], nums[5], nums[7], nums[9]]
        s_extnodes = sorted(extnodes)
        i = extnodes.index(s_extnodes[0])
        for j in range(len(numstr)):
            s_numstr[j] = numstr[i]
            i += 1
            if i == 5:
                i = 0

        tmpstr = ''.join(s_numstr)
        if len(tmpstr) == 16:
            tmpint = int(tmpstr)
            if tmpint > best:
                best = tmpint
print(best)
