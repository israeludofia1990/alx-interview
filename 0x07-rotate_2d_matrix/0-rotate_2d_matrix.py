#!/usr/bin/python3
'''in-place rotation of a 2D matrix'''


def rotate_2d_matrix(matrix):
    '''In-Place matrix rotation'''
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix[i].reverse()
