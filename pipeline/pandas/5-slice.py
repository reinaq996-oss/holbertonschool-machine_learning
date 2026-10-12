#!/usr/bin/env python3
"""Module that slices a DataFrame by columns and by every 60th row."""


def slice(df):
    """Extract selected columns and keep every 60th row.

    Args:
        df: pd.DataFrame containing the columns High, Low, Close and
            Volume_(BTC).

    Returns:
        The sliced pd.DataFrame.
    """
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
