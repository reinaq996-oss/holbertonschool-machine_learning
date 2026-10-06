#!/usr/bin/env python3
"""Write a function that adds two arrays element-wise:"""


def add_arrays(arr1, arr2):
    """The function that adds 2 arrays element-wise"""
    if len(arr1) != len(arr2):
        return None

    return [arr1[i]+arr2[i] for i in range(len(arr1))]
