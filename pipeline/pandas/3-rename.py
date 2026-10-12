
#!/usr/bin/env python3
"""Rename Timestamp and convert it to datetime."""

import pandas as pd


def rename(df):
    """Rename Timestamp, convert values, and keep two columns."""
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    return df[['Datetime', 'Close']]

