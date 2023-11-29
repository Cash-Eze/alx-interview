#!/usr/bin/python3
"""Writng a function Pascal Triangle"""


def pascal_triangle(n):
    """
        Printing the Triangle
    """
    trow = []
    x = [0]
    if n <= 0:
        return []
    else:
        for i in range(n):
            print(trow)
            trow = [left+right, for left, right in zip(trow + x, x + trow)]
