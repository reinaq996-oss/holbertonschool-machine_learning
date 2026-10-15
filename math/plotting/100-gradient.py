#!/usr/bin/env python3
"""Module that plots a scatter plot of mountain elevations"""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Plots a scatter plot of sampled elevations on a mountain

    The x-axis is labeled 'x coordinate (m)', the y-axis is labeled
    'y coordinate (m)', the title is 'Mountain Elevation' and a
    colorbar labeled 'elevation (m)' displays the elevation.
    """
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c=z)
    plt.colorbar(label='elevation (m)')
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')
    plt.show()
