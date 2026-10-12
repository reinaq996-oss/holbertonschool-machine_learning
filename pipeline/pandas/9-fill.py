#!/usr/bin/env python3
"""Module that fills the missing values of a DataFrame."""


def fill(df):
    """Clean the DataFrame and fill its missing values.

    Removes Weighted_Price, forward fills Close, fills High, Low and Open
    with the Close of the same row and sets missing volumes to 0.

    Args:
        df: pd.DataFrame with the coinbase/bitstamp columns.

    Returns:
        The modified pd.DataFrame.
    """
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()
    for column in ['High', 'Low', 'Open']:
        df[column] = df[column].fillna(df['Close'])
    for column in ['Volume_(BTC)', 'Volume_(Currency)']:
        df[column] = df[column].fillna(0)
    return df
