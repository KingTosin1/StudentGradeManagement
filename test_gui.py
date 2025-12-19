"""
Test GUI window imports.
"""

try:
    from src.login_window import LoginWindow
    print("LoginWindow OK")
except Exception as e:
    print(f"LoginWindow error: {e}")

try:
    from src.dashboard_window import DashboardWindow
    print("DashboardWindow OK")
except Exception as e:
    print(f"DashboardWindow error: {e}")

try:
    from src.student_management_window import StudentManagementWindow
    print("StudentManagementWindow OK")
except Exception as e:
    print(f"StudentManagementWindow error: {e}")

try:
    from src.course_management_window import CourseManagementWindow
    print("CourseManagementWindow OK")
except Exception as e:
    print(f"CourseManagementWindow error: {e}")

try:
    from src.grade_entry_window import GradeEntryWindow
    print("GradeEntryWindow OK")
except Exception as e:
    print(f"GradeEntryWindow error: {e}")

try:
    from src.gpa_display_window import GPADisplayWindow
    print("GPADisplayWindow OK")
except Exception as e:
    print(f"GPADisplayWindow error: {e}")

try:
    from src.charts_window import ChartsWindow
    print("ChartsWindow OK")
except Exception as e:
    print(f"ChartsWindow error: {e}")

try:
    from src.pdf_export_dialog import PDFExportDialog
    print("PDFExportDialog OK")
except Exception as e:
    print(f"PDFExportDialog error: {e}")

print("GUI import tests completed.")
