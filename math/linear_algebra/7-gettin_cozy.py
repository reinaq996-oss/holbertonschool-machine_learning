#!/usr/bin/env python3
"""Concatenate two 2D matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two matrices along the specified axis."""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]

    return None
