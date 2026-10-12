#!/usr/bin/env python3
"""Module that concatenates the bitstamp and coinbase DataFrames."""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Concatenate bitstamp rows (up to 1417411920) on top of coinbase.

    Args:
        df1: pd.DataFrame with the coinbase data.
        df2: pd.DataFrame with the bitstamp data.

    Returns:
        The concatenated pd.DataFrame, keyed by bitstamp and coinbase.
    """
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2[df2.index <= 1417411920]
    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
