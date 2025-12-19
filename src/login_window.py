"""
Login Window Module

This module defines the LoginWindow class for admin authentication.
"""

import customtkinter as ctk
from tkinter import messagebox

class LoginWindow:
    """
    Login window for admin authentication.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Login - Student Grade Management System")
        self.window.geometry("400x300")
        self.window.resizable(False, False)

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Title
        self.title_label = ctk.CTkLabel(self.window, text="Student Grade Management System",
                                       font=ctk.CTkFont(size=18, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Username
        self.username_label = ctk.CTkLabel(self.window, text="Username:")
        self.username_label.pack(pady=(10, 0))
        self.username_entry = ctk.CTkEntry(self.window, placeholder_text="admin")
        self.username_entry.pack(pady=(0, 10))
        self.username_entry.insert(0, "admin")

        # Password
        self.password_label = ctk.CTkLabel(self.window, text="Password:")
        self.password_label.pack(pady=(10, 0))
        self.password_entry = ctk.CTkEntry(self.window, show="*", placeholder_text="password")
        self.password_entry.pack(pady=(0, 10))
        self.password_entry.insert(0, "password")

        # Login button
        self.login_button = ctk.CTkButton(self.window, text="Login", command=self.login)
        self.login_button.pack(pady=(20, 10))

        # Error label
        self.error_label = ctk.CTkLabel(self.window, text="", text_color="red")
        self.error_label.pack(pady=(0, 10))

    def login(self):
        """Handles login authentication."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.window.destroy()
            self.app.show_dashboard()
        else:
            self.error_label.configure(text="Invalid username or password.")
