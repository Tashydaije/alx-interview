#!/usr/bin/python3
"""island perimeter module"""


def island_perimeter(grid):
    """returns perimeter of the island described in grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # check top
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # check bottom
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # check right
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
