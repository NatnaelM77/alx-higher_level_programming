#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    sum = ((tuple_a[0] if len(tuple_a) >= 1 else 0) + (
        tuple_b[0] if len(tuple_b) >= 1
        else 0), (tuple_a[1] if
                  len(tuple_a) >= 2 else 0) +
           (tuple_b[1] if len(tuple_b) >= 2 else 0))
    return sum
