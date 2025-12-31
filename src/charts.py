"""
Charts Module

This module provides functions to generate charts for GPA trends and grade distributions
using matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from .gpa_calculator import calculate_semester_gpa, get_grade_distribution

def plot_gpa_trend(student_grades, student_name, courses):
    """
    Plots a line chart of GPA trend over semesters.

    Args:
        student_grades (list of Grade): List of Grade objects for the student.
        student_name (str): Name of the student for the title.
        courses (list of Course): List of Course objects for credit units.
    """
    if not student_grades:
        plt.figure(figsize=(8, 6))
        plt.text(0.5, 0.5, "No grades available", ha='center', va='center', fontsize=14)
        plt.title(f"GPA Trend for {student_name}")
        plt.show()
        return

    # Group grades by semester
    semesters = {}
    for grade in student_grades:
        sem = grade.semester
        if sem not in semesters:
            semesters[sem] = []
        semesters[sem].append(grade)

    # Calculate GPA per semester
    sem_list = sorted(semesters.keys())
    gpas = [calculate_semester_gpa(semesters[sem], courses) for sem in sem_list]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(sem_list, gpas, marker='o', linestyle='-', color='b')
    plt.title(f"GPA Trend for {student_name}")
    plt.xlabel("Semester")
    plt.ylabel("GPA")
    plt.ylim(0, 5)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_grade_distribution(grades, student_name):
    """
    Plots a bar chart of grade distribution.

    Args:
        grades (list of Grade): List of Grade objects.
        student_name (str): Name of the student for the title.
    """
    if not grades:
        plt.figure(figsize=(8, 6))
        plt.text(0.5, 0.5, "No grades available", ha='center', va='center', fontsize=14)
        plt.title(f"Grade Distribution for {student_name}")
        plt.show()
        return

    distribution = get_grade_distribution(grades)
    grades_list = list(distribution.keys())
    counts = list(distribution.values())

    # Plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x=grades_list, y=counts, hue=grades_list, palette="viridis", legend=False)
    plt.title(f"Grade Distribution for {student_name}")
    plt.xlabel("Grade")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def save_chart(filename):
    """
    Saves the current matplotlib figure to a file.

    Args:
        filename (str): Path to save the image.
    """
    plt.savefig(filename)
    print(f"Chart saved to {filename}")
