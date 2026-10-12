#!/usr/bin/env python3
"""Module that removes rows with missing Close values from a DataFrame."""


def prune(df):
    """Remove the entries where Close has NaN values.

    Args:
        df: pd.DataFrame containing a Close column.

    Returns:
        The modified pd.DataFrame without NaN values in Close.
    """
    return df.dropna(subset=['Close'])
