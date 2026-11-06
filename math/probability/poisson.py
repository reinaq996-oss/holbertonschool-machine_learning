#!/usr/bin/env python3
"""Poisson distribution class."""


class Poisson:
    """Represents a Poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the distribution from data or an expected rate.

        Args:
            data (list): Data used to estimate the distribution.
            lambtha (float): Expected number of occurrences in a time frame.

        Raises:
            TypeError: If data is not a list.
            ValueError: If lambtha is not positive or data has too few values.
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
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Return the probability of exactly k successes."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        factorial = 1
        for value in range(1, k + 1):
            factorial *= value
        e = 2.7182818285
        return (self.lambtha ** k * e ** (-self.lambtha)) / factorial

    def cdf(self, k):
        """Return the probability of at most k successes."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(value) for value in range(k + 1))
