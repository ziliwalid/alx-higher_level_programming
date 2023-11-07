#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """does magic :)
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        temp = [1]
        for i in range(len(t) - 1):
            temp.append(t[i] + t[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
