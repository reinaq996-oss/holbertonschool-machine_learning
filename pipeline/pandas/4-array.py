#!/usr/bin/env python3
"""Module that converts the last rows of a DataFrame to a numpy array."""


def array(df):
    """Select the last 10 High and Close rows and convert them to ndarray.

    Args:
        df: pd.DataFrame containing the columns High and Close.

    Returns:
        A numpy.ndarray with the last 10 rows of High and Close.
    """
    return df[['High', 'Close']].tail(10).to_numpy()
