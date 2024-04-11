#!/usr/bin/python3
'''0-pascal_triangle module'''


def pascal_triangle(n):
    '''returns a list of lists of integers
       representing the Pascal's triangle of n
    '''
    if n <= 0:
        return []
    else:
        pascal = []
        my_list = []
        for i in range(n):
            new_list = []
            for j in range(len(my_list)):
                if j != 0:
                    new_list.append(my_list[j-1] + my_list[j])
                else:
                    if my_list[0]:
                        new_list.append(1)
            new_list.append(1)
            pascal.append(new_list)
            my_list = new_list
        return pascal