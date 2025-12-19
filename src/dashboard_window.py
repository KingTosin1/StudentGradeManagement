"""
Dashboard Window Module

This module defines the DashboardWindow class for the main application hub.
"""

import customtkinter as ctk

class DashboardWindow:
    """
    Main dashboard window with navigation buttons.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Dashboard - Student Grade Management System")
        self.window.geometry("800x600")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Title
        self.title_label = ctk.CTkLabel(self.window, text="Student Grade Management System",
                                       font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Subtitle
        self.subtitle_label = ctk.CTkLabel(self.window, text="Dashboard",
                                          font=ctk.CTkFont(size=16))
        self.subtitle_label.pack(pady=(0, 20))

        # Navigation buttons frame
        self.button_frame = ctk.CTkFrame(self.window)
        self.button_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Row 1
        self.row1_frame = ctk.CTkFrame(self.button_frame, fg_color="transparent")
        self.row1_frame.pack(pady=10)

        self.student_btn = ctk.CTkButton(self.row1_frame, text="Manage Students",
                                        command=self.app.show_student_management, width=150, height=50)
        self.student_btn.pack(side="left", padx=10)

        self.course_btn = ctk.CTkButton(self.row1_frame, text="Manage Courses",
                                       command=self.app.show_course_management, width=150, height=50)
        self.course_btn.pack(side="left", padx=10)

        # Row 2
        self.row2_frame = ctk.CTkFrame(self.button_frame, fg_color="transparent")
        self.row2_frame.pack(pady=10)

        self.grade_btn = ctk.CTkButton(self.row2_frame, text="Enter Grades",
                                      command=self.app.show_grade_entry, width=150, height=50)
        self.grade_btn.pack(side="left", padx=10)

        self.gpa_btn = ctk.CTkButton(self.row2_frame, text="View GPA/CGPA",
                                    command=self.app.show_gpa_display, width=150, height=50)
        self.gpa_btn.pack(side="left", padx=10)

        # Row 3
        self.row3_frame = ctk.CTkFrame(self.button_frame, fg_color="transparent")
        self.row3_frame.pack(pady=10)

        self.charts_btn = ctk.CTkButton(self.row3_frame, text="View Charts",
                                       command=self.app.show_charts, width=150, height=50)
        self.charts_btn.pack(side="left", padx=10)

        self.pdf_btn = ctk.CTkButton(self.row3_frame, text="Export PDF",
                                    command=self.app.show_pdf_export, width=150, height=50)
        self.pdf_btn.pack(side="left", padx=10)

        # Logout button
        self.logout_btn = ctk.CTkButton(self.window, text="Logout",
                                       command=self.logout, fg_color="red", hover_color="darkred")
        self.logout_btn.pack(pady=(20, 10))

        # Status info
        self.status_label = ctk.CTkLabel(self.window,
                                        text=f"Students: {len(self.app.students)} | Courses: {len(self.app.courses)} | Grades: {len(self.app.grades)}")
        self.status_label.pack(pady=(0, 10))

    def logout(self):
        """Logs out and returns to login."""
        self.window.destroy()
        self.app.show_login()
