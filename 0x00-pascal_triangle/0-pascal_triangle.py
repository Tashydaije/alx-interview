#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Creats Pascal's triangle upto the `n`th level

        Args:
            n (number): The number of levels to show
        Returns:
            A list of lists of integers representing Pascal's triangle
            [] otherwise
    """
    if n <= 0:
        return []

    """Initialize first row with 1"""
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            """add elements from the previous row"""
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
