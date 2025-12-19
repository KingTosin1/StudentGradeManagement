"""
Grade Model Module

This module defines the Grade class, which represents a grade entry for a student in a course.
"""

class Grade:
    """
    Represents a grade for a student in a specific course and semester.

    Attributes:
        student_id (str): ID of the student.
        course_code (str): Code of the course.
        grade (str): Grade letter (A-F).
        semester (str): Semester of the grade.
    """

    VALID_GRADES = ["A", "B", "C", "D", "E", "F"]

    def __init__(self, student_id, course_code, grade, semester):
        """
        Initializes a Grade instance.

        Args:
            student_id (str): Student ID.
            course_code (str): Course code.
            grade (str): Grade (A-F).
            semester (str): Semester.
        """
        self.student_id = student_id
        self.course_code = course_code
        self.grade = grade.upper()
        self.semester = semester

    def __str__(self):
        """
        Returns a string representation of the grade.

        Returns:
            str: Formatted string with grade details.
        """
        return f"Student: {self.student_id}, Course: {self.course_code}, Grade: {self.grade}, Semester: {self.semester}"

    def validate(self):
        """
        Validates the grade data.

        Returns:
            bool: True if data is valid, False otherwise.

        Raises:
            ValueError: If validation fails with specific error message.
        """
        if not self.student_id or not isinstance(self.student_id, str):
            raise ValueError("Student ID must be a non-empty string.")
        if not self.course_code or not isinstance(self.course_code, str):
            raise ValueError("Course code must be a non-empty string.")
        if self.grade not in self.VALID_GRADES:
            raise ValueError(f"Grade must be one of {self.VALID_GRADES}.")
        if not self.semester or not isinstance(self.semester, str):
            raise ValueError("Semester must be a non-empty string.")
        return True

    def get_points(self):
        """
        Returns the point value for the grade (Nigerian scale).

        Returns:
            int: Points (5 for A, 4 for B, etc.).
        """
        points = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
        return points.get(self.grade, 0)

    def to_dict(self):
        """
        Converts the grade object to a dictionary for CSV storage.

        Returns:
            dict: Dictionary representation of the grade.
        """
        return {
            "student_id": self.student_id,
            "course_code": self.course_code,
            "grade": self.grade,
            "semester": self.semester
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Grade instance from a dictionary.

        Args:
            data (dict): Dictionary containing grade data.

        Returns:
            Grade: New Grade instance.
        """
        return cls(data["student_id"], data["course_code"], data["grade"], data["semester"])
