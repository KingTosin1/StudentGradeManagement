"""
Student Management Window Module

This module defines the StudentManagementWindow class for managing students.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from src.student import Student

class StudentManagementWindow:
    """
    Window for adding, editing, and deleting students.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = tk.Toplevel(root)
        self.window.title("Manage Students")
        self.window.geometry("700x500")

        # Listbox for students
        self.student_listbox = tk.Listbox(self.window, height=15)
        self.student_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.student_listbox.bind('<<ListboxSelect>>', self.on_select)

        # Buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(fill=tk.X, padx=10)
        tk.Button(button_frame, text="Add Student", command=self.add_student).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Edit Selected", command=self.edit_student).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Selected", command=self.delete_student).pack(side=tk.LEFT, padx=5)

        # Search
        search_frame = tk.Frame(self.window)
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.search_entry.bind('<KeyRelease>', self.search_students)

        self.load_students()

    def load_students(self):
        """Loads students into the listbox."""
        self.student_listbox.delete(0, tk.END)
        for student in self.app.students:
            self.student_listbox.insert(tk.END, str(student))

    def on_select(self, event):
        """Handles student selection."""
        pass  # Placeholder for future use

    def add_student(self):
        """Adds a new student."""
        student_id = simpledialog.askstring("Add Student", "Enter Student ID:")
        if not student_id:
            return
        name = simpledialog.askstring("Add Student", "Enter Name:")
        if not name:
            return
        email = simpledialog.askstring("Add Student", "Enter Email:")
        if not email:
            return

        try:
            student = Student(student_id, name, email)
            student.validate()
            self.app.students.append(student)
            self.app.save_data()
            self.load_students()
            messagebox.showinfo("Success", "Student added successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def edit_student(self):
        """Edits the selected student."""
        selection = self.student_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a student to edit.")
            return
        index = selection[0]
        student = self.app.students[index]

        new_id = simpledialog.askstring("Edit Student", "Enter new Student ID:", initialvalue=student.student_id)
        if not new_id:
            return
        new_name = simpledialog.askstring("Edit Student", "Enter new Name:", initialvalue=student.name)
        if not new_name:
            return
        new_email = simpledialog.askstring("Edit Student", "Enter new Email:", initialvalue=student.email)
        if not new_email:
            return

        try:
            student.student_id = new_id
            student.name = new_name
            student.email = new_email
            student.validate()
            self.app.save_data()
            self.load_students()
            messagebox.showinfo("Success", "Student updated successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_student(self):
        """Deletes the selected student."""
        selection = self.student_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a student to delete.")
            return
        index = selection[0]
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            del self.app.students[index]
            self.app.save_data()
            self.load_students()
            messagebox.showinfo("Success", "Student deleted successfully!")

    def search_students(self, event):
        """Filters students based on search query."""
        query = self.search_entry.get().lower()
        self.student_listbox.delete(0, tk.END)
        for student in self.app.students:
            if query in student.name.lower() or query in student.student_id.lower():
                self.student_listbox.insert(tk.END, str(student))