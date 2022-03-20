#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    length = 0
    new_list = my_list[0:x]
    for i in new_list:
        try:
            print(i, end='')
            length += 1
        except IndexError:
            break
    print()
    return length
