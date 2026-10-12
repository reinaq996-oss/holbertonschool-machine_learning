#!/usr/bin/env python3
"""Module that computes descriptive statistics of a DataFrame."""


def analyze(df):
    """Compute descriptive statistics for all columns except Timestamp.

    Args:
        df: pd.DataFrame containing a Timestamp column.

    Returns:
        A new pd.DataFrame containing the statistics.
    """
    return df.drop(columns=['Timestamp']).describe()
