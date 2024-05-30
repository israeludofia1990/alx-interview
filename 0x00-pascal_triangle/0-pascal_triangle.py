#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's Triangle of n
    returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for tri_row in range(1, n):
        prev_row = triangle[tri_row - 1]
        new_row = [1]
        
        for tri_col in range(1, len(prev_row)):
            new_row.append(prev_row[tri_col] + prev_row[tri_col - 1])
        
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle
