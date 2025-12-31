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
        self.window.geometry("900x700")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Title
        self.title_label = ctk.CTkLabel(self.window, text="Academic Management Portal",
                                       font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Top navigation bar
        self.navbar_frame = ctk.CTkFrame(self.window, height=60, corner_radius=0)
        self.navbar_frame.pack(fill="x", padx=0, pady=(0, 20))

        # Navigation buttons in navbar
        nav_buttons = [
            ("Manage Students", self.app.show_student_management),
            ("Manage Courses", self.app.show_course_management),
            ("Enter Grades", self.app.show_grade_entry),
            ("View GPA/CGPA", self.app.show_gpa_display),
            ("View Charts", self.app.show_charts),
            ("Export PDF", self.app.show_pdf_export)
        ]

        for text, command in nav_buttons:
            btn = ctk.CTkButton(self.navbar_frame, text=text, command=command,
                               height=40, font=ctk.CTkFont(size=12, weight="bold"))
            btn.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        # Main content area
        self.content_frame = ctk.CTkFrame(self.window)
        self.content_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Welcome message
        self.welcome_label = ctk.CTkLabel(self.content_frame, text="Welcome to the Student Grade Management System",
                                         font=ctk.CTkFont(size=18, weight="bold"))
        self.welcome_label.pack(pady=(20, 10))

        self.desc_label = ctk.CTkLabel(self.content_frame,
                                      text="Use the navigation bar above to manage students, courses, grades, and generate reports.",
                                      font=ctk.CTkFont(size=14))
        self.desc_label.pack(pady=(0, 20))

        # Quick stats
        self.stats_frame = ctk.CTkFrame(self.content_frame)
        self.stats_frame.pack(pady=10, padx=20, fill="x")

        self.stats_label = ctk.CTkLabel(self.stats_frame,
                                       text=f"Current Statistics:\nStudents: {len(self.app.students)} | Courses: {len(self.app.courses)} | Grades: {len(self.app.grades)}",
                                       font=ctk.CTkFont(size=14))
        self.stats_label.pack(pady=15, padx=20)

        # Logout button at bottom
        self.logout_btn = ctk.CTkButton(self.window, text="Logout",
                                       command=self.logout, fg_color="red", hover_color="darkred",
                                       height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.logout_btn.pack(pady=(20, 10), padx=20, fill="x")

    def logout(self):
        """Logs out and returns to login."""
        self.window.destroy()
        self.app.show_login()
