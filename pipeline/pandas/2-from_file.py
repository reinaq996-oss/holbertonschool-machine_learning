
#!/usr/bin/env python3
"""Load data from a file into a pandas DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """Load a DataFrame from a file using the given delimiter."""
    return pd.read_csv(filename, delimiter=delimiter)
