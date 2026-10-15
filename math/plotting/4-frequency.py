#!/usr/bin/env python3
"""Module that plots a histogram of student grades"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plots a histogram of student scores for a project

    The x-axis is labeled 'Grades' with bins every 10 units,
    the y-axis is labeled 'Number of Students', the title is
    'Project A' and the bars are outlined in black.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.xticks(range(0, 101, 10))
    plt.show()
