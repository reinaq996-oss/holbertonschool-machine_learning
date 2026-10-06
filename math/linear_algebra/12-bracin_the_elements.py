#!/usr/bin/env python3
"""Perform element-wise operations on matrices."""


def np_elementwise(mat1, mat2):
    """Return the sum, difference, product, and quotient of two matrices."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
