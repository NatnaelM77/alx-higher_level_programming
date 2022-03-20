#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    index = 0
    result = []
    try:
        for index in range(list_length):
            try:
                result.append(my_list_1[index] / my_list_2[index])
            except IndexError:
                print('out of range')
                result.append(0)
                continue
            except (TypeError, ValueError):
                print('wrong type')
                result.append(0)
                continue
            except ZeroDivisionError:
                print('division by 0')
                result.append(0)
                continue
    finally:
        return result
