"""
Grade Entry Window Module

This module defines the GradeEntryWindow class for entering grades.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from src.grade import Grade

class GradeEntryWindow:
    """
    Window for entering grades for students.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = tk.Toplevel(root)
        self.window.title("Enter Grades")
        self.window.geometry("600x400")

        # Student selector
        tk.Label(self.window, text="Select Student:").pack(pady=5)
        self.student_var = tk.StringVar()
        self.student_combo = ttk.Combobox(self.window, textvariable=self.student_var)
        self.student_combo['values'] = [f"{s.student_id} - {s.name}" for s in self.app.students]
        self.student_combo.pack(pady=5)
        self.student_combo.bind("<<ComboboxSelected>>", self.on_student_select)

        # Course selector
        tk.Label(self.window, text="Select Course:").pack(pady=5)
        self.course_var = tk.StringVar()
        self.course_combo = ttk.Combobox(self.window, textvariable=self.course_var)
        self.course_combo.pack(pady=5)

        # Semester selector
        tk.Label(self.window, text="Select Semester:").pack(pady=5)
        self.semester_var = tk.StringVar()
        self.semester_combo = ttk.Combobox(self.window, textvariable=self.semester_var, values=["2023/2024 Semester 1", "2023/2024 Semester 2"])
        self.semester_combo.pack(pady=5)

        # Grade selector
        tk.Label(self.window, text="Select Grade:").pack(pady=5)
        self.grade_var = tk.StringVar()
        self.grade_combo = ttk.Combobox(self.window, textvariable=self.grade_var, values=Grade.VALID_GRADES)
        self.grade_combo.pack(pady=5)

        # Save button
        tk.Button(self.window, text="Save Grade", command=self.save_grade).pack(pady=20)

        # Table for existing grades (placeholder)
        self.grade_table = tk.Text(self.window, height=10, width=50)
        self.grade_table.pack(pady=10)

    def on_student_select(self, event):
        """Updates course combo based on selected student."""
        selected = self.student_var.get()
        if selected:
            student_id = selected.split(" - ")[0]
            # Filter courses (placeholder logic)
            self.course_combo['values'] = [f"{c.code} - {c.name}" for c in self.app.courses]

    def save_grade(self):
        """Saves the entered grade."""
        student_str = self.student_var.get()
        course_str = self.course_var.get()
        semester = self.semester_var.get()
        grade_letter = self.grade_var.get()

        if not all([student_str, course_str, semester, grade_letter]):
            messagebox.showerror("Error", "Please fill all fields.")
            return

        student_id = student_str.split(" - ")[0]
        course_code = course_str.split(" - ")[0]

        # Check for duplicate
        for g in self.app.grades:
            if g.student_id == student_id and g.course_code == course_code and g.semester == semester:
                messagebox.showerror("Error", "Grade already exists for this student, course, and semester.")
                return

        try:
            grade = Grade(student_id, course_code, grade_letter, semester)
            self.app.grades.append(grade)
            self.app.save_data()
            messagebox.showinfo("Success", "Grade saved successfully!")
            self.update_grade_table()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_grade_table(self):
        """Updates the grade table display."""
        self.grade_table.delete(1.0, tk.END)
        student_id = self.student_var.get().split(" - ")[0] if self.student_var.get() else None
        if student_id:
            grades = [g for g in self.app.grades if g.student_id == student_id]
            for g in grades:
                self.grade_table.insert(tk.END, f"{g.course_code}: {g.grade} ({g.semester})\n")