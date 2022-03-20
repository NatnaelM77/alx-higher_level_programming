#!/usr/bin/python3
"""Method for pascal_triangle function."""


def pascal_triangle(n):
    """The Pascal Triangle function."""
    if n <= 0:
        return []

    elif n == 1:
        return [[1]]

    container = [[1]]

    while len(container) != n:
        last = container[-1]
        extreme = [1]

        for num in range(len(last) - 1):
            extreme.append(last[num] + last[num + 1])

        extreme += [1]
        container.append(extreme)
    return container
