#!/usr/bin/python3

"""
finds a peak in a list
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    num = 0
    if list_of_integers:
        if len(list_of_integers) == 0:
            return list_of_integers[0]
        elif len(list_of_integers) == 2:
            return max(list_of_integers)

        for i in list_of_integers:
            if i > num:
                num = i
        return num
    return None
