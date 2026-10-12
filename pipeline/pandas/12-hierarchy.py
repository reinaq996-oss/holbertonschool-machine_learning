#!/usr/bin/env python3
"""Module that builds a hierarchical index from two DataFrames."""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate bitstamp and coinbase with Timestamp as first level.

    Only the timestamps from 1417411980 to 1417417980 (inclusive) are kept
    and the result is displayed in chronological order.

    Args:
        df1: pd.DataFrame with the coinbase data.
        df2: pd.DataFrame with the bitstamp data.

    Returns:
        The concatenated pd.DataFrame.
    """
    df1 = index(df1)
    df2 = index(df2)
    df1 = df1[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
    df2 = df2[(df2.index >= 1417411980) & (df2.index <= 1417417980)]
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    df = df.swaplevel(0, 1)
    return df.sort_index(level=0)
