#!/usr/bin/env python3
"""Exponential distribution class."""


class Exponential:
    """Represents an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the exponential distribution.

        Args:
            data (list): Data used to estimate the distribution.
            lambtha (float): Expected number of occurrences in a
                given time frame.

        Raises:
            ValueError: If lambtha is not positive, or if data has
                fewer than two values.
            TypeError: If data is not a list.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(len(data) / sum(data))
