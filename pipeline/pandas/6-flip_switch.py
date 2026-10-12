#!/usr/bin/env python3
"""Module that sorts a DataFrame in reverse chronological order and
transposes it."""


def flip_switch(df):
    """Sort the data in reverse chronological order and transpose it.

    Args:
        df: pd.DataFrame containing a Timestamp column.

    Returns:
        The transformed (sorted and transposed) pd.DataFrame.
    """
    return df.sort_values('Timestamp', ascending=False).T
