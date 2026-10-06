#!/usr/bin/env python3
"""This script contains a funcion which returns the shape of a matrix"""


def matrix_shape(matrix):
    """Returns the shape of the patrix"""
    return calculate_dimension(matrix, [])


def calculate_dimension(matrix, shape=[]):
    """The recursive function which calculates the shape of the matrix"""
    # base case - matrix is not a list
    if not isinstance(matrix, list):
        return shape

    # add length of current reduced list
    shape.append(len(matrix))

    # call recursively with the first element of the list
    return calculate_dimension(matrix[0], shape)