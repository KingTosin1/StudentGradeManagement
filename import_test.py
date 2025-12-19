"""
Import test script to check for module errors.
"""

try:
    from src.student import Student
    print("Student module OK")
except Exception as e:
    print(f"Student module error: {e}")

try:
    from src.course import Course
    print("Course module OK")
except Exception as e:
    print(f"Course module error: {e}")

try:
    from src.grade import Grade
    print("Grade module OK")
except Exception as e:
    print(f"Grade module error: {e}")

try:
    from src.gpa_calculator import calculate_semester_gpa, calculate_cgpa
    print("GPA Calculator module OK")
except Exception as e:
    print(f"GPA Calculator module error: {e}")

try:
    from src.storage import load_students, load_courses, load_grades
    print("Storage module OK")
except Exception as e:
    print(f"Storage module error: {e}")

try:
    from src.charts import plot_gpa_trend, plot_grade_distribution
    print("Charts module OK")
except Exception as e:
    print(f"Charts module error: {e}")

try:
    from src.pdf_report import generate_student_report
    print("PDF Report module OK")
except Exception as e:
    print(f"PDF Report module error: {e}")

try:
    import tkinter as tk
    print("Tkinter OK")
except Exception as e:
    print(f"Tkinter error: {e}")

try:
    import pandas as pd
    print("Pandas OK")
except Exception as e:
    print(f"Pandas error: {e}")

try:
    import matplotlib.pyplot as plt
    print("Matplotlib OK")
except Exception as e:
    print(f"Matplotlib error: {e}")

try:
    from reportlab.pdfgen import canvas
    print("ReportLab OK")
except Exception as e:
    print(f"ReportLab error: {e}")

print("Import tests completed.")
