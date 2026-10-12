#!/usr/bin/env python3
"""Module that sets the Timestamp column as the index of a DataFrame."""


def index(df):
    """Set the Timestamp column as the index of the DataFrame.

    Args:
        df: pd.DataFrame containing a Timestamp column.

    Returns:
        The modified pd.DataFrame indexed on Timestamp.
    """
    return df.set_index('Timestamp')
