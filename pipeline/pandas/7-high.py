#!/usr/bin/env python3
"""Module that sorts a DataFrame by the High price."""


def high(df):
    """Sort the DataFrame by the High price in descending order.

    Args:
        df: pd.DataFrame containing a High column.

    Returns:
        The sorted pd.DataFrame.
    """
    return df.sort_values('High', ascending=False)
