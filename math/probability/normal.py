#!/usr/bin/env python3
"""Normal distribution class."""


class Normal:
    """Represents a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize the distribution from data or given parameters.

        Args:
            data (list): Data used to estimate the distribution.
            mean (float): Mean of the distribution.
            stddev (float): Standard deviation of the distribution.

        Raises:
            TypeError: If data is not a list.
            ValueError: If stddev is not positive or data has too few values.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = float(sum(data) / len(data))
            variance = sum((value - self.mean) ** 2 for value in data)
            self.stddev = float((variance / len(data)) ** 0.5)

    def z_score(self, x):
        """Return the z-score corresponding to the x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Return the x-value corresponding to the z-score."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Return the probability density for the x-value."""
        e = 2.7182818285
        pi = 3.1415926536
        z = self.z_score(x)
        return e ** (-0.5 * z ** 2) / (self.stddev * (2 * pi) ** 0.5)

    def cdf(self, x):
        """Approximate the cumulative probability for the x-value."""
        pi = 3.1415926536
        z = self.z_score(x) / (2 ** 0.5)
        erf = (2 / (pi ** 0.5)) * (
            z - z ** 3 / 3 + z ** 5 / 10
            - z ** 7 / 42 + z ** 9 / 216
        )
        return (1 + erf) / 2
