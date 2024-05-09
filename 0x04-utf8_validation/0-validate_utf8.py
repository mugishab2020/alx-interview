#!/usr/bin/env python3
'''Makking the verification of the given data list of integers
and change them in decimal one by one and check the UTF-rule to
check the varidation of the UTF-8 encoding'''
from typing import List


def valid_utf8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing the data set
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    if not isinstance(data, list) or \
            not all(isinstance(num, int) for num in data):
        return False

    binary_list = [format(decimal_number % 256, '08b')
                   for decimal_number in data]
    i = 0
    while i < len(binary_list):
        byte = binary_list[i]
        if byte.startswith('0'):
            i += 1
        elif byte.startswith('110'):
            if len(binary_list) < i + 2:
                return False
            if not binary_list[i + 1].startswith('10'):
                return False
            i += 2
        elif byte.startswith('1110'):
            if len(binary_list) < i + 3:
                return False
            for j in range(i + 1, i + 3):
                if not binary_list[j].startswith('10'):
                    return False
            i += 3
        elif byte.startswith('11110'):
            if len(binary_list) < i + 4:
                return False
            for j in range(i + 1, i + 4):
                if not binary_list[j].startswith('10'):
                    return False
            i += 4
        else:
            return False
    return True
