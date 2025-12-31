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
        self.window.geometry("750x600")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Scrollable main frame
        self.scrollable_main = ctk.CTkScrollableFrame(self.window)
        self.scrollable_main.pack(fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(self.scrollable_main, text="Course Management",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Add button
        self.add_btn = ctk.CTkButton(self.scrollable_main, text="Add New Course", command=self.show_add_form,
                                    height=35, font=ctk.CTkFont(size=14))
        self.add_btn.pack(pady=(0, 10), padx=20, fill="x")

        # Search
        search_frame = ctk.CTkFrame(self.scrollable_main, fg_color="transparent")
        search_frame.pack(pady=(0, 10), padx=20, fill="x")
        self.search_label = ctk.CTkLabel(search_frame, text="Search Courses:")
        self.search_label.pack(side="left", padx=(0, 10))
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Type to search...")
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.bind('<KeyRelease>', self.search_courses)

        # Scrollable frame for courses
        self.scrollable_frame = ctk.CTkScrollableFrame(self.scrollable_main, height=400)
        self.scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Form frame (hidden initially)
        self.form_frame = ctk.CTkFrame(self.scrollable_main)

        self.form_title = ctk.CTkLabel(self.form_frame, text="", font=ctk.CTkFont(size=16, weight="bold"))
        self.form_title.pack(pady=(15, 10))

        self.code_label = ctk.CTkLabel(self.form_frame, text="Course Code:")
        self.code_label.pack(anchor="w", padx=20)
        self.code_entry = ctk.CTkEntry(self.form_frame, height=35)
        self.code_entry.pack(pady=(0, 10), padx=20, fill="x")

        self.name_label = ctk.CTkLabel(self.form_frame, text="Name:")
        self.name_label.pack(anchor="w", padx=20)
        self.name_entry = ctk.CTkEntry(self.form_frame, height=35)
        self.name_entry.pack(pady=(0, 10), padx=20, fill="x")

        self.credits_label = ctk.CTkLabel(self.form_frame, text="Credit Units:")
        self.credits_label.pack(anchor="w", padx=20)
        self.credits_entry = ctk.CTkEntry(self.form_frame, height=35)
        self.credits_entry.pack(pady=(0, 10), padx=20, fill="x")

        self.semester_label = ctk.CTkLabel(self.form_frame, text="Semester:")
        self.semester_label.pack(anchor="w", padx=20)
        self.semester_entry = ctk.CTkEntry(self.form_frame, height=35)
        self.semester_entry.pack(pady=(0, 15), padx=20, fill="x")

        button_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        button_frame.pack(pady=(10, 15))

        self.save_btn = ctk.CTkButton(button_frame, text="Save", command=self.save_course,
                                     height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.save_btn.pack(side="left", padx=10)

        self.cancel_btn = ctk.CTkButton(button_frame, text="Cancel", command=self.cancel_edit,
                                       fg_color="gray", hover_color="darkgray", height=35,
                                       font=ctk.CTkFont(size=12, weight="bold"))
        self.cancel_btn.pack(side="left", padx=10)

        # Load courses
        self.load_courses()

        # Editing state
        self.editing_course = None

    def load_courses(self):
        """Loads courses into the scrollable frame as cards."""
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for course in self.app.courses:
            self.create_course_card(course)

    def create_course_card(self, course):
        """Creates a card for a course."""
        card_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10, border_width=1)
        card_frame.pack(pady=5, padx=10, fill="x")

        # Course info
        info_label = ctk.CTkLabel(card_frame, text=f"Code: {course.code}\nName: {course.name}\nCredits: {course.credit_units}\nSemester: {course.semester}",
                                 font=ctk.CTkFont(size=12))
        info_label.pack(side="left", padx=15, pady=10, fill="x", expand=True)

        # Buttons
        button_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
        button_frame.pack(side="right", padx=10, pady=10)

        edit_btn = ctk.CTkButton(button_frame, text="Edit", command=lambda: self.show_edit_form(course),
                                width=60, height=30, font=ctk.CTkFont(size=11))
        edit_btn.pack(pady=2)

        delete_btn = ctk.CTkButton(button_frame, text="Delete", command=lambda: self.delete_course(course),
                                  width=60, height=30, fg_color="red", hover_color="darkred",
                                  font=ctk.CTkFont(size=11))
        delete_btn.pack(pady=2)

    def show_add_form(self):
        """Shows the form for adding a new course."""
        self.form_title.configure(text="Add New Course")
        self.code_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.credits_entry.delete(0, "end")
        self.semester_entry.delete(0, "end")
        self.editing_course = None
        self.form_frame.pack(pady=10, padx=20, fill="x")
        self.scrollable_main._parent_canvas.yview_moveto(1.0)  # Scroll to bottom

    def show_edit_form(self, course):
        """Shows the form for editing a course."""
        self.form_title.configure(text="Edit Course")
        self.code_entry.delete(0, "end")
        self.code_entry.insert(0, course.code)
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, course.name)
        self.credits_entry.delete(0, "end")
        self.credits_entry.insert(0, str(course.credit_units))
        self.semester_entry.delete(0, "end")
        self.semester_entry.insert(0, course.semester)
        self.editing_course = course
        self.form_frame.pack(pady=10, padx=20, fill="x")
        self.scrollable_main._parent_canvas.yview_moveto(1.0)  # Scroll to bottom

    def delete_course(self, course):
        """Deletes the selected course."""
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete course {course.name}?"):
            self.app.courses.remove(course)
            self.app.grades = [g for g in self.app.grades if g.course_code != course.code]  # Remove grades too
            self.app.save_data()
            self.load_courses()
            messagebox.showinfo("Success", "Course deleted successfully!")

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
                index = self.app.courses.index(self.editing_course)
                self.app.courses[index] = course
            else:
                # Check for duplicate code
                if any(c.code == code for c in self.app.courses):
                    messagebox.showerror("Error", "Course code already exists.")
                    return
                self.app.courses.append(course)
            self.app.save_data()
            self.load_courses()
            self.cancel_edit()
            messagebox.showinfo("Success", "Course saved successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cancel_edit(self):
        """Cancels editing and hides the form."""
        self.form_frame.pack_forget()
        self.editing_course = None

    def search_courses(self, event):
        """Filters courses based on search query."""
        query = self.search_entry.get().lower()
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for course in self.app.courses:
            if query in course.name.lower() or query in course.code.lower():
                self.create_course_card(course)
