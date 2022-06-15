#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    keys = []
    if a_dictionary:
        for i in a_dictionary.items():
            if value == i[1]:
                keys.append(i[0])
        for i in keys:
            a_dictionary.pop(i)
        return a_dictionary
    else:
        return {}
