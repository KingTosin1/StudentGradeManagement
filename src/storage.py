"""
Storage Module

This module handles data persistence using CSV files for students, courses, and grades.
"""

import csv
import os
from .student import Student
from .course import Course
from .grade import Grade

DATA_DIR = "data"

def ensure_data_dir():
    """Ensures the data directory exists."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_students():
    """Loads students from CSV file."""
    students = []
    filepath = os.path.join(DATA_DIR, "students.csv")
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(Student.from_dict(row))
    return students

def save_students(students):
    """Saves students to CSV file."""
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, "students.csv")
    with open(filepath, 'w', newline='') as f:
        if students:
            writer = csv.DictWriter(f, fieldnames=students[0].to_dict().keys())
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())

def load_courses():
    """Loads courses from CSV file."""
    courses = []
    filepath = os.path.join(DATA_DIR, "courses.csv")
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                courses.append(Course.from_dict(row))
    return courses

def save_courses(courses):
    """Saves courses to CSV file."""
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, "courses.csv")
    with open(filepath, 'w', newline='') as f:
        if courses:
            writer = csv.DictWriter(f, fieldnames=courses[0].to_dict().keys())
            writer.writeheader()
            for course in courses:
                writer.writerow(course.to_dict())

def load_grades():
    """Loads grades from CSV file."""
    grades = []
    filepath = os.path.join(DATA_DIR, "grades.csv")
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                grades.append(Grade.from_dict(row))
    return grades

def save_grades(grades):
    """Saves grades to CSV file."""
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, "grades.csv")
    with open(filepath, 'w', newline='') as f:
        if grades:
            writer = csv.DictWriter(f, fieldnames=grades[0].to_dict().keys())
            writer.writeheader()
            for grade in grades:
                writer.writerow(grade.to_dict())
