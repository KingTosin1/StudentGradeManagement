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
        self.window.geometry("400x500")
        self.window.resizable(False, False)

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Main title
        self.title_label = ctk.CTkLabel(self.window, text="Academic Portal",
                                       font=ctk.CTkFont(size=22, weight="bold"))
        self.title_label.pack(pady=(25, 5))

        self.subtitle_label = ctk.CTkLabel(self.window, text="Student Grade Management System",
                                          font=ctk.CTkFont(size=14))
        self.subtitle_label.pack(pady=(0, 20))

        # Login card frame
        self.login_frame = ctk.CTkFrame(self.window, corner_radius=15, border_width=2)
        self.login_frame.pack(pady=10, padx=30, fill="x")

        # Username
        self.username_label = ctk.CTkLabel(self.login_frame, text="Username:",
                                          font=ctk.CTkFont(size=12, weight="bold"))
        self.username_label.pack(pady=(20, 5), anchor="w", padx=20)
        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Enter admin username",
                                          height=35)
        self.username_entry.pack(pady=(0, 15), padx=20, fill="x")
        self.username_entry.insert(0, "admin")

        # Password
        self.password_label = ctk.CTkLabel(self.login_frame, text="Password:",
                                          font=ctk.CTkFont(size=12, weight="bold"))
        self.password_label.pack(pady=(10, 5), anchor="w", padx=20)
        self.password_entry = ctk.CTkEntry(self.login_frame, show="*", placeholder_text="Enter password",
                                          height=35)
        self.password_entry.pack(pady=(0, 20), padx=20, fill="x")
        self.password_entry.insert(0, "password")

        # Login button
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login,
                                         height=40, font=ctk.CTkFont(size=14, weight="bold"))
        self.login_button.pack(pady=(10, 20), padx=20, fill="x")

        # Error label
        self.error_label = ctk.CTkLabel(self.login_frame, text="", text_color="red",
                                       font=ctk.CTkFont(size=11))
        self.error_label.pack(pady=(0, 15), padx=20)

        # Ensure the window is updated
        self.window.update()

    def login(self):
        """Handles login authentication."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.window.destroy()
            self.app.show_dashboard()
        else:
            self.error_label.configure(text="Invalid username or password.")
