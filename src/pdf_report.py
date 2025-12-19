"""
PDF Report Module

This module generates PDF reports for student grades using ReportLab.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from .gpa_calculator import calculate_semester_gpa, calculate_cgpa

def generate_student_report(student, grades, courses, filename):
    """
    Generates a PDF report for a student.

    Args:
        student (Student): Student object.
        grades (list): List of Grade objects for the student.
        courses (list): List of Course objects.
        filename (str): Output filename.
    """
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle(name='Title', fontSize=18, alignment=1, spaceAfter=20)
    story.append(Paragraph("Student Grade Report", title_style))
    story.append(Spacer(1, 12))

    # Student Info
    story.append(Paragraph(f"Student ID: {student.student_id}", styles['Normal']))
    story.append(Paragraph(f"Name: {student.name}", styles['Normal']))
    story.append(Paragraph(f"Email: {student.email}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Grades Table
    data = [["Course Code", "Course Name", "Grade", "Points", "Credits", "Semester"]]
    for grade in grades:
        course = next((c for c in courses if c.code == grade.course_code), None)
        if course:
            points = grade.get_points()
            data.append([grade.course_code, course.name, grade.grade, str(points), str(course.credit_units), grade.semester])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 12))

    # GPA Summary
    cgpa = calculate_cgpa(grades, courses)
    story.append(Paragraph(f"Cumulative GPA (CGPA): {cgpa}", styles['Normal']))

    # Build PDF
    doc.build(story)
    print(f"PDF report generated: {filename}")
