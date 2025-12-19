"""
GPA Display Window Module

This module defines the GPADisplayWindow class for displaying GPA and CGPA reports.
"""

import customtkinter as ctk
from tkinter import ttk, messagebox
from src.gpa_calculator import calculate_semester_gpa, calculate_cgpa

class GPADisplayWindow:
    """
    Window for displaying GPA and CGPA for a selected student.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("GPA & CGPA Display")
        self.window.geometry("600x400")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Title
        self.title_label = ctk.CTkLabel(self.window, text="GPA & CGPA Display",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Student selection
        self.student_label = ctk.CTkLabel(self.window, text="Select Student:")
        self.student_label.pack(pady=(10, 0))
        self.student_var = ctk.StringVar()
        self.student_combo = ctk.CTkComboBox(self.window, variable=self.student_var,
                                            values=[f"{s.student_id} - {s.name}" for s in self.app.students])
        self.student_combo.pack(pady=(0, 10))

        # Display button
        self.display_btn = ctk.CTkButton(self.window, text="Display GPA", command=self.display_gpa)
        self.display_btn.pack(pady=(10, 10))

        # GPA display area
        self.gpa_frame = ctk.CTkScrollableFrame(self.window)
        self.gpa_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # CGPA label
        self.cgpa_label = ctk.CTkLabel(self.window, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.cgpa_label.pack(pady=(0, 10))

    def display_gpa(self):
        """Displays GPA and CGPA for the selected student."""
        selected = self.student_var.get()
        if not selected:
            messagebox.showerror("Error", "Please select a student.")
            return
        student_id = selected.split(" - ")[0]
        student = next((s for s in self.app.students if s.student_id == student_id), None)
        if not student:
            messagebox.showerror("Error", "Student not found.")
            return

        # Clear previous display
        for widget in self.gpa_frame.winfo_children():
            widget.destroy()

        # Get student's grades
        grades = [g for g in self.app.grades if g.student_id == student_id]

        # Group grades by semester
        semesters = {}
        for grade in grades:
            sem = grade.semester
            if sem not in semesters:
                semesters[sem] = []
            semesters[sem].append(grade)

        # Calculate GPA per semester
        sem_list = sorted(semesters.keys())
        gpa_data = []
        for sem in sem_list:
            gpa = calculate_semester_gpa(semesters[sem], self.app.courses)
            gpa_data.append((sem, gpa))

        # Display semester GPAs in a table
        if gpa_data:
            table_frame = ctk.CTkFrame(self.gpa_frame)
            table_frame.pack(pady=10, fill="x")

            table_label = ctk.CTkLabel(table_frame, text="Semester GPAs", font=ctk.CTkFont(weight="bold"))
            table_label.pack(pady=(10, 5))

            tree = ttk.Treeview(table_frame, columns=("Semester", "GPA"), show="headings", height=5)
            tree.heading("Semester", text="Semester")
            tree.heading("GPA", text="GPA")
            tree.pack(fill="x")

            for sem, gpa in gpa_data:
                tree.insert("", "end", values=(sem, f"{gpa:.2f}"))
        else:
            no_data_label = ctk.CTkLabel(self.gpa_frame, text="No grades available for this student.")
            no_data_label.pack(pady=20)

        # Calculate and display CGPA
        cgpa = calculate_cgpa(grades, self.app.courses)
        self.cgpa_label.configure(text=f"Cumulative GPA (CGPA): {cgpa:.2f}")
