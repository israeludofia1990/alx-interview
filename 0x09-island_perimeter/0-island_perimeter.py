#!/usr/bin/python3
'''Island Perimeter'''


def island_perimeter(grid):
    '''Returns perimeter of an island description in grid'''
    if not grid or not grid[0]:
        return 0
    row_len = len(grid)
    col_len = len(grid[0])
    perimeter = 0

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                perimeter += 4
                if i < row_len - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2
                if j < col_len - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2
    return perimeter
