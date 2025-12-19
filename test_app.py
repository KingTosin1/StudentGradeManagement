"""
Simple test script to verify application functionality.
"""

from src.storage import load_students, load_courses, load_grades
from src.gpa_calculator import calculate_semester_gpa, calculate_cgpa
from src.student import Student
from src.course import Course
from src.grade import Grade

def test_data_loading():
    """Test loading data from CSV files."""
    students = load_students()
    courses = load_courses()
    grades = load_grades()
    print(f"Loaded {len(students)} students, {len(courses)} courses, {len(grades)} grades.")
    return students, courses, grades

def test_gpa_calculation():
    """Test GPA calculations."""
    students, courses, grades = test_data_loading()

    if students and courses and grades:
        student = students[0]
        student_grades = [g for g in grades if g.student_id == student.student_id]
        if student_grades:
            gpa = calculate_semester_gpa(student_grades, courses)
            cgpa = calculate_cgpa(student_grades, courses)
            print(f"GPA for {student.name}: {gpa}, CGPA: {cgpa}")
        else:
            print("No grades for student.")
    else:
        print("Insufficient data for GPA test.")

def test_validation():
    """Test data validation."""
    try:
        student = Student("", "John", "john@example.com")
        student.validate()
        print("Validation failed: empty ID should raise error.")
    except ValueError:
        print("Student validation works.")

    try:
        course = Course("ICT323", "Intro to ICT", 7, "Sem1")  # Credits >6
        course.validate()
        print("Validation failed: credits >6 should raise error.")
    except ValueError:
        print("Course validation works.")

def test_edge_cases():
    """Test edge cases for GPA calculation."""
    # Test with no grades
    gpa = calculate_semester_gpa([], [])
    print(f"GPA with no grades: {gpa} (should be 0.0)")

    # Test with grades but no matching courses
    grades = [Grade("12345", "ICT323", "A", "Sem1")]
    gpa = calculate_semester_gpa(grades, [])
    print(f"GPA with no courses: {gpa} (should be 0.0)")

    # Test CGPA with no grades
    cgpa = calculate_cgpa([], [])
    print(f"CGPA with no grades: {cgpa} (should be 0.0)")

if __name__ == "__main__":
    test_data_loading()
    test_gpa_calculation()
    test_validation()
    print("Basic tests completed.")
