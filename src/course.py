"""
Course Model Module

This module defines the Course class, which represents a course in the grade management system.
It includes attributes for course details and credit units, along with methods for validation
and data conversion.
"""

class Course:
    """
    Represents a course with its details.

    Attributes:
        code (str): Unique course code.
        name (str): Full name of the course.
        credit_units (int): Number of credit units for the course.
        semester (str): Semester in which the course is offered.
    """

    def __init__(self, code, name, credit_units, semester):
        """
        Initializes a Course instance.

        Args:
            code (str): Unique course code.
            name (str): Course name.
            credit_units (int): Credit units (1-6).
            semester (str): Semester (e.g., "2023/2024 Semester 1").
        """
        self.code = code
        self.name = name
        self.credit_units = credit_units
        self.semester = semester

    def __str__(self):
        """
        Returns a string representation of the course.

        Returns:
            str: Formatted string with course details.
        """
        return f"Code: {self.code}, Name: {self.name}, Credits: {self.credit_units}, Semester: {self.semester}"

    def validate(self):
        """
        Validates the course data.

        Returns:
            bool: True if data is valid, False otherwise.

        Raises:
            ValueError: If validation fails with specific error message.
        """
        if not self.code or not isinstance(self.code, str):
            raise ValueError("Course code must be a non-empty string.")
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Course name must be a non-empty string.")
        if not isinstance(self.credit_units, int) or self.credit_units < 1 or self.credit_units > 6:
            raise ValueError("Credit units must be an integer between 1 and 6.")
        if not self.semester or not isinstance(self.semester, str):
            raise ValueError("Semester must be a non-empty string.")
        return True

    def to_dict(self):
        """
        Converts the course object to a dictionary for CSV storage.

        Returns:
            dict: Dictionary representation of the course.
        """
        return {
            "code": self.code,
            "name": self.name,
            "credit_units": self.credit_units,
            "semester": self.semester
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Course instance from a dictionary.

        Args:
            data (dict): Dictionary containing course data.

        Returns:
            Course: New Course instance.
        """
        return cls(data["code"], data["name"], int(data["credit_units"]), data["semester"])
