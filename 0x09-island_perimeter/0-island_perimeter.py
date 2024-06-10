#!/usr/bin/env python3
'''function to generate the island parameters'''


def island_perimeter(grid):
    params = 0

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                params += 4
                # Check the cell above
                if i > 0 and grid[i][j] == grid[i-1][j]:
                    params -= 2
                # Check the cell to the left
                if j > 0 and grid[i][j] == grid[i][j-1]:
                    params -= 2
    return params
