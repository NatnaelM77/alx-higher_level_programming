#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda l: [i * i for i in l], matrix))
