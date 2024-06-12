#!/usr/bin/python3
'''function to generate the island parameters'''


def island_perimeter(grid):
    '''
    Island Perimeter
    '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                    perimeter -= 1
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    perimeter -= 1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
    return perimeter
