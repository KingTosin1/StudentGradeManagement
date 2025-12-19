"""
PDF Export Dialog Module

This module defines the PDFExportDialog class for exporting PDF reports.
"""

import tkinter as tk
from tkinter import filedialog
from src.pdf_report import generate_student_report

class PDFExportDialog:
    """
    Dialog for selecting student and exporting PDF report.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = tk.Toplevel(root)
        self.window.title("Export PDF Report")
        self.window.geometry("400x200")

        # Student selection
        tk.Label(self.window, text="Select Student:").pack(pady=10)
        self.student_var = tk.StringVar()
        self.student_combo = tk.StringVar()
        self.student_combo = tk.OptionMenu(self.window, self.student_var, *[f"{s.student_id} - {s.name}" for s in self.app.students])
        self.student_combo.pack(pady=5)

        # Filename
        tk.Label(self.window, text="Filename:").pack(pady=5)
        self.filename_entry = tk.Entry(self.window)
        self.filename_entry.insert(0, "student_report.pdf")
        self.filename_entry.pack(pady=5)

        # Export button
        export_button = tk.Button(self.window, text="Export PDF", command=self.export_pdf)
        export_button.pack(pady=20)

    def export_pdf(self):
        """Exports the PDF report."""
        selected = self.student_var.get()
        if not selected:
            tk.messagebox.showerror("Error", "Please select a student.")
            return
        student_id = selected.split(" - ")[0]
        student = next((s for s in self.app.students if s.student_id == student_id), None)
        if not student:
            tk.messagebox.showerror("Error", "Student not found.")
            return

        filename = self.filename_entry.get()
        if not filename:
            tk.messagebox.showerror("Error", "Please enter a filename.")
            return

        grades = [g for g in self.app.grades if g.student_id == student_id]
        generate_student_report(student, grades, self.app.courses, filename)
        tk.messagebox.showinfo("Success", f"PDF exported to {filename}")
        self.window.destroy()
