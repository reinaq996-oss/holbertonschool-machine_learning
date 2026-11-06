#!/usr/bin/env python3
"""Binomial distribution class."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the distribution from data or given parameters.

        Args:
            data (list): Data used to estimate the distribution.
            n (int): Number of Bernoulli trials.
            p (float): Probability of a success.

        Raises:
            TypeError: If data is not a list.
            ValueError: If n or p is invalid or data has too few values.
        """
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = sum(data) / len(data)
            variance = sum((value - mean) ** 2 for value in data) / len(data)
            p = 1 - variance / mean
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Return the probability of exactly k successes."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0

        combinations = 1
        for value in range(1, min(k, self.n - k) + 1):
            combinations = combinations * (self.n - value + 1) // value
        return combinations * self.p ** k * (1 - self.p) ** (self.n - k)

    def cdf(self, k):
        """Return the cumulative probability for k successes in range."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        return sum(self.pmf(value) for value in range(k + 1))
