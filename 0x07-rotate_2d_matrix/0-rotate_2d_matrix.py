#!/usr/bin/python3
"""rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    '''
      Rotate 2 Dimensional Matrix in 90 degrees
      Return:
          - Nothing
     '''
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reverse each row from the transposed matrix
    for row in matrix:
        row.reverse()
