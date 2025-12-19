"""
Charts Window Module

This module defines the ChartsWindow class for displaying charts.
"""

import tkinter as tk
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
        self.window = tk.Toplevel(root)
        self.window.title("Charts")
        self.window.geometry("800x600")

        # Student selector
        tk.Label(self.window, text="Select Student:").pack(pady=5)
        self.student_var = tk.StringVar()
        self.student_combo = ttk.Combobox(self.window, textvariable=self.student_var)
        self.student_combo['values'] = [f"{s.student_id} - {s.name}" for s in self.app.students]
        self.student_combo.pack(pady=5)
        self.student_combo.bind("<<ComboboxSelected>>", self.update_charts)

        # Tabbed interface
        self.tab_control = ttk.Notebook(self.window)
        self.tab_control.pack(fill=tk.BOTH, expand=True)

        # GPA Trend Tab
        self.gpa_tab = tk.Frame(self.tab_control)
        self.tab_control.add(self.gpa_tab, text="GPA Trend")
        self.gpa_canvas = None

        # Grade Distribution Tab
        self.dist_tab = tk.Frame(self.tab_control)
        self.tab_control.add(self.dist_tab, text="Grade Distribution")
        self.dist_canvas = None

        # Export button
        tk.Button(self.window, text="Export Chart", command=self.export_chart).pack(pady=10)

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
        current_tab = self.tab_control.index(self.tab_control.select())
        if current_tab == 0 and self.gpa_canvas:
            plot_gpa_trend([], "Exported")  # Re-plot to save
        elif current_tab == 1 and self.dist_canvas:
            plot_grade_distribution([], "Exported")  # Re-plot to save
        # Note: Actual export logic in charts.py save_chart function
