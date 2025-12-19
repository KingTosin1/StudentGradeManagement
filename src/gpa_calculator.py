"""
GPA Calculator Module

This module provides functions to calculate GPA and CGPA based on the Nigerian university grading system.
It uses the standard scale: A=5, B=4, C=3, D=2, E=1, F=0.
"""

import numpy as np
from .grade import Grade

def calculate_semester_gpa(grades, courses):
    """
    Calculates the GPA for a specific semester.

    Args:
        grades (list of Grade): List of Grade objects for the semester.
        courses (list of Course): List of Course objects to get credit units.

    Returns:
        float: GPA for the semester, or 0.0 if no grades or credits.

    Raises:
        ValueError: If grades list is empty or contains invalid data.
    """
    if not grades:
        return 0.0

    total_points = 0
    total_credits = 0

    for grade in grades:
        if not isinstance(grade, Grade):
            raise ValueError("All items in grades must be Grade instances.")
        course = next((c for c in courses if c.code == grade.course_code), None)
        if course:
            points = grade.get_points()
            credits = course.credit_units
            total_points += points * credits
            total_credits += credits

    if total_credits == 0:
        return 0.0

    gpa = total_points / total_credits
    return round(gpa, 2)

def calculate_cgpa(all_grades, courses):
    """
    Calculates the Cumulative GPA (CGPA) across all semesters.

    Args:
        all_grades (list of Grade): List of all Grade objects for the student.
        courses (list of Course): List of Course objects to get credit units.

    Returns:
        float: CGPA, or 0.0 if no grades or credits.

    Raises:
        ValueError: If all_grades list is empty or contains invalid data.
    """
    if not all_grades:
        return 0.0

    total_points = 0
    total_credits = 0

    for grade in all_grades:
        if not isinstance(grade, Grade):
            raise ValueError("All items in all_grades must be Grade instances.")
        course = next((c for c in courses if c.code == grade.course_code), None)
        if course:
            points = grade.get_points()
            credits = course.credit_units
            total_points += points * credits
            total_credits += credits

    if total_credits == 0:
        return 0.0

    cgpa = total_points / total_credits
    return round(cgpa, 2)

def get_grade_distribution(grades):
    """
    Returns the distribution of grades for visualization.

    Args:
        grades (list of Grade): List of Grade objects.

    Returns:
        dict: Dictionary with grade letters as keys and counts as values.
    """
    distribution = {grade: 0 for grade in Grade.VALID_GRADES}
    for grade in grades:
        if isinstance(grade, Grade):
            distribution[grade.grade] += 1
    return distribution

# Note: The credit_units for grades need to be accessible. In practice, this might require joining with course data.
# For now, assuming Grade objects have a credit_units attribute or it's passed separately.
