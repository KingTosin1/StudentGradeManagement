"""
Course Management Window Module

This module defines the CourseManagementWindow class for CRUD operations on courses.
"""

import customtkinter as ctk
from tkinter import messagebox, ttk
from src.course import Course

class CourseManagementWindow:
    """
    Window for managing courses (add, edit, delete, view).
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Course Management")
        self.window.geometry("700x500")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Title
        self.title_label = ctk.CTkLabel(self.window, text="Course Management",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Treeview for courses
        self.tree_frame = ctk.CTkFrame(self.window)
        self.tree_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Code", "Name", "Credits", "Semester"), show="headings")
        self.tree.heading("Code", text="Course Code")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Credits", text="Credits")
        self.tree.heading("Semester", text="Semester")
        self.tree.pack(fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Buttons frame
        self.button_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.add_btn = ctk.CTkButton(self.button_frame, text="Add Course", command=self.add_course)
        self.add_btn.pack(side="left", padx=5)

        self.edit_btn = ctk.CTkButton(self.button_frame, text="Edit Selected", command=self.edit_course)
        self.edit_btn.pack(side="left", padx=5)

        self.delete_btn = ctk.CTkButton(self.button_frame, text="Delete Selected", command=self.delete_course,
                                       fg_color="red", hover_color="darkred")
        self.delete_btn.pack(side="left", padx=5)

        # Form frame (hidden initially)
        self.form_frame = ctk.CTkFrame(self.window)

        self.code_label = ctk.CTkLabel(self.form_frame, text="Course Code:")
        self.code_label.pack(pady=(10, 0))
        self.code_entry = ctk.CTkEntry(self.form_frame)
        self.code_entry.pack(pady=(0, 10))

        self.name_label = ctk.CTkLabel(self.form_frame, text="Name:")
        self.name_label.pack(pady=(10, 0))
        self.name_entry = ctk.CTkEntry(self.form_frame)
        self.name_entry.pack(pady=(0, 10))

        self.credits_label = ctk.CTkLabel(self.form_frame, text="Credit Units:")
        self.credits_label.pack(pady=(10, 0))
        self.credits_entry = ctk.CTkEntry(self.form_frame)
        self.credits_entry.pack(pady=(0, 10))

        self.semester_label = ctk.CTkLabel(self.form_frame, text="Semester:")
        self.semester_label.pack(pady=(10, 0))
        self.semester_entry = ctk.CTkEntry(self.form_frame)
        self.semester_entry.pack(pady=(0, 10))

        self.save_btn = ctk.CTkButton(self.form_frame, text="Save", command=self.save_course)
        self.save_btn.pack(pady=(10, 5))

        self.cancel_btn = ctk.CTkButton(self.form_frame, text="Cancel", command=self.cancel_edit,
                                       fg_color="gray", hover_color="darkgray")
        self.cancel_btn.pack(pady=(0, 10))

        # Load courses
        self.load_courses()

        # Editing state
        self.editing_course = None

    def load_courses(self):
        """Loads courses into the treeview."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for course in self.app.courses:
            self.tree.insert("", "end", values=(course.code, course.name, course.credit_units, course.semester))

    def add_course(self):
        """Shows form for adding a new course."""
        self.editing_course = None
        self.code_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.credits_entry.delete(0, "end")
        self.semester_entry.delete(0, "end")
        self.form_frame.pack(pady=10, padx=20, fill="x")

    def edit_course(self):
        """Shows form for editing selected course."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a course to edit.")
            return
        item = self.tree.item(selected[0])
        values = item["values"]
        self.editing_course = values[0]
        self.code_entry.delete(0, "end")
        self.code_entry.insert(0, values[0])
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, values[1])
        self.credits_entry.delete(0, "end")
        self.credits_entry.insert(0, values[2])
        self.semester_entry.delete(0, "end")
        self.semester_entry.insert(0, values[3])
        self.form_frame.pack(pady=10, padx=20, fill="x")

    def delete_course(self):
        """Deletes the selected course."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a course to delete.")
            return
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this course?"):
            item = self.tree.item(selected[0])
            course_code = item["values"][0]
            self.app.courses = [c for c in self.app.courses if c.code != course_code]
            self.app.grades = [g for g in self.app.grades if g.course_code != course_code]  # Remove grades too
            self.load_courses()

    def save_course(self):
        """Saves the course data."""
        code = self.code_entry.get().strip()
        name = self.name_entry.get().strip()
        credits_str = self.credits_entry.get().strip()
        semester = self.semester_entry.get().strip()

        if not code or not name or not credits_str or not semester:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            credits = int(credits_str)
            course = Course(code, name, credits, semester)
            if self.editing_course:
                # Update existing
                for i, c in enumerate(self.app.courses):
                    if c.code == self.editing_course:
                        self.app.courses[i] = course
                        break
            else:
                # Check for duplicate code
                if any(c.code == code for c in self.app.courses):
                    messagebox.showerror("Error", "Course code already exists.")
                    return
                self.app.courses.append(course)
            self.load_courses()
            self.cancel_edit()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cancel_edit(self):
        """Cancels editing and hides the form."""
        self.form_frame.pack_forget()
        self.editing_course = None
