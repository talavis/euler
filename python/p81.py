#!/usr/bin/env python3

'''In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

131 673 234 103  18
201  96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524  37 331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down'''

raw = open('p081_matrix.txt').read()
matrix = [[int(i) for i in row.split(',')] for row in raw.split('\n') if len(row) > 0]

# "dynamic programming"
# fix first row/column)
for x in range(1, len(matrix[0])) :
    matrix[0][x] += matrix[0][x-1]
for y in range(1, len(matrix)) :
    matrix[y][0] += matrix[y-1][0]
    
for y in range(1, len(matrix)) :
    for x in range(1, len(matrix[0])) :
        matrix[y][x] += min(matrix[y][x-1], matrix[y-1][x]) 

print(matrix[-1][-1])
