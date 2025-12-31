"""
Student Management Window Module

This module defines the StudentManagementWindow class for managing students.
"""

import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox, simpledialog
from src.student import Student

class StudentManagementWindow:
    """
    Window for adding, editing, and deleting students.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Student Management")
        self.window.geometry("750x600")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Scrollable main frame
        self.scrollable_main = ctk.CTkScrollableFrame(self.window)
        self.scrollable_main.pack(fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(self.scrollable_main, text="Student Management",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Add button
        self.add_btn = ctk.CTkButton(self.scrollable_main, text="Add New Student", command=self.show_add_form,
                                    height=35, font=ctk.CTkFont(size=14))
        self.add_btn.pack(pady=(0, 10), padx=20, fill="x")

        # Search
        search_frame = ctk.CTkFrame(self.scrollable_main, fg_color="transparent")
        search_frame.pack(pady=(0, 10), padx=20, fill="x")
        self.search_label = ctk.CTkLabel(search_frame, text="Search Students:")
        self.search_label.pack(side="left", padx=(0, 10))
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Type to search...")
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.bind('<KeyRelease>', self.search_students)

        # Scrollable frame for students
        self.scrollable_frame = ctk.CTkScrollableFrame(self.scrollable_main, height=400)
        self.scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Form frame (hidden initially)
        self.form_frame = ctk.CTkFrame(self.scrollable_main)

        self.form_title = ctk.CTkLabel(self.form_frame, text="", font=ctk.CTkFont(size=16, weight="bold"))
        self.form_title.pack(pady=(15, 10))

        self.id_label = ctk.CTkLabel(self.form_frame, text="Student ID:")
        self.id_label.pack(anchor="w", padx=20)
        self.id_entry = ctk.CTkEntry(self.form_frame, height=35)
        self.id_entry.pack(pady=(0, 10), padx=20, fill="x")

        self.name_label = ctk.CTkLabel(self.form_frame, text="Name:")
        self.name_label.pack(anchor="w", padx=20)
        self.name_entry = ctk.CTkEntry(self.form_frame, height=35)
        self.name_entry.pack(pady=(0, 10), padx=20, fill="x")

        self.email_label = ctk.CTkLabel(self.form_frame, text="Email:")
        self.email_label.pack(anchor="w", padx=20)
        self.email_entry = ctk.CTkEntry(self.form_frame, height=35)
        self.email_entry.pack(pady=(0, 15), padx=20, fill="x")

        button_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        button_frame.pack(pady=(10, 15))

        self.save_btn = ctk.CTkButton(button_frame, text="Save", command=self.save_student,
                                     height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.save_btn.pack(side="left", padx=10)

        self.cancel_btn = ctk.CTkButton(button_frame, text="Cancel", command=self.cancel_edit,
                                       fg_color="gray", hover_color="darkgray", height=35,
                                       font=ctk.CTkFont(size=12, weight="bold"))
        self.cancel_btn.pack(side="left", padx=10)

        # Load students
        self.load_students()

        # Editing state
        self.editing_student = None

    def load_students(self):
        """Loads students into the scrollable frame as cards."""
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for student in self.app.students:
            self.create_student_card(student)

    def create_student_card(self, student):
        """Creates a card for a student."""
        card_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10, border_width=1)
        card_frame.pack(pady=5, padx=10, fill="x")

        # Student info
        info_label = ctk.CTkLabel(card_frame, text=f"ID: {student.student_id}\nName: {student.name}\nEmail: {student.email}",
                                 font=ctk.CTkFont(size=12))
        info_label.pack(side="left", padx=15, pady=10, fill="x", expand=True)

        # Buttons
        button_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
        button_frame.pack(side="right", padx=10, pady=10)

        edit_btn = ctk.CTkButton(button_frame, text="Edit", command=lambda: self.show_edit_form(student),
                                width=60, height=30, font=ctk.CTkFont(size=11))
        edit_btn.pack(pady=2)

        delete_btn = ctk.CTkButton(button_frame, text="Delete", command=lambda: self.delete_student(student),
                                  width=60, height=30, fg_color="red", hover_color="darkred",
                                  font=ctk.CTkFont(size=11))
        delete_btn.pack(pady=2)

    def show_add_form(self):
        """Shows the form for adding a new student."""
        self.form_title.configure(text="Add New Student")
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.editing_student = None
        self.form_frame.pack(pady=10, padx=20, fill="x")
        self.scrollable_main._parent_canvas.yview_moveto(1.0)  # Scroll to bottom

    def show_edit_form(self, student):
        """Shows the form for editing a student."""
        self.form_title.configure(text="Edit Student")
        self.id_entry.delete(0, "end")
        self.id_entry.insert(0, student.student_id)
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, student.name)
        self.email_entry.delete(0, "end")
        self.email_entry.insert(0, student.email)
        self.editing_student = student
        self.form_frame.pack(pady=10, padx=20, fill="x")
        self.scrollable_main._parent_canvas.yview_moveto(1.0)  # Scroll to bottom

    def save_student(self):
        """Saves the student data."""
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not student_id or not name or not email:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            from src.student import Student
            student = Student(student_id, name, email)
            student.validate()
            if self.editing_student:
                # Update existing
                index = self.app.students.index(self.editing_student)
                self.app.students[index] = student
            else:
                # Check for duplicate ID
                if any(s.student_id == student_id for s in self.app.students):
                    messagebox.showerror("Error", "Student ID already exists.")
                    return
                self.app.students.append(student)
            self.app.save_data()
            self.load_students()
            self.cancel_edit()
            messagebox.showinfo("Success", "Student saved successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cancel_edit(self):
        """Cancels editing and hides the form."""
        self.form_frame.pack_forget()
        self.editing_student = None

    def delete_student(self, student):
        """Deletes the selected student."""
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete student {student.name}?"):
            self.app.students.remove(student)
            self.app.save_data()
            self.load_students()
            messagebox.showinfo("Success", "Student deleted successfully!")

    def search_students(self, event):
        """Filters students based on search query."""
        query = self.search_entry.get().lower()
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for student in self.app.students:
            if query in student.name.lower() or query in student.student_id.lower():
                self.create_student_card(student)
