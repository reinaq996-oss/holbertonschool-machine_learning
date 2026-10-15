#!/usr/bin/env python3
"""Create a scatter plot of men's height versus weight."""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """Plot height and weight as magenta points."""
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))
    plt.scatter(x, y, color='m')
    plt.xlabel("Height (in)")
    plt.ylabel("Weight (lbs)")
    plt.title("Men's Height vs Weight")
    plt.show()
