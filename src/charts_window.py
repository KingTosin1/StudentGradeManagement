"""
Charts Window Module

This module defines the ChartsWindow class for displaying charts.
"""

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.charts import plot_gpa_trend, plot_grade_distribution

class ChartsWindow:
    """
    Window for displaying GPA trend and grade distribution charts.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Charts")
        self.window.geometry("800x600")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Title
        self.title_label = ctk.CTkLabel(self.window, text="Charts & Analytics",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Student selector
        student_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        student_frame.pack(pady=10, padx=20, fill="x")
        self.student_label = ctk.CTkLabel(student_frame, text="Select Student:")
        self.student_label.pack(side="left", padx=(0, 10))
        self.student_var = ctk.StringVar()
        self.student_combo = ctk.CTkComboBox(student_frame, variable=self.student_var,
                                            values=[f"{s.student_id} - {s.name}" for s in self.app.students],
                                            command=self.update_charts)
        self.student_combo.pack(side="left", fill="x", expand=True)

        # Tabbed interface
        self.tab_control = ctk.CTkTabview(self.window, width=750, height=450)
        self.tab_control.pack(pady=10, padx=20)

        # GPA Trend Tab
        self.tab_control.add("GPA Trend")
        self.gpa_tab = self.tab_control.tab("GPA Trend")
        self.gpa_canvas = None

        # Grade Distribution Tab
        self.tab_control.add("Grade Distribution")
        self.dist_tab = self.tab_control.tab("Grade Distribution")
        self.dist_canvas = None

        # Export button
        self.export_btn = ctk.CTkButton(self.window, text="Export Chart", command=self.export_chart,
                                       height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.export_btn.pack(pady=(10, 20), padx=20, fill="x")

    def update_charts(self, event):
        """Updates the charts for the selected student."""
        selected = self.student_var.get()
        if not selected:
            return
        student_id = selected.split(" - ")[0]
        student_name = selected.split(" - ")[1]

        # Get student's grades
        student_grades = [g for g in self.app.grades if g.student_id == student_id]

        # GPA Trend Chart
        if self.gpa_canvas:
            self.gpa_canvas.get_tk_widget().destroy()
        fig = plot_gpa_trend(student_grades, student_name, self.app.courses)
        self.gpa_canvas = FigureCanvasTkAgg(fig, master=self.gpa_tab)
        self.gpa_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.gpa_canvas.draw()

        # Grade Distribution Chart
        if self.dist_canvas:
            self.dist_canvas.get_tk_widget().destroy()
        fig2 = plot_grade_distribution(student_grades, student_name)
        self.dist_canvas = FigureCanvasTkAgg(fig2, master=self.dist_tab)
        self.dist_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.dist_canvas.draw()

    def export_chart(self):
        """Exports the current chart as PNG."""
        # Placeholder: Export the active tab's chart
        current_tab = self.tab_control.get()
        if current_tab == "GPA Trend" and self.gpa_canvas:
            plot_gpa_trend([], "Exported")  # Re-plot to save
        elif current_tab == "Grade Distribution" and self.dist_canvas:
            plot_grade_distribution([], "Exported")  # Re-plot to save
        # Note: Actual export logic in charts.py save_chart function
