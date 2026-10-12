#!/usr/bin/env python3
"""Module that renames the Timestamp column of a DataFrame."""
import pandas as pd


def rename(df):
    """Rename Timestamp to Datetime and keep only Datetime and Close.

    Args:
        df: pd.DataFrame containing a column named Timestamp.

    Returns:
        The modified pd.DataFrame with the Datetime and Close columns,
        where Datetime holds datetime values.
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    return df[['Datetime', 'Close']]
