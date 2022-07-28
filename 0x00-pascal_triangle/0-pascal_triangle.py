#!/usr/bin/python3
"""
Defines a function pascal
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers of integers representing
    the Pascal's triangle of n
    """
    res = []
    if n == 0:
        return res
    res = [[1]]
    for rows in range(n - 1):
        row_above = [0] + res[rows] + [0]
        row = []
        for nums in range(len(row_above) - 1):
            addRes = row_above[nums] + row_above[nums + 1]
            row.append(addRes)
        res.append(row)
    return res
