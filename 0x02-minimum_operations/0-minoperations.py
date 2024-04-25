!/usr/bin/python3
''' Minimum Operations'''


def minOperations(n):
    '''calculates the fewest number of operations needed
       to result in exactly n H characters in the file.
    '''
    if n == 1:
        return 0
    sum = 0
    i = 2
    while (n > 1):
        while (n % i != 0):
            i = i + 1
        sum += i
        n /= i
    return sum
