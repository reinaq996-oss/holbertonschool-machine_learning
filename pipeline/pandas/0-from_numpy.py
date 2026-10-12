
# !/usr/bin/env python3
"""Create a pandas DataFrame from a NumPy array."""

import pandas as pd


def from_numpy(array):
    """Create a DataFrame with alphabetical, capitalized column names."""
    columns = [chr(i) for i in range(ord('A'), ord('A') + array.shape[1])]
    return pd.DataFrame(array, columns=columns)
