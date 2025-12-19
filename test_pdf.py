"""
Test PDF generation.
"""

from src.student import Student
from src.grade import Grade
from src.course import Course
from src.pdf_report import generate_student_report

# Sample data
student = Student("12345", "John Doe", "john@example.com")
grades = [
    Grade("12345", "ICT323", "A", "2023/2024 Semester 1"),
    Grade("12345", "CSC101", "B", "2023/2024 Semester 1")
]
courses = [
    Course("ICT323", "Intro to ICT", 3, "2023/2024 Semester 1"),
    Course("CSC101", "Computer Science", 3, "2023/2024 Semester 1")
]

generate_student_report(student, grades, courses, "test_report.pdf")
print("PDF test completed.")
