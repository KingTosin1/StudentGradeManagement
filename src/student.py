"""
Student Model Module

This module defines the Student class, which represents a student in the grade management system.
It includes attributes for student identification and contact information, along with methods
for data validation and string representation.
"""

class Student:
    """
    Represents a student with basic information.

    Attributes:
        student_id (str): Unique identifier for the student.
        name (str): Full name of the student.
        email (str): Email address of the student.
    """

    def __init__(self, student_id, name, email):
        """
        Initializes a Student instance.

        Args:
            student_id (str): Unique student ID.
            name (str): Student's full name.
            email (str): Student's email address.
        """
        self.student_id = student_id
        self.name = name
        self.email = email

    def __str__(self):
        """
        Returns a string representation of the student.

        Returns:
            str: Formatted string with student details.
        """
        return f"ID: {self.student_id}, Name: {self.name}, Email: {self.email}"

    def validate(self):
        """
        Validates the student data.

        Returns:
            bool: True if data is valid, False otherwise.

        Raises:
            ValueError: If validation fails with specific error message.
        """
        if not self.student_id or not isinstance(self.student_id, str):
            raise ValueError("Student ID must be a non-empty string.")
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Name must be a non-empty string.")
        if not self.email or not isinstance(self.email, str) or "@" not in self.email:
            raise ValueError("Email must be a valid string containing '@'.")
        return True

    def to_dict(self):
        """
        Converts the student object to a dictionary for CSV storage.

        Returns:
            dict: Dictionary representation of the student.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Student instance from a dictionary.

        Args:
            data (dict): Dictionary containing student data.

        Returns:
            Student: New Student instance.
        """
        return cls(data["student_id"], data["name"], data["email"])
