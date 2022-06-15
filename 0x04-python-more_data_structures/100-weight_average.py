#!/usr/bin/python3


def weight_average(my_list=[]):
    score = weight = 0
    if not my_list:
        return (0)
    for t in my_list:
        score += t[0] * t[1]
        weight += t[1]
    return (score / weight)
