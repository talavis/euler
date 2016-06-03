#!/usr/bin/env python3

'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?'''

if __name__ == '__main__' :
    # initialize grid
    grid = list()
    for i in range(20) :
        grid.append([0]*20)



    for i in range(20) :
        grid[0][i] = i + 2
        grid[i][0] = i + 2

    for y in range(1,20) :
        for x in range(1,20) :
            grid[y][x] = grid[y-1][x] + grid[y][x-1]

    print(grid[-1][-1])
        
