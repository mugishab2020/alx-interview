#!usr/bin/env python3
'''implementation of 2d matrix '''


def rotate_2d_matrix(matrix):

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for a in range(n):
        matrix[a].reverse()
