#!/usr/bin/env python3
"""Plot a histogram of student grades."""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot student grades with bins of 10 units."""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    plt.hist(
        student_grades,
        bins=np.arange(0, 101, 10),
        edgecolor='k'
    )
    plt.xticks(np.arange(0, 101, 10))
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")
    plt.show()


if __name__ == "__main__":
    frequency()
