#!usr/bin/env python3
'''implementation of 2d matrix '''


def rotate_2d_matrix(matrix):
    """
      Rotate The 2 matrix
      Args:
          - matrix: list of two dimension array
      Return:
          - Nothing
    """
    # Get the number of rows and colu

    n = len(matrix)
    # 1. Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):  # Avoid redundant swaps (i == j)
            # Swap elements
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 2. Reverse each row finally
    for a in range(n):
        matrix[a].reverse()
