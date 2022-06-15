#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda l: list(map(lambda i: i * i, l)), matrix))
