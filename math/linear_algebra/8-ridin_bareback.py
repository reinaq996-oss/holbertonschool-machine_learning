#!/usr/bin/env python3
"""Matrix multiplication."""


def mat_mul(mat1, mat2):
    """Multiply two matrices."""
    if len(mat1[0]) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            total = 0
            for k in range(len(mat2)):
                total += mat1[i][k] * mat2[k][j]
            row.append(total)
        result.append(row)

    return result
