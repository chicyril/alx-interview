#!/usr/bin/python3
"""
This module contains a function that rotates a 2D matrix by 90 degrees
in a clockwise direction
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a n by n 2D matrix in place.
    """
    i = 0
    for v in list(zip(*matrix)):
        matrix[i][:] = v[::-1]
        i += 1
